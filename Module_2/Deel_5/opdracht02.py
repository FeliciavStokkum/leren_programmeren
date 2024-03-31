#Print alleen het totaal aantal stuks fruit in de fruitmand, probeer dit zo kort mogelijk te doen.
import fruitmand

#Manier 1
lijst = [] #lege lijst, zodat je elk fruitstuk uit de lijst kan halen

for fruit in fruitmand.fruitmand: #for loop
    lijst.append(fruit) #hier word in de lijst de fruitsoorten geappend

print(len(lijst)) #Hier print ik de lengte van de lijst 

#Manier 2
print(len(fruitmand.fruitmand)) #hij print de hoeveelheid items in fruitmand