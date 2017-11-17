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

    def display(self):
        print "the " + self.name + " are " + str(self.wins) + " and " + str(self.losses) + ". They are in the " + self.conference + " " + self.division + " division"

objectlist = []
teamnames = ["Patriots", "Bills", "Dolphins", "Jets", "Steelers", "Ravens", "Bengals", "Browns", "Jaguars", "Titans", "Texans", "Colts", "Chiefs", "Raiders", "Broncos", "Chargers", "Eagles", "Cowboys", "Redskins", "Giants", "Vikings", "Lions", "Packers", "Bears", "Saints", "Panthers", "Falcons", "Buccaneers", "Seahawks", "Rams", "Cardinals", "49ers"]
teamconf = ["AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "AFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", "NFC", ]
teamdiv = ["East", "East", "East", "East", "North", "North", "North", "North", "South", "South", "South", "South", "West", "West", "West", "West", "East", "East", "East", "East", "North", "North", "North", "North", "South", "South", "South", "South", "West", "West", "West", "West"]
teamwins = [7,5,4,4,8,4,3,0,6,6,3,3,6,4,3,3,8,5,4,1,7,5,5,3,7,7,5,3,6,7,4,1]
teamloss = [2,4,5,6,2,5,6,9,3,4,6,7,3,5,6,6,1,4,5,8,2,4,4,6,2,3,4,6,3,2,5,9]

cont =1

while cont ==1:
    abcd = raw_input("Would you like to (l)ist the teams, (s)earch for a team, or (q)uit?")
    if abcd == "q":
        cont = 0
    elif abcd == "l":
        for i in range (0, len(teamnames)):
            objectlist.append(Team(teamnames[i], teamconf[i], teamdiv[i], teamwins[i], teamloss[i]))

    elif abcd == "s":
        print "hi"
    else:
        print "invalid input"


print teamnames[27]
phi = Team("Eagles", "NFC", "East", 8, 1)
atl = Team("Falcons", "NFC", "South", 5, 4)
pit = Team("Steelers", "AFC", "North", 8, 2)
print phi.ask()
print atl.ask()
print pit.ask()
