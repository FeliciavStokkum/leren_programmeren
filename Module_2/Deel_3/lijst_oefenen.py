pizza_lijst = [
    {"naam": "Margherita", "diameter": 20, "ingredienten": ["tomatensaus", "mozzarella", "basilicum"]},
    {"naam": "Pepperoni", "diameter": 25, "ingredienten": ["tomatensaus", "mozzarella", "pepperoni"]},
    {"naam": "Hawaï", "diameter": 30, "ingredienten": ["tomatensaus", "mozzarella", "ham", "ananas"]},
    {"naam": "Quattro Formaggi", "diameter": 35, "ingredienten": ["tomatensaus", "mozzarella", "gorgonzola", "parmezaan", "fontina"]},
    {"naam": "Veggie", "diameter": 22, "ingredienten": ["tomatensaus", "mozzarella", "paprika", "olijven", "ui", "champignons"]},
    {"naam": "BBQ Chicken", "diameter": 28, "ingredienten": ["BBQ saus", "mozzarella", "kip", "rode ui", "koriander"]},
    {"naam": "Buffalo", "diameter": 26, "ingredienten": ["buffelmozzarella", "tomaat", "basilicum"]},
    {"naam": "Carbonara", "diameter": 32, "ingredienten": ["roomsaus", "mozzarella", "pancetta", "ei", "zwarte peper"]},
    {"naam": "Seafood", "diameter": 24, "ingredienten": ["tomatensaus", "mozzarella", "zeevruchtenmix", "knoflook"]},
    {"naam": "Salami", "diameter": 29, "ingredienten": ["tomatensaus", "mozzarella", "salami"]}
]

# for pizza in pizza_lijst:
#     print(pizza["naam"])

#hoeveel pizza's heb ik?
# print(len(pizza_lijst))


#hoeveel pizza's met ham
teller = 0

for p in pizza_lijst:
    if 'ham' in p['ingredienten']:
        teller += 1
print(teller)

teller2 = sum(1 for pizza in pizza_lijst if 'ham' in pizza['ingredienten'])

teller3 = len(list(filter(lambda a: 'ham' in a['ingredienten'], pizza_lijst)))
print(teller3)
