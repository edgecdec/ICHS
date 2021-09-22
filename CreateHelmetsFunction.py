from Team import Team
def createHelmetsFunction(teams, fileLocation):
    with open(fileLocation, "w") as outfile:
        for i in range(len(teams)):
            curTeam = teams[i]
            teamNum = curTeam.getNumber()
            teamColor = int(str(curTeam.getHexCode()), 16)
            command = f"execute as @p run replaceitem entity @a[team=team{teamNum}] armor.head leather_helmet 1 0 {{display:{{color:{teamColor}}}}}\n\n"
            outfile.write(f"#Put team{teamNum} helmet on\n")
            outfile.write(command)
