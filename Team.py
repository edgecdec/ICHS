class Team:
    def __init__(self, color, hexCode, block, num, leader=""):
        self.teamColorName = color
        self.hexCode = hexCode
        self.block = block
        self.number = num
        self.leader = leader

    def __str__(self):
        output = f"TEAM {self.number}: {self.teamColorName} (leader: {self.leader})\n"
        return output

    def printAllInfo(self):
        f"TEAM {self.number}: {self.teamColorName}-#{self.hexCode} ({self.block}) (leader: {self.leader})\n"

    def getBlock(self):
        return self.block

    def getHexCode(self):
        return self.hexCode

    def getTeamColorName(self):
        return self.teamColorName

    def getNumber(self):
        return self.number

    def getLeader(self):
        return self.leader