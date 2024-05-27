#Controleert of getal even of oneven is
#Parameter is getal hier word True of False aan teruggegeven
#% 2 == 0 controleert of de rest van de deling door 2 gelijk is aan 0. 

def even_odd(number:int) -> bool:
    return number % 2 == 0

#Geeft True terug
print(even_odd(10))

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

#Deze functie bekijkt hoeveel verschillende tekens erin de string zitten
#Dan worden de tekens opgeslagen in set 
#Dan word de lengte bepaald van de characters 
#Dan geeft hij de lengte van de tekens terug

def different_characters(characters_text:str) -> int:
    all_charachters = set(characters_text)
    len_charachters = len(all_charachters)
    return len_charachters

#Geeft 8 terug
print(different_characters("Hello World"))

# Deze functie berekend het gemiddelde aantal tekens per woord in de string
# Je geeft een string op, hier komt een float uit
# Eerst word de opgegeven string opgesplitst, deze word opgeslagen in een variabele
# de counter telt hoeveel worden er in de opgegeven zin zitten
# dan word de hoeveelheid worden gedeeld door de lengte van de gesplitte tekst
# Dan returnt hij de float

def average_word_length(sentence_input:str) -> float:
    sentence_split = sentence_input.split()
    
    counter = 0
    for word in sentence_split:
        counter += len(word)

    results = counter / len(sentence_split)
    return results

#Geeft 4.25 terug
print(average_word_length("Mijn naam is Felicia"))

#Deze functie berekend de tafel met wat je invoert
#Je voert een getal in, het tweede getal staat al vast in de parameter
#vervolgens word per getal in range de berekening gemaakt
#Dat is de getal in de range keer het getal dat je invult
#Dan wordt de uitslag geprint

def tafel_berekening(getal:int, getal_10:int=10) -> None:
    for getal in range(1, getal_10+1):
       berekening = getal * getal
       print(f'{getal} x {getal} = {berekening}')

print(tafel_berekening(2))