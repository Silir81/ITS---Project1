import random

database_of_beautiful_necessities = [
    "iPad",
    "espresso",
    "monitor",
    "mouse",
    "laptop stand",
    "rack pentru SDD extern",
    "birou reglabil pe inaltime",
    "casti",
    "MacBook",
    "airfrier",
    "pat",
    "dulap",
    "scaun gaming",
    "cooler laptop",
    "webcam",
    "tastatura",
    "drona",
    "placa video",
    "set jenti moto",
    "vacanta italia",
    "PS5",
    "turbina noua",
    "masina",
    "boxe",
    "scaun de masaj",
    "apple watch",
    "scaun auto bebe",
    "patut bebe",
    "monitor mai generos",
    "tastatura mecanica"
]

cos_cumparaturi = dict()
print(len(database_of_beautiful_necessities))
while len(cos_cumparaturi) < 15:
    index_random = random.randint(0, 14)
    if database_of_beautiful_necessities[index_random] not in cos_cumparaturi:
        cos_cumparaturi[
            database_of_beautiful_necessities[index_random]
        ] = random.randint(50, 200)


# Definire functie suma din totalul valorii ariticolelor din Dictionar)
# Sursa: https://www.geeksforgeeks.org/python-program-to-find-the-sum-of-all-items-in-a-dictionary/
Total_valore_cos = sum(cos_cumparaturi.values())

# print(cos_cumparaturi)
print('\n' "Cosul nostru are " + str(len(cos_cumparaturi)) + " necesitati in el ")
print("\nValoarea totala a cosului este: ", type(Total_valore_cos), Total_valore_cos, '\n')
for key, value in cos_cumparaturi.items():
    print(f"{key}: {value}")

# Introducerea limitei de buget
setare_buget = int(input("\nIntroduceti bugetul alocat"'\n'))
# print Setare_buget:

# Eliminare obiecte din lista pana la limita intodusa
while Total_valore_cos > setare_buget:
    item, cost = cos_cumparaturi.popitem()
    Total_valore_cos -= cost
    print("\u0332".join("\nCu regret trebuie sa te informez ca nu te-ai incadrat in buget.\nVom elimina anumite elemente din cos!"))
    print("\nAm eliminat:", item.upper(), "din cos")
    print('\n' "Cosul nostru are " + str(len(cos_cumparaturi)) + " necesitati in el ")
    print("\nValoarea totala a cosului este: ", type(Total_valore_cos), Total_valore_cos, '\n')
    for key, value in cos_cumparaturi.items():
        print(f"{key}: {value}")


if Total_valore_cos < setare_buget:
    print("\nFelicitari, te-ai incadrat in bugetul stabilit: ", Total_valore_cos)
# else:
#    print("Cu regret trebuie sa te informez ca nu te-ai incadrat in buget.\nVom elimina anumite elemente din cos!")
