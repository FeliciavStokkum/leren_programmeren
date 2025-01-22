import time, math
from termcolor import colored
from data import JOURNEY_IN_DAYS, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK, COST_INN_HORSE_COPPER_PER_NIGHT, COST_INN_HUMAN_SILVER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount: int) -> float:
    copper2silver = amount / 10
    return copper2silver

def silver2gold(amount: int) -> float:
    silver2gold = amount / 5
    return silver2gold

def gold2silver(amount:int) -> float:
    gold2silver = amount * 5
    return gold2silver

def copper2gold(amount: int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount: int) -> float:
    platinum2gold = amount * 25
    return platinum2gold

def getPersonCashInGold(personCash: dict) -> float:
    copper_in_gold = copper2gold(personCash.get("copper", 0))
    silver_in_gold = silver2gold(personCash.get("silver", 0))
    gold_in_gold = personCash.get("gold", 0)
    platinum_in_gold = platinum2gold(personCash.get("platinum", 0))
    total_gold = copper_in_gold + silver_in_gold + gold_in_gold + platinum_in_gold
    return round(total_gold, 2)

##################### O05 #####################

def getJourneyFoodCostsInGold(people: int, horses: int) -> float:
    total_copper = (
        people * COST_FOOD_HUMAN_COPPER_PER_DAY * JOURNEY_IN_DAYS +
        horses * COST_FOOD_HORSE_COPPER_PER_DAY * JOURNEY_IN_DAYS
    )
    return round(copper2gold(total_copper), 2)

##################### O06 #####################

def getFromListByKeyIs(list: list, key: str, value: any) -> list:
    return [item for item in list if item.get(key) == value]


def getAdventuringPeople(people: list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)


def getShareWithFriends(friends: list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True)


def getAdventuringFriends(friends: list) -> list:
    adventuring_friends = getAdventuringPeople(friends)
    return getShareWithFriends(adventuring_friends)


##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    paarden = math.ceil(people / 2) # paard = max 2 personen rijden
    return paarden

def getNumberOfTentsNeeded(people:int) -> int:
    tenten = math.ceil(people / 3) # tent = max 3 personen slapen
    return tenten

def getTotalRentalCost(horses: int, tents: int) -> float:
    horses_gold_cost = silver2gold(COST_HORSE_SILVER_PER_DAY)
    weeks = math.ceil(JOURNEY_IN_DAYS / 7)

    horses_cost = (horses_gold_cost * JOURNEY_IN_DAYS) * horses
    tents_cost = (weeks * COST_TENT_GOLD_PER_WEEK) * tents
    return float(horses_cost + tents_cost)

##################### O08 #####################

def getItemsAsText(items: list) -> str:
    item_strings = []
    for item in items:
        item_strings.append(f"{item['amount']}{item['unit']} {item['name']}")
    # Combineer de items met komma's en een '&' voor het laatste item
    return ", ".join(item_strings[:-1]) + " & " + item_strings[-1] if len(item_strings) > 1 else item_strings[0]

def getItemsValueInGold(items: list) -> float:
    total_gold = 0.0
    for item in items:
        price = item['price']
        amount = item['amount']

        # Bereken de prijs per eenheid in goud met behulp van de conversiefuncties
        if price['type'] == 'copper':
            unit_price_in_gold = copper2gold(price['amount'])
        elif price['type'] == 'silver':
            unit_price_in_gold = silver2gold(price['amount'])
        elif price['type'] == 'gold':
            unit_price_in_gold = price['amount']  # 1 goud = 1 goud
        elif price['type'] == 'platinum':
            unit_price_in_gold = platinum2gold(price['amount'])
        else:
            raise ValueError(f"Onbekende prijs type: {price['type']}")

        # Vermenigvuldig met de hoeveelheid en voeg toe aan het totaal
        item_total = unit_price_in_gold * amount
        total_gold += item_total

    # Afronden tot 2 decimalen
    return round(total_gold, 2)

##################### O09 #####################

def getCashInGoldFromPeople(people: list) -> float:
    total_gold = 0.0
    
    # Itereer door de lijst van mensen
    for person in people:
        cash = person['cash']
        
        # Converteer de munten naar goud
        copper_in_gold = copper2gold(cash.get("copper", 0))
        silver_in_gold = silver2gold(cash.get("silver", 0))
        gold_in_gold = cash.get("gold", 0)
        platinum_in_gold = platinum2gold(cash.get("platinum", 0))
        
        # Totaal goud voor deze persoon
        total_gold += copper_in_gold + silver_in_gold + gold_in_gold + platinum_in_gold
    
    # Retourneer het totaal aan goud, afgerond op 2 decimalen
    return round(total_gold, 2)

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    result = []
    for investor in investors:
        if investor['profitReturn'] <= 10:
            result.append(investor)
    return result

