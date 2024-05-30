def naam_age():
    dict_name_age = {}  
    name = input("Wat is je naam?: ")  
    age = input("Wat is je leeftijd?: ")  
    dict_name_age['name'] = name  
    dict_name_age['age'] = age 
    return dict_name_age 

resultaat = naam_age()
print(f"{resultaat['name']} is {resultaat['age']} jaar")