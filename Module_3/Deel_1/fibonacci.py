def fibonacci(getal1, getal2, length):
    fibonacci_lijst = [getal1, getal2]
    for x in range(length):
        volgende_nummer = fibonacci_lijst[-1] + fibonacci_lijst[-2]
        fibonacci_lijst.append(volgende_nummer)

    return f"{fibonacci_lijst}"
print(fibonacci(0, 1, 8))