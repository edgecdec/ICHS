from Team import Team
def createHelmetsFunction(teams, fileLocation):
    with open(fileLocation, "w") as outfile:
        for i in range(len(teams)):
            curTeam = teams[i]
            teamNum = curTeam.getNumber()
            teamColor = int(str(curTeam.getHexCode()), 16)
            command = f"execute as @a run item replace entity @p[team=team{teamNum}] armor.head with leather_helmet{{Unbreakable:1,Enchantments:[{{id:binding_curse,lvl:1}}],display:{{color:{teamColor}}}}} 1\n\n"
            outfile.write(f"#Put team{teamNum} helmet on\n")
            outfile.write(command)
