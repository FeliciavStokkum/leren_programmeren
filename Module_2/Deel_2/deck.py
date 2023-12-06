import random

deck = []
deck_kleur = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_waarden = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "boer", "vrouw", "heer", "aas"]

for kleur in deck_kleur:
    for waardes in kaart_waarden:
         deck.append(f"{kleur} {waardes}")

deck.append("Joker")
deck.append("Joker")

random.shuffle(deck)
print(deck)

for i in range(7):
    card = deck.pop(0)
    print(card)

    # print(f"Kaart {i + 1}: {deck[1]}")

# overgebleven_kaarten = deck[7:]
# print(f"\ndeck ({len(overgebleven_kaarten)} kaarten:) {overgebleven_kaarten}")