def getAdventuringInvestors(investors: list) -> list:
    return getFromListByKeyIs(getInterestingInvestors(investors), 'adventuring', True)

def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    total = 0
    interesting = getInterestingInvestors(investors)
    adventuring = getAdventuringInvestors(interesting)

    if adventuring:
        horses = len(adventuring)
        tents = len(adventuring)

        total += getTotalRentalCost(horses, tents)
        total += getJourneyFoodCostsInGold(len(adventuring), horses)
        gear_price =  getItemsValueInGold(gear)
        total += gear_price * len(adventuring)


    return float(round(total, 2))

##################### O11 #####################

# Functie om het aantal nachten te berekenen die maximaal in de herberg overnacht kunnen worden
def getMaxAmountOfNightsInInn(leftoverGold: float, people: int, horses: int) -> int:
    # Converteer het overgebleven goud naar zilver
    leftoverSilver = gold2silver(leftoverGold)
    
    # Kosten per nacht per persoon in zilver
    cost_per_night_human = COST_INN_HUMAN_SILVER_PER_NIGHT
    cost_per_night_horse = copper2silver(COST_INN_HORSE_COPPER_PER_NIGHT)  # Kosten in koper, dus omrekenen naar zilver
    
    # Totale kosten per nacht voor mensen en paarden
    total_cost_per_night = (people * cost_per_night_human) + (horses * cost_per_night_horse)
    
    # Bereken het aantal nachten dat men kan blijven met het overgebleven goud
    max_nights = math.floor(leftoverSilver / total_cost_per_night)
    
    return max_nights

# Functie om de kosten van de herberg voor het verblijf van mensen en paarden te berekenen
def getJourneyInnCostsInGold(nightsInInn: int, people: int, horses: int) -> float:
    # Kosten per nacht per persoon in zilver
    cost_per_night_human = COST_INN_HUMAN_SILVER_PER_NIGHT
    cost_per_night_horse = copper2silver(COST_INN_HORSE_COPPER_PER_NIGHT)  # Kosten in koper, dus omrekenen naar zilver
    
    # Totale kosten per nacht voor mensen en paarden in zilver
    total_cost_per_night = (people * cost_per_night_human) + (horses * cost_per_night_horse)
    
    # Totale kosten voor het aantal nachten in de herberg
    total_cost_in_silver = nightsInInn * total_cost_per_night
    
    # Zet de kosten om naar goud en geef het resultaat terug
    total_cost_in_gold = silver2gold(total_cost_in_silver)
    
    return round(total_cost_in_gold, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    InterestingInvestors = getInterestingInvestors(investors)
    bedrag_investors = []

    for investor in InterestingInvestors:
        procent = investor['profitReturn']
        bedrag = round(profitGold / 100 * procent, 2)
        bedrag_investors.append(bedrag)

    return bedrag_investors

def getAdventurerCut(profitGold: float, investorsCuts: list, fellowship: int) -> float:
    # Bereken het resterende geld na de verdeling aan investeerders
    totalInvestorsShare = sum(investorsCuts)
    remainingGold = profitGold - totalInvestorsShare

    # Zorg ervoor dat er geen negatieve overgebleven goud is
    if remainingGold < 0:
        remainingGold = 0

    # Deel het resterende geld gelijk tussen de avonturiers
    adventurerShare = round(remainingGold / fellowship, 2)

    return adventurerShare


##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    interestingInvestors = getInterestingInvestors(investors)
    adventuringInvestors = getAdventuringInvestors(interestingInvestors)
    investorsCuts = getInvestorsCuts(profitGold, investors)
    goldCut = 0.0
    end_cash = 0.0

    aantal = 1 + len(adventuringFriends) + len(adventuringInvestors)
    cut_index = 0

    # verdeel de uitkomsten
    for person in people:
        end_cash = 0.0
        goldCut = 0.0

        naam = person['name']
        start_cash = round(getCashInGoldFromPeople([person]), 2)
        end_cash += start_cash

        total_adventuring = getAdventurerCut(profitGold, investorsCuts, aantal)

        if person in interestingInvestors:
            goldCut = investorsCuts[cut_index]
            end_cash += goldCut
            cut_index += 1

        elif person in adventuringFriends:
                end_cash -= 10
                for earning in earnings:
                    if earning['name'] == mainCharacter['name']:
                        earning['end'] += 10

        if person == mainCharacter or person in adventuringInvestors or person in adventuringFriends:
            end_cash += total_adventuring


        earnings.append({
            'name'   : naam,
            'start'  : round(start_cash,2),
            'end'    : round(end_cash,2)
        })

    return earnings


##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()