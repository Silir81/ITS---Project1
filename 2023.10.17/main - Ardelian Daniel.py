import random

numbers_card = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
type_cards = ["Heart_Red", "Heart_Black", "Romb", "Trefla"]

def poker_cards():
    deck_of_cards = []
    for x_numbers in numbers_card:
        for x_type in type_cards:
            values = x_numbers + "_" + x_type
            deck_of_cards.append(values)
    return deck_of_cards

# amestec carti
final_deck = poker_cards()
random.shuffle(final_deck)

def random_5_cards():
    list_cards = []
    for i in final_deck:
        if len(list_cards) < 5:
            x = final_deck[random.randint(1, len(final_deck))]
            list_cards.append(x)
            final_deck.remove(x)
    return list_cards

if __name__ == "__main__":
    final_deck = poker_cards()
    random.shuffle(final_deck)
    print("Let's play a poker game. The numbers of players should be between 2 and 4")
    print("\n")
    numbers_of_players = int(input("How many players will join the game: "))
    if numbers_of_players >= 2 and numbers_of_players <=4:
        if numbers_of_players == 2:
            players_1 = input("Enter the name of Player 1: ")
            player_1_card = {}
            cards_player_1 = random_5_cards()
            player_1_card[players_1] = cards_player_1
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_2 = input("Enter the name of Player 2: ")
            player_2_card = {}
            cards_player_2 = random_5_cards()
            player_2_card[players_2] = cards_player_2
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

        elif numbers_of_players == 3:
            players_1 = input("Enter the name of Player 1: ")
            player_1_card = {}
            cards_player_1 = random_5_cards()
            player_1_card[players_1] = cards_player_1
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_2 = input("Enter the name of Player 2: ")
            player_2_card = {}
            cards_player_2 = random_5_cards()
            player_2_card[players_2] = cards_player_2
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_3 = input("Enter the name of Player 3: ")
            player_3_card = {}
            cards_player_3 = random_5_cards()
            player_3_card[players_3] = cards_player_3
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

        elif numbers_of_players == 4:
            players_1 = input("Enter the name of Player 1: ")
            player_1_card = {}
            cards_player_1 = random_5_cards()
            player_1_card[players_1] = cards_player_1
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_2 = input("Enter the name of Player 2: ")
            player_2_card = {}
            cards_player_2 = random_5_cards()
            player_2_card[players_2] = cards_player_2
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_3 = input("Enter the name of Player 3: ")
            player_3_card = {}
            cards_player_3 = random_5_cards()
            player_3_card[players_3] = cards_player_3
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

            players_4 = input("Enter the name of Player 4: ")
            player_4_card = {}
            cards_player_4 = random_5_cards()
            player_4_card[players_4] = cards_player_4
            print("\n")
            print("------------INFO: The length of the deck of cards is: " + str(len(final_deck)) + "------------")

    else:
        print("To much players, please try again")

    if numbers_of_players == 2:
        print("The 1 player is: " + str(players_1) + " with the cards: " + str(cards_player_1))
        print("The 2 player is: " + str(players_2) + " with the cards: " + str(cards_player_2))

    elif numbers_of_players == 3:
        print("The 1 player is: " + str(players_1) + " with the cards: " + str(cards_player_1))
        print("The 2 player is: " + str(players_2) + " with the cards: " + str(cards_player_2))
        print("The 3 player is: " + str(players_3) + " with the cards: " + str(cards_player_3))

    elif numbers_of_players == 4:
        print("The 1 player is: " + str(players_1) + " with the cards: " + str(cards_player_1))
        print("The 2 player is: " + str(players_2) + " with the cards: " + str(cards_player_2))
        print("The 3 player is: " + str(players_3) + " with the cards: " + str(cards_player_3))
        print("The 4 player is: " + str(players_4) + " with the cards: " + str(cards_player_4))






