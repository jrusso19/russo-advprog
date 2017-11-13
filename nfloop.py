class Team:
    teamCount = 0
    AFCCount = 0
    NFCCount = 0

    def __init__(self, name, conference, division, wins, losses):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.conference = conference
        self.division = division
        Team.teamCount += 1
        if conference == "AFC":
            Team.AFCCount += 1
        if conference == "NFC":
            Team.NFCCount += 1

    def ask(self):
        return "the " + self.name + " are " + str(self.wins) + " and " + str(self.losses) + ". They are in the " + self.conference + " " + self.division + " division"


phi = Team("Eagles", "NFC", "East", 8, 1)
atl = Team("Falcons", "NFC", "South", 5, 4)
pit = Team("Steelers", "AFC", "North", 7, 2)
print phi.ask()
print atl.ask()
print pit.ask()
print Team.teamCount
print Team.AFCCount
print Team.NFCCount
