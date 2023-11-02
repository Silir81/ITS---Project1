def form_teams(no_of_teams, param_dataBase): #Definire numar echipe si nr membrii / echipa
    # if randomize == 1:
    #   amesteca

    dataBaseLenght = len(param_dataBase)

    print("Extra players " + str(dataBaseLenght % no_of_teams))

    print("Members who fit in the teams " + str(dataBaseLenght // no_of_teams))

    pool_of_teams = dict()

    for name_of_team in list(range(no_of_teams)):
        name_of_team_str = "Team " + str(name_of_team)
        pool_of_teams[name_of_team_str] = []
        # pool_of_teams.update({name_of_team_str : []})
        for member in param_dataBase[0:dataBaseLenght // no_of_teams]:
            pool_of_teams[name_of_team_str].append(member)
            param_dataBase.remove(member)
    for index in list(range(len(param_dataBase))):
        member = param_dataBase[index]
        print(member)  # list item
        key = list(pool_of_teams.keys())[index]
        print(key)  # key
        # modify the program to include radu/cezar if cezar/radu is already the current team
        # if radu/cezar is already in a team, add cezar/radu in that team only
        list1 = pool_of_teams[key]
        list1.append(member)
        pool_of_teams[key] = list1  # NOT POSSIBLE: pool_of_teams[key].append(member)

    print(pool_of_teams)


if __name__ == "__main__":
    dataBase = ["Andra Urdea",
                "Andrei Roman",
                "Cata Dragusinoiu",
                "Dani Ardelean",
                "Denis Bujor",
                "Mario Dragut",
                "Elvis Chican",
                "Andrei Ilie",
                "Remus Lupu",
                "Norbert Toth",
                "Radu Gugu",
                "Razvan Silisteanu",
                "Radu Videanu",
                "Cezar Hurubean"
                ]

    dataBase2 = ["you", "me", "Dupree"]

    form_teams(3, dataBase)
