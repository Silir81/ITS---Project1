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

def joaca_spanzuratoarea():
    # Selecteaza un cuvant aleatoriu din lista
    cuvant_aleatoriu = random.choice(list(Cuvinte_spanzuratoare))

    # Creaza o lista de caractere "_" si inlocuieste cuvantul selectat cu acest caracter
    liniuta = "_" * len(cuvant_aleatoriu)

    # Creaz o lista cu cuvintele gasite
    litera_ghicita = []


    incercari_ramase = 7

    print("\nCuvantul selectat este: \n")
    print(liniuta)

    # Creaza o bucla care va rula atata timp cat nu sunt ghicite toate literele
    while "_" in liniuta and incercari_ramase > 0:
        litera = input("\n Introdu o litera: \n")

        if len(litera) != 1 or not litera.isalpha():
            print("\nTe rog sa introduci o singura litera valida.\n")
            continue

        if litera in litera_ghicita:
            print(f"Ai mai incercat deja litera '{litera}'.")
            continue

        litera_ghicita.append(litera)

        if litera in cuvant_aleatoriu:
            for i in range(len(cuvant_aleatoriu)):
                if cuvant_aleatoriu[i] == litera:
                    liniuta = liniuta[:i] + litera + liniuta[i + 1:]
            print("Cuvantul pentru spanzuratoare:")
            print(liniuta)
        else:
            incercari_ramase -= 1
            print(f"Litera '{litera}' nu se potriveste. Mai ai {incercari_ramase} incercari.")

    if "_" not in liniuta:
        print("Felicitari, ai castigat! Cuvantul este: " + cuvant_aleatoriu)
    else:
        print("Ai epuizat toate incercarile. Cuvantul corect era: " + cuvant_aleatoriu)

if __name__ == "__main__":
    print("Salutari. \nHai sa facem cunostinta. \nCare este numele tau?")
    Nume = input()
    print("\nSalutari", str(Nume).capitalize())

    print("\nCuvinte pentru spanzuratoare sunt:\n")
    for key in Cuvinte_spanzuratoare:
        print(key)

    while True:
        joaca_spanzuratoarea()
        raspuns = input("Doresti sa joci din nou? (Da/Nu) ").strip().lower()
        if raspuns != "da":
            break
