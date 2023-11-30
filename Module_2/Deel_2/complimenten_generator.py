import random

def get_random_compliment(naam: str) -> str:
    MIJN_COMPLIMENTEN = ("Je bent super", "Ga zo door", "Je bent geweldig")
    compliment = random.choices(MIJN_COMPLIMENTEN)
    return f"{compliment} {naam}"

print(get_random_compliment("Felicia"))