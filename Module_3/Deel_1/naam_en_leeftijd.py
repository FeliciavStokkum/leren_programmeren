def naam_age():
    #Nieuwe dict voor de name en age
    dict_name_age = {} 
    #De name en age worden opgeslagen in de dict
    dict_name_age['name'] = input("Wat is je naam?: ")  
    dict_name_age['age'] = input("Wat is je leeftijd?: ")  
    return dict_name_age 

def questions():
    #Hier word een lege lijst gemaakt
    lijst = []
    #Zolang dit waar is gaat hij door
    while True:
        #Resultaat word uit de functie naam_age gehaald
        resultaat = naam_age()
        #Hier word dit resultaat in een lijst toegevoegd
        lijst.append(resultaat)
        if input("Toets enter om door te gaan of stop om te printen ").lower() == "stop":
            return lijst
            break

lijst = questions()
for dict in lijst:
    print(f"{dict['name']} is {dict['age']} jaar")