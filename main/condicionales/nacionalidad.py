america_sur = [
    "argentina",
    "bolivia",
    "brasil",
    "chile",
    "colombia",
    "ecuador",
    "guyana",
    "paraguay",
    "peru",
    "surinam",
    "uruguay",
    "venezuela",
]


norte_america = ["estados unidos", "canada", "mexico"]

centro_america = [
    "guatemala",
    "salvador",
    "cuba",
    "belice",
    "puerto rico",
    "haiti",
    "panama",
]

pais = str(input("Ingrese el pais de nacimiento: "))
pais = pais.lower()

if pais in america_sur:
    print(f"Tu continente de nacimiento es america del sur. ")
elif pais in norte_america:
    print(f"Tu continente de nacimiento es america del norte. ")
elif pais in centro_america:
    print(f"Tu continente de nacimiento es centro america. ")
else:
    print("Tu no naciste en el continente americano.")
