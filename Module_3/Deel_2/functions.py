import time
from termcolor import colored
import math
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HUMAN_COPPER_PER_DAY, COST_FOOD_HORSE_COPPER_PER_DAY, JOURNEY_IN_DAYS, friends, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    silver_amount = copper2silver(amount)
    gold_amount = silver2gold(silver_amount)
    return gold_amount

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    for item in personCash:
        if item == 'copper':
            personCash["gold"] += copper2gold(personCash[item])
        elif item == 'silver':
            personCash["gold"] += silver2gold(personCash[item])
        elif item == 'platinum':
            personCash["gold"] += platinum2gold(personCash[item])
    return personCash["gold"]

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    people_cost = COST_FOOD_HUMAN_COPPER_PER_DAY * people
    horse_cost = COST_FOOD_HORSE_COPPER_PER_DAY * horses
    return round(copper2gold(JOURNEY_IN_DAYS * (people_cost + horse_cost)), 2)

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    nieuwe_list = []
    for dict in list:
        if dict.get(key) == value:
            nieuwe_list.append(dict)

    return nieuwe_list

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    adventuring_friends = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)

    # Return the intersection of the two lists
    return [friend for friend in adventuring_friends if friend in share_with_friends]

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    paarden = math.ceil(people / 2) 
    return paarden

def getNumberOfTentsNeeded(people:int) -> int:
    tenten = math.ceil(people / 3) 
    return tenten

def getTotalRentalCost(horses: int, tents: int) -> float:
    horses_gold_cost = silver2gold(COST_HORSE_SILVER_PER_DAY)
    weeks = math.ceil(JOURNEY_IN_DAYS / 7)

    horses_cost = (horses_gold_cost * JOURNEY_IN_DAYS) * horses
    tents_cost = (weeks * COST_TENT_GOLD_PER_WEEK) * tents
    return float(horses_cost + tents_cost)

##################### O08 #####################

def getItemsAsText(items:list) -> str:
    # Maak een lijst van strings
    formatted_items = [f"{item['amount']}{item['unit']} {item['name']}" for item in items]
    
    # Verwerk de lijst afhankelijk van het aantal items
    if len(formatted_items) == 1:
        return formatted_items[0]
    elif len(formatted_items) == 2:
        return " & ".join(formatted_items)
    else:
        return ", ".join(formatted_items[:-1]) + " & " + formatted_items[-1]
    pass

def getItemsValueInGold(items:list) -> float:
    total_amount = 0
    for item in items:
        item_amount = item['amount']
        item_type = item['price']['type']
        amount = item['price']['amount']

        if item_type == 'platinum':
            amount = platinum2gold(amount) * item_amount
            total_amount = total_amount + amount

        elif item_type == 'copper':
            amount = copper2gold(amount) * item_amount
            total_amount = total_amount + amount

        elif item_type == 'silver':
            amount = silver2gold(amount) * item_amount
            total_amount = total_amount + amount
        
        elif item_type == 'gold':
            amount = amount * item_amount
            total_amount += amount 

    return float(round(total_amount, 2))

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

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