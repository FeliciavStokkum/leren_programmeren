def hello(getallen: int):
    zin = ""
    for x in range(getallen):
        zin += (f"Hello from function town {x + 1}! \n")
    return zin

print(hello(5))