#Laat de gebruiker 2 hele getallen invoeren
a = input("Voer getal a in: ")
b = input("Voer getal b in: ")

#Bepaal welk getal groter is dmv een if statement
if a > b: 
    max = a
    min = b
    print("a is het grootste getal:", max)
    print("Het minimum is", min)
    print("Het maximum is", max)
elif a < b:
    min = a
    max = b
    print("a is het kleinste getal:", min)
    print("Het minimum is", min)
    print("Het maximum is", max)
else: 
    print("a en b zijn even groot")