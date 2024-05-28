def aantal(getallen):
    return len(getallen)

# Som van alle getallen in de lijst
def som(getallen):
    return sum(getallen)

# Gemiddelde berekenen
def gemiddelde(som, aantal):
    return som / aantal

# Het grootste getal in de lijst
def grootste_getal(getallen):
    return max(grootste_getal)

# Het kleinste getal in de lijst
def kleinste_getal(getallen):
    return min(kleinste_getal)

# Het eerste getal in de lijst
def eerste_getal(getallen):
    return getallen[0]

# Het kleinste getal gedeeld door het eerste controle getal
def delen1(controlegetal1):
    return kleinste_getal / controlegetal1

# Het grootste getal gedeeld door het tweede controle getal
def delen2(controlegetal2):
    return grootste_getal / controlegetal2

# alle unieke getallen
def unieke_getallen(getallen):
    return list(set(getallen))

# Aantal unieke elementen in de lijst
def aantal_unieke_elementen(unieke_getallen):
    return len(unieke_getallen)

# Verschil tussen aantal unieke elementen en eerste controle getal
def verschil1(controlegetal1):
    return abs(aantal_unieke_elementen - controlegetal1)

# Sorteer de lijst van getallen
def gesorteerde_lijst(getallen):
    return sorted(getallen)

# Sorteer de lijst van unieke getallen
def gesorteerde_lijst_uniek(unieke_getallen):
    return sorted(unieke_getallen)

# Tel het aantal keren dat elk uniek element voorkomt in de lijst
def tel_elementen(getallen):
    telling_elementen = {}
    for getal in getallen:
        aantalkeer = telling_elementen[getal] + 1 if getal in telling_elementen else 1
        telling_elementen[getal] = aantalkeer
    return telling_elementen

# Getallen die deelbaar zijn door het eerste controlle getal
def deelbare_getallen(getallen):
    deelbaar1 = []
    for getal in unieke_getallen:
        if getal % controlegetal1 == 0:
            deelbaar1.append(getal)
    deelbaar1 = sorted(deelbaar1)
    return deelbare_getallen

# Getallen die deelbaar zijn door het tweede controlle getal
def deelbare_getallen2(getallen):
    deelbaar2 = []
    for getal in unieke_getallen:
        if getal % controlegetal2 == 0:
            deelbaar2.append(getal)
    deelbaar2 = sorted(deelbaar2)
    return deelbare_getallen2

# Controleer of een bepaald getallen in de lijst voorkomen
def komt_voor(getallen):
    return controlegetal1 in getallen and controlegetal2 in getallen

# Vindt de posities van heteerste controle getal
def posities(getallen):
    posities = []
    for index, num in enumerate(getallen):
        if num == controlegetal1:
            posities.append(index)
    return posities

# Standaardafwijking berekenen
def standaardafwijking(getallen):
    verschil_kwadraat = sum((x - gemiddelde) ** 2 for x in getallen)
    variantie = verschil_kwadraat / aantal
    standaardafwijking = math.sqrt(variantie)
    return standaardafwijking

# Shuffle de lijst
def shuffle(getallen):
    random.shuffle(getallen)
    return shuffle

# Pak een random getal uit de lijst
def random_getal(getallen):
    random_getal = getallen[random.randint(0,aantal-1)]
    return random_getal

# Verschil tussen twee getallen
def verschil2(getallen):
    verschil2 = abs(random_getal - controlegetal2)
    return verschil2

print(aantal([1,2,3,4,6]))