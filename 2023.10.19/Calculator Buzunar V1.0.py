# Partea de introducere
def cunostinta():
    print("Salutari, hai sa facem cunostinta\n")
    nume = input('Introdu numele tau\n')
    print('\nSalutari' , nume.capitalize())

# Functie introducere plaje de numere
def lista_numere():
    #nunr = variabila pentru numarul de numere :D
    nunr = int(input("Cate numere doresti sa operezi? "))
    return nunr

# Functie pentru a citi numerele introduse de utilizator
def citeste_numere(nunr):
    # Definire o lista goala denumita "numere"
    numere = []
    for i in range(nunr):
        numar = float(input(f"Introdu numarul {i + 1}: "))
        numere.append(numar)
    return numere

def suma_numere(numere):
    # Definire variabila total cu primul obiect (index)
    total = 0
    for numar in numere:
        total += numar
    return total


# Functie initiala diferenta
# def dif_numere(numere):
#     dif = 0
#     for numar in numere:
#         dif -= numar
#     return dif

def dif_numere(numere):
    if len(numere) == 0:
        return 0
    #Definire variabila "dif" cu valoarea index 0 din lista "numere"
    dif = numere[0]

    for numar in numere[1:]:  # Start from the second number
        dif -= numar
    return dif

def produs_numere(numere):
    if len(numere) == 0:
        return 0
    produs = numere[0]  # Initialize with the first number
    # Incepe de la cel de-al doilea element din lista:
    # Acesta este un list slicing. De fapt se creaza o noua lista care include toate elementele de la indexul 1
    # (al doile element din lista) pana la sfarsitul listei.Cu alte cuvinte, excludem din list primul elemnt).
    for numar in numere[1:]:
        produs *= numar
    return produs

# Introducere nume
cunostinta()

# Introducere numar dorit de numere
nr_numere = lista_numere()

# Citirea numerelor
numere = citeste_numere(nr_numere)
print(type(numere))

result = suma_numere(numere)
print("Suma numerelor introduse este:", result)

result1 = dif_numere(numere)
print("Diferenta numerelor introduse este:", result1)

result2 = produs_numere(numere)
print("Produsul numerelor introduse este:", result2)