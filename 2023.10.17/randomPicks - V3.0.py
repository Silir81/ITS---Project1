def form_teams(no_of_teams, param_dataBase):
    dataBaseLength = len(param_dataBase)
    print("Extra players " + str(dataBaseLength % no_of_teams))
    print("Members who fit in the teams " + str(dataBaseLength // no_of_teams))

    pool_of_teams = dict()

    for name_of_team in range(no_of_teams):
        name_of_team_str = "Team " + str(name_of_team)
        pool_of_teams[name_of_team_str] = []

    # Formeaza Echipa 0 din "Radu Videanu" and "Cezar Hurubean"
    pool_of_teams["Team 0"] = ["Radu Videanu", "Cezar Hurubean"]

    # Distribuie restul membrilor
    rest_of_members = [member for member in param_dataBase if member != "Radu Videanu" and member != "Cezar Hurubean"]
    for member in rest_of_members:
        min_team = min(pool_of_teams, key=lambda team: len(pool_of_teams[team])
        if team != "Team 0"
        else float('inf'))  # Ensure Team 0 is not considered for distribution
        pool_of_teams[min_team].append(member)

    print("Team distribution:")
    team_list = [{"Team Name": team_name, "Members": members} for team_name, members in pool_of_teams.items()]
    for team in team_list:
        print(team)


if __name__ == "__main__":
    dataBase = ["Andra Urdea", "Andrei Roman", "Cata Dragusinoiu", "Dani Ardelean", "Denis Bujor", "Mario Dragut",
                "Elvis Chican", "Andrei Ilie", "Remus Lupu", "Norbert Toth", "Razvan Silisteanu", "Radu Videanu",
                "Cezar Hurubean"]

    form_teams(4, dataBase)
