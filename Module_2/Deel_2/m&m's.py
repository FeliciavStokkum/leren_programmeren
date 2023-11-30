import random
m_en_m = ("oranje", "blauw", "groen", "bruin")

hoeveelheid = int(input("Hoeveel M&M's moeten er aan de zak toegevoegd worden?"))

MM_lijst = []

for i in range(hoeveelheid):
    kleuren = random.choice(m_en_m)
    MM_lijst.append(kleuren)


print(f"Dit zijn de kleurtjes: {MM_lijst}")
