def meten_is_weten():
    a = int(input("Noem een getal: "))
    b = int(input("Noem een 2e getal: "))

    if a > b:
        max_value = a
        min_value = b
        print(f"max is {max_value}")
        print(f"min is {min_value}")
        print(f"a is het grootst getal en de waarde van max = {max_value}.")
    elif a < b:
        max_value = b
        min_value = a
        print(f"max is {max_value}")
        print(f"min is {min_value}")
        print(f"a is het kleinste getal. en de waarde van min = {min_value}")
    else:
        print("a en b zijn even groot")

meten_is_weten()