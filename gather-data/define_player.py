players = []
class Player:
    def __init__(self, id, name, current):
        self.id = id
        self.name = name
        self.current = current
        players.append(self)
    def getId():
        return self.id
    def getName():
        return self.name
    def current():
        return self.current
def findById(id):
    for player in players:
        if player.id == id:
            return player
def findByName(name):
    # this is not good unless you are debugging something
    for player in players:
        if player.name == name:
            return player
