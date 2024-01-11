woorden = ["tovenaar", "amulet", "bossen", "toverstaf", "zoektocht"]

vertaling_dict = {
    "tovenaar" : "avonturier",
    "amulet" : "sleutel",
    "bossen" : "grotten",
    "toverstaf" : "zwaard",
    "zoektocht" : "missie",
}

stukje_tekst = input("Type hier een stukje tekst, die je wilt vertalen: ")

woorden_in_tekst = stukje_tekst.split()

vertaalde_woorden = []

for woord in woorden_in_tekst:
    if woord in woorden:
        vertaalde_woorden.append(vertaling_dict[woord])
    else:
        vertaalde_woorden.append(woord)

vertaalde_zin = " ".join(vertaalde_woorden)

for omgekeerde_tekst in vertaalde_woorden[-1]:
    print(omgekeerde_tekst)

print("Vertaalde tekst: ")
print(vertaalde_zin)

#vertaalde tekst omkeren, beginnen bij afwerpen en eindigt bij diep. Hele woorden niet de letters. (2 of 3 manieren)
# print(type(woorden_in_tekst))

#VOORBEED TEKST
#Diep in de betoverende bossen leefde tovenaar Eldor met zijn eeuwenoude amulet en krachtige toverstaf. Toen een profetie hem vertelde over een verloren artefact, begon hij een zoektocht. De bossen wezen hem de weg, en met zijn toverstaf ontsluierde hij oude runen. Het amulet lichtte op, en Eldor wist dat zijn magische zoektocht vruchten zou afwerpen.