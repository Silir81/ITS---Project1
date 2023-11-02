def form_teams(no_of_teams, param_dataBase):
    dataBaseLength = len(param_dataBase)
    print("Extra players " + str(dataBaseLength % no_of_teams))
    print("Members who fit in the teams " + str(dataBaseLength // no_of_teams))

    pool_of_teams = dict()

    for name_of_team in range(no_of_teams):
        name_of_team_str = "Team " + str(name_of_team)
        pool_of_teams[name_of_team_str] = []

    # Ensure "Radu" and "Cezar" are in Team 0
    pool_of_teams["Team 0"] = ["Radu", "Cezar"]

    for member in param_dataBase:
        min_team = min(pool_of_teams, key=lambda team: len(pool_of_teams[team]))
        pool_of_teams[min_team].append(member)

    print("Team distribution:")
    for team_name, team_members in pool_of_teams.items():
        print(f"{team_name}: {team_members}")


if __name__ == "__main__":
    dataBase = ["Andra Urdea", "Andrei Roman", "Cata Dragusinoiu", "Dani Ardelean", "Denis Bujor", "Mario Dragut",
                "Elvis Chican", "Andrei Ilie", "Remus Lupu", "Norbert Toth", "Razvan Silisteanu", "Radu Videanu",
                "Cezar Hurubean"]

    dataBase2 = ["you", "me", "Dupree"]

    form_teams(4
               , dataBase)
