#Laat de gebruiker 2 hele getallen invoeren
a = input("Voer getal a in: ")
b = input("Voer getal b in: ")

#Bepaal welk getal groter is dmv een if statement
if a > b: 
    max = a
    print("a is het grootste getal:", max)
elif a < b:
    min = a
    print("a is het kleinste getal:", min)
else: 
    print("a en b zijn even groot")
