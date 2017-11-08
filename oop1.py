class Team:
    """A simple example class"""
    i = 0

    def __init__(self, name):
        self.name = name
        self.wins = 0

    def setwins(self, wins):
        self.wins = wins

    def askwins(self):
        return self.wins

    def addwin(self):
        return self.wins + 1

eagles = Team("Eagles")
eagles.setwins(8)
falcons = Team("Falcons")
falcons.setwins(4)
print eagles.askwins()
print falcons.askwins()



# print x.f()
# print x.i
# print x.data
# print x.add()
# print x.addi()
