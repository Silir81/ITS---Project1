def form_teams(no_of_teams, param_dataBase):
    dataBaseLength = len(param_dataBase)  # Get the length of the dataBase.

    print("Extra players " + str(dataBaseLength % no_of_teams))  # Print the remainder when dividing dataBaseLength by no_of_teams.
    print("Members who fit in the teams " + str(dataBaseLength // no_of_teams))  # Print the integer division of dataBaseLength by no_of_teams.

    pool_of_teams = dict()  # Create an empty dictionary to hold the teams.

    for name_of_team in range(no_of_teams):
        name_of_team_str = "Team " + str(name_of_team)  # Create a team name based on the team number.
        pool_of_teams[name_of_team_str] = []  # Initialize an empty list for each team in the dictionary.

        # Distribute members to teams equally as much as possible.
        for member in param_dataBase[0:dataBaseLength // no_of_teams]:
            pool_of_teams[name_of_team_str].append(member)  # Add the member to the team.
            param_dataBase.remove(member)  # Remove the member from the dataBase.

    # Distribute remaining members to teams in a round-robin fashion.
    for index in range(len(param_dataBase)):
        member = param_dataBase[index]
        print(member)  # Print the member's name.
        key = list(pool_of_teams.keys())[index]  # Get the key (team name) based on the current index.
        print(key)  # Print the team name.

        # Add the member to the current team.
        list1 = pool_of_teams[key]
        list1.append(member)
        pool_of_teams[key] = list1

    print(pool_of_teams)  # Print the final dictionary containing teams and their members.
