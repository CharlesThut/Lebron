from sportsipy.nba.teams import Teams

teams = Teams()
for team in teams:
    print(team.name)  # Prints the team's name
    print(team.blocks)  # Prints the team's total blocked shots