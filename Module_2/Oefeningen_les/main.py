

# x = 3 #variabele is x en value is 3

# kleuren = ('geel', 'paars', 'geel', 'rood', 'geel', 'rood')
# teller = 0

# #Print alle kleuren onder elkaar
# for kleur in kleuren: 
#     print(kleur)

# print(kleuren.count('geel'))


# #groepeer per kleur en geef aantal
# kleuren_teller = {}
# for kleur in kleuren:
#     if kleur in kleuren_teller:
#         kleuren_teller[kleur] += 1
#     else:
#         kleuren_teller[kleur] = 1
# print(kleuren_teller)

# kleuren_teller2 = {}
# for kleur in set(kleuren):
#     kleuren_teller2[kleur] = kleuren.count(kleur)
# print(kleuren_teller2)


# kleuren_teller3 = {kleur : kleuren.count(kleur) for kleur in set(kleuren)}
# print(kleuren_teller3)

# # for kleur in kleuren:
# if kleur == 'geel':
#     teller += 1
# print(f"Er zitten {teller} gele mm's in")
# print(kleuren.count('geel'))

#Goede letters of niet? Mini galgje
geraden = list('_' * 5)
te_raden = 'appel'

geraden[1] = 'p'
geraden[2] = 'p'

print(''.join(geraden))

for l in te_raden:
    print(l)
    print(l == 'p')


import string
woord_te_raden = 'appel'
#verbeter get_letter
def get_letter() -> str:
    while True:
        letter = input("Voer een letter in: ")
        print(letter)
        if len(letter) != 1: 
            print("voer 1 letter in")
        elif letter not in string.ascii_lowercase:
            print('Je voert geen letters in')
        else:
            return letter

geraden_letter = get_letter()
teller_fout = 0
fout_geraden = []
geraden = '_' * len(woord_te_raden)

while teller_fout < 10:
    teller_fout += 1
    geraden_letter = get_letter()
    print(geraden_letter)
    #stap 1
    #controleer of het letter in de te raden woord zit
    if geraden_letter in woord_te_raden:
        print("Letter zit erin")
    else:
        print("Letter zit er niet in probeer opnieuw")
    #stap 2
    #zit letter er niet in moet die in de lijst fout_geraden

    #stap 3
    #zit letter er wel in print de letter op de juiste plaats

    #stap 4
    #

print(f"Je hebt het niet geraden:\n{woord_te_raden} is juiste woord")


#maximaal tien fouten maken
#Tikt iemand 'p' in dan: print('_pp__')