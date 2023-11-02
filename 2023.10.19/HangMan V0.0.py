import random

Cuvinte_spanzuratoare = {
"accomplishment",
"communication",
"configuration",
"determination",
"encyclopedia",
"extraordinary",
"inconvenience",
"manipulation",
"observational",
"participation",
"rehabilitation",
"spectacularly",
"unbelievable",
"underestimated",
"unpredictable"
}

print("Salutari. \nHai sa facem cunostinta. \nCare este numele tau?")
Nume = input()
print("\nSalutari", str(Nume).capitalize())

print("\nCuvinte pentru spanzuratoare sunt"
      ":\n")
for key in Cuvinte_spanzuratoare:
    print(key)

# Selecteaza un cuvant aleatoriu din lista
cuvant_aleatoriu = random.choice(list(Cuvinte_spanzuratoare))


# Creaza o lista de caractere "_" si inlocuieste cuvantul selectat cu acest caracter
liniuta = "_ , " * len(cuvant_aleatoriu)

#Creaz o lista cu cuvintele gasite
litera_ghicita = []

print("\nCuvantul selectat este: \n")
print(liniuta)

#Creaza o bucla care va rula atata timp cat nu sunt ghicite toate literele
while "_" in liniuta: #
    litera = input("\n Introdu o litera: \n")


    # verifică dacă este introdusa o singură literă și daca conține doar caractere alfabetice.
    # Dacă nu, imprimă un mesaj de eroare și continuă bucla.
    # isalpha() = Boolean, returneaza valoara de tip TRUE daca este un sir alfanumeric,
    # in caz contrar, valoare de tip FLASE
    if len(litera) != 1 or not litera.isalpha():
        print("\nTe rog sa introduci o singura litera valida\n.")
        continue

    # Liniile urmatoare verifică dacă litera a fost deja ghicită și afișează un mesaj dacă a fost.
    # Apoi continuă la următoarea iterație.
    if litera in litera_ghicita:
        print(f"Ai mai incercat deja litera '{litera}'.")
        continue

    #Se adaugă litera ghicita la lista de litera_ghicita.
    litera_ghicita.append(litera)

    # Urmatoarea secventa verifică dacă litera ghicită se află în cuvântul selectat aleatoriu.
    # In caz afirmativ,bucla trece prin fiecare caracter din cuvânt,iar dacă se potrivește cu litera ghicită,
    # înlocuiește litera.
    # Apoi tipărește cuvântul actualizat pentru jucător.
    if litera in cuvant_aleatoriu:
        for i in range(len(cuvant_aleatoriu)):
            if cuvant_aleatoriu[i] == litera:
                liniuta = liniuta[:i] + litera + liniuta[i + 1:]
        print("Cuvantul pentru spanzuratoare:")
        print(liniuta)