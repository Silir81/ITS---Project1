# Partea de introducere
def cunostinta():
    print("Salutari, hai sa facem cunostinta\n")
    nume = input('Introdu numele tau\n')
    print('\nSalutari' , nume.capitalize())

# Functie introducere plaje de numere
def lista_numere():
    nunr = int(input("Cate numere doresti sa operezi? "))
    return nunr

# Functie pentru a citi numerele introduse de utilizator
def citeste_numere(nunr):

    # Definire o lista goala
    numere = []
    for i in range(nunr):
        numar = float(input(f"Introdu numarul {i + 1}: "))
        numere.append(numar)
    return numere


def suma_numere(numere):
    total = 0
    for numar in numere:
        total += numar
    return total

def dif_numere(numere):
    dif = 0
    for numar in numere:
        dif -= numar
    return dif

# Introducere nume
cunostinta()

# Introducere numar dorit de numere
nr_numere = lista_numere()

# Citirea numerelor
numere = citeste_numere(nr_numere)
print(type(numere))


result = suma_numere(numere)
print("Suma numerelor introduse este:", result)

result = dif_numere(numere)
print("Diferenta numerelor introduse este:", result)