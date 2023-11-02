# Jocul este organizat în funcții pentru o mai bună modularitate.
# Selectarea cuvintelor și inițializarea jocului sunt funcții separate
# Starea jocului este afișată după fiecare ghicire, arătând cuvântul curent și încercările rămase.
# Bucla jocului continuă până când cuvântul este ghicit sau jucătorul rămâne fără încercări.
# Numele jucătorului este cerut la început, iar mesajul de bun venit este personalizat.


import random

# Definire Lista cuvinte pentru joc
cuvinte = [
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
]

# Definire functie alegere cuvand aleatoriu din Lista
def alege_cuvant_aleatoriu():
    return random.choice(cuvinte)

# funcție inițiere joc.
# Selectează un cuvânt aleatoriu, creează o listă inlocuind literele cuvantului ales cu "_"
# și inițializează variabilele pentru literele ghicite și încercările rămase
def initiere_joc():
    cuvant_de_ghicit = alege_cuvant_aleatoriu()
    cuvant_ghicit = ['_'] * len(cuvant_de_ghicit)
    litera_ghicita = set()
    incercari = 15
    return cuvant_de_ghicit, cuvant_ghicit, litera_ghicita, incercari

# Definire functie afisare status jocul
def afiseaza_status(cuvant_ghicit, incercari):
    print(f"\nCuvantul este: {' '.join(cuvant_ghicit)}")
    print(f"Incercari disponibile: {incercari}")

# Main game loop
def play_hangman():
    print("Bine ai venit la in cadrul jocului Spanzuratoarea")
    name = input("Hai sa facem cunostinta. \nCare este numele tau?\n ").capitalize()
    print(f"\nBuna, {name}!")

    # Apeleaza functia initiere_joc, si atribuie valorile returnare celor 4 variabile
    cuvant_de_ghicit, cuvant_ghicit, litera_ghicita, incercari = initiere_joc()

    # O bucla While care continua atata timp cat jucatorul are încercari ramase
    while incercari > 0:
        afiseaza_status(cuvant_ghicit, incercari)
        litera = input("Ghiceste o litera: ").lower()

        # Verifica dacă este introdusa o singura litera si constă numai din caractere alfabetice.
        if len(litera) != 1 or not litera.isalpha():
            print("Te rog sa introduci o litera valabilavde tip STRING")
            continue

        # verifica dacă litera ghicita a fost folosita înainte.
        if litera in litera_ghicita:
            print(f"Ai folosit deja litera '{litera}'.")
            continue

        #Daca litera este valida și nu a fost folosita, ea este adăugată la setul de litere ghicite
        litera_ghicita.add(litera)

        #Verifica dacă litera ghicită face parte din cuvântul de ghicit.
        if litera in cuvant_de_ghicit:
            #Bucla "FOR" iterează prin caracterele cuvantului care trebuie ghicit.
            for i in range(len(cuvant_de_ghicit)):
                #Verifica daca caracterul curent se potrivește cu litera ghicită.
                if cuvant_de_ghicit[i] == litera:
                    # In caz afirmativ, litera ghicita este adaugata la lista de caractere ale cuvintului care trebuie
                    # ghicit
                    cuvant_ghicit[i] = litera
        else:
            # In caz contrar, numarul incercarilor scade
            incercari -= 1

        # Se verifica daca nu mai există caractere mascate în cuvantul ghicit,
        # indicand că jucătorul a ghicit cu succes cuvantul.
        if '_' not in cuvant_ghicit:
            afiseaza_status(cuvant_ghicit, incercari)
            print("Felicitari, ai ghicit cuvantul!")
            print("Cuvantul selectat a fost:", str(cuvant_de_ghicit).upper())
            break

    if '_' in cuvant_ghicit:
        print(f"Ai epuizat toate incercarile. Cuvantul nominalizat a fost:", str(cuvant_de_ghicit).upper())

if __name__ == "__main__":
    play_hangman()
