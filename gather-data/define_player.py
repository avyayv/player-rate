players = []
import json
class Player:

    def __init__(self, id, name, current):
        self.id = id
        self.name = name
        self.current = current
        self.seasons = []

        players.append(self)
    def getId():
        return self.id
    def getName():
        return self.name
    def current():
        return self.current
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

def findById(id):
    for player in players:
        if player.id == id:
            return player

class Season:
    def __init__(self, playerid, teamid, teamabr, age, gp, gs, min, fgm, fga, fgp, threem, threea, threep, ftm, fta, ftp, oreb, dreb, reb, ast, stl, blk, tov, pf, pts):
        self.playerid = playerid
        self.teamid = teamid
        self.teamabr = teamabr
        self.age = age
        self.gp = gp
        self.gs = gs
        self.min = min
        self.fgm = fgm
        self.fga = fga
        self.fgp = fgp
        self.threem = threem
        self.threea = threea
        self.threep = threep
        self.ftm = ftm
        self.oreb = oreb
        self.dreb = dreb
        self.reb = reb
        self.ast = ast
        self.stl = stl
        self.blk = blk
        self.tov = tov
        self.pf = pf
        self.pts = pts

def findByName(name):
    # this is not good unless you are debugging something
    for player in players:
        if player.name == name:
            return player
