from garage import autos

# print(f"U heeft {len(autos)} auto's in de garage")

# print(autos)

# lijst = [6, 2, 3, 5]
#hoe print ik alleen de auto met de kleinste motorinhoud in 1 regel. 

# kleinste_getal = min(lijst)
# print(kleinste_getal)

def get_motorinhoud(a):
    return a['motorinhoud']

auto_kleinste_motor = min(autos, key=get_motorinhoud)
print(auto_kleinste_motor)

auto_kleinste_motor2 = min(autos, key =lambda a: a['motorinhoud'])
print(auto_kleinste_motor2)