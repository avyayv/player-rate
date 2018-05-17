players = []
games = []
import json

class Player:
    def __init__(self, id, name, current):
        self.id = id
        self.name = name
        self.current = current
        self.offensive_seasons = []
        self.defensive_seasons = []
        self.height = 0
        self.weight = 0
        self.position = ""
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

class OffensiveSeason:
    def __init__(self, playerid, year, teamid, teamabr, age, gp, gs, min, fgm, fga, fgp, threem, threea, threep, ftm, fta, ftp, oreb, dreb, reb, ast, stl, blk, tov, pf, pts):

        self.playerid = playerid
        self.year = year
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

class DefensiveSeason:
    def __init__(self, playerid, teamid, teamabr, age, gp, gs, min, wins, losses, win_p, offensive_rating, defensive_rating, net_rating, ast_pct, ast_to, ast_ratio, oreb_percentage, dreb_percentage, tm_tov_pct, ts_pct, usg_pct, pace, pie):
        self.playerid = playerid
        self.teamid = teamid
        self.teamabr = teamabr
        self.age = age
        self.gp = gp
        self.gs = gs
        self.min = min
        self.wins = wins
        self.losses = losses
        self.win_p = win_p
        self.offensive_rating = offensive_rating
        self.defensive_rating = defensive_rating
        self.net_rating = net_rating
        self.ast_pct = ast_pct
        self.ast_to = ast_to
        self.ast_ratio = ast_ratio
        self.oreb_percentage = oreb_percentage
        self.dreb_percentage = dreb_percentage
        self.tm_tov_pct = tm_tov_pct
        self.ts_pct = ts_pct
        self.usg_pct = usg_pct
        self.pace = pace
        self.pie = pie
class Game:
    def __init__(self, date, id, home_score, away_score, attendance, home_team_id, away_team_id, home_players, away_players, home_inactive_players, away_inactive_players):
        self.date = date
        self.id = id
        self.home_score = home_score
        self.away_score = away_score
        self.attendance = attendance
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.home_players = home_players
        self.away_players = away_players
        self.home_inactive_players = home_inactive_players
        self.away_inactive_players = away_inactive_players
        games.append(self)

def findByName(name):
    # this is not good unless you are debugging something
    for player in players:
        if player.name == name:
            return player
