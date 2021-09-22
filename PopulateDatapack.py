from Team import Team
import csv

basePath = 'ICHS/data/ichs/functions/team_setup/'
callPath = 'ichs:team_setup/'

teams = []

teamLeaders = []

#Read the team leaders from file and put them in list to be used later
with open("TeamLeaders.txt", "r") as infile:
    for line in infile.readlines():
        teamLeaders.append(line.replace('\n', ''))

# print(teamLeaders)


teamDataDict = csv.DictReader(open("TeamData.csv"))

#Create Team Objects for ease
i = 0
for teamData in teamDataDict:
    teams.append(Team(teamData['Team Color Name'], teamData['Hex Code'], teamData['Block'], teamData['Team Number'], teamLeaders[i]))
    i += 1

# Create Teams and add leader to them
with open(basePath + "create_teams.mcfunction", "w") as outfile:
    for team in teams:
        curTeamNum = team.getNumber()
        outfile.write(f'#Create Team {curTeamNum} and add leader\n')
        outfile.write(f'team add team{curTeamNum} "Team {curTeamNum}"\n')
        outfile.write(f'team modify team{curTeamNum} color {team.getTeamColorName()}\n')
        outfile.write(f'team join team{curTeamNum} {team.getLeader()}\n\n')

# with open("TeamData.csv", "w") as outfile:
#     outfile.write(f"Team Number,Team Color Name,Hex Code,Block\n")
#     for team in teams:
#         outfile.write(f"{team.number},{team.teamColorName},{team.hexCode},{team.block}\n")


