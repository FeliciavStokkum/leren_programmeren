#Controleert of getal even of oneven is
#Parameter is getal hier word True of False aan teruggegeven
#% 2 == 0 controleert of de rest van de deling door 2 gelijk is aan 0. 

def even_odd(number:int) -> bool:
    return number % 2 == 0


#Slaat de zin op in een lijst en draaid de lijst om
#Parameter is een string, er word ook een string terug gegeven
#eerst word de opgegeven zin opgesplits in aparte woorden en deze woord in de lijst gezet
#Dan word de lijst toegevoegd aan elkaar tot weer een zin

def turn_sentence_around(text:str) -> str:
    split_sentence = text.split()
    turned_sentence = split_sentence[::-1]
    add_sentences = ' '.join(turned_sentence)
    return add_sentences

# #Print world hello
print(turn_sentence_around("Hello World"))


#Slaat de 

def kosmische_koekjesmix(galactische_snoepjes:str) -> int:
    planetair_taartje = set(galactische_snoepjes)
    whatchamacallit = len(planetair_taartje)
    return whatchamacallit

print(kosmische_koekjesmix("Hallo"))

# def ruimte_hamsterwiel(planetair_taartje:str) -> float:
#     wobbelwobbel = planetair_taartje.split()
    
#     blork = 0
#     for snorkelwagen in wobbelwobbel:
#         blork += len(snorkelwagen)

#     bizarro_matrix = blork / len(wobbelwobbel)
#     return bizarro_matrix

# def spaghetti_spaceship(infinity_pizza:int, parallelle_tosti:int=10) -> None:
#     for zwabber_krakeling in range(1, parallelle_tosti+1):
#         laser_sandwich = zwabber_krakeling * infinity_pizza
#         print(f'{zwabber_krakeling} x {infinity_pizza} = {laser_sandwich}')