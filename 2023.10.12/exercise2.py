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

print(cos_cumparaturi)
print('\n' "cosul nostru are " + str(len(cos_cumparaturi)) + " necesitati in el")