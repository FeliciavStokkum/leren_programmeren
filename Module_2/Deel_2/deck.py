import random

deck = []
deck_kleur = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_waarden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas", "Joker", "Joker"]

for kleur in deck_kleur:
    for waardes in kaart_waarden:
         deck.append(f"{kleur} {waardes}")

random.shuffle(deck)

for i in range(7):
    print(f"Kaart {i + 1}: {deck[i]}")

overgebleven_kaarten = deck[7:]
print(f"\ndeck ({len(overgebleven_kaarten)} kaarten:) {overgebleven_kaarten}")