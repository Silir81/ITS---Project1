# Copiati urmatorul paragraf intr-un fisier nou, si salvati-l sub denumirea de newFile.txt,
# intr-un folder "NewFoldwr" direct pe C

# The rain turned to snow. New skies dawned bright on the green pasture.
# My luck was about to turn for the better once
# I opened Word.
# My favorite TV show is big bang theory.
# Random text on line 4.
# Added new line

# 1.Scrieti o functie care sa sa verifice daca fisierul dat ca argumet pentru functie este intradevar un fisier
# 2.Scrieti o functie care sa deschida fisierul doar cu dreptul de a-l citi
# 3.Scrieti o functie care sa deschida fisierul cu dreptul de citire si de sriere
# 4.Scrieti o functie care va permite sa adaugati o noua linie textului deja existent in fisier
# 5.Scrieti o functie care sa permita sa stergeti fisierul, dar doar daca userul


import os.path
def veriyi_file_existence(file):
    """
    Acesta functie verifica existenta unui fisier.
    Parameters:
        file
    Returns:
        Daca exista, valoarea TREU va fi returnata
        Daca nu exista, valoare FLASE va fi returnata
    -------
    """
    file_check = os.path.isfile(file)
    print("Verificam existenta fisierului")
    if file_check is True:
        print("Fisierul exista")
    else:
        print("Acest fisier nu exista")
    return


def open_file_read(file_read):
    """
    Acesta functie deschide un fisier existent in modul citire.
    Parameters:
        file_read
    Returns:
        Daca fisierul exita va returna continutul fisierului
    -------
    """
    open_file = open(file_read, "r")
    print("Deschidem fisierul in modul 'Citire' si il listam folosind 'readlines'")
    lines = open_file.readlines()
    for line in lines:
        print(line)
    open_file.close()
    return

def open_file_rr(read_write):
    """
    Acesta functie deschide un fisier existent in modul citire.
    Parameters:
        file_read
    Returns:
        Daca fisierul exita va returna continutul fisierului
    -------
    """
    open_file = open(read_write, "r+")
    print("Deschidem fisierul in modul 'Citire' si il listam folosind 'readlines'")

    #Citeste toate liniile din fisierul deschis si le inregistreaza ca o lista in variabila "line"
    lines = open_file.readlines()

    # Itereaza fiecare linie a listei
    for line in lines:
        print(line)
    open_file.close()
    return





if __name__ == "__main__":
    my_string = ("The rain turned to snow. New skies dawned bright on the green pasture."
                     "My luck was about to turn for the better once I opened Word."
                     "My favorite TV show is big bang theory."
                     "Random text on line 4.")

    path_file = "Database/newFile.txt"

    file_name = "newFile.txt"

    print()
    veriyi_file_existence(path_file)
    print()
    open_file_read(path_file)