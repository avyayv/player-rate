players = []
games = []
import json
import pdb
from bs4 import BeautifulSoup
from lxml import html
import requests
class Player:
    def __init__(self, id, name, current):
        self.id = id
        self.name = name
        self.current = current
        self.offensive_seasons = []
        self.defensive_seasons = []
        self.advanced_statistics = []
        self.height = 0
        self.weight = 0
        self.position = ""
        self.salary = 0
        players.append(self)
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def current(self):
        return self.current
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
    def find_advanced_for_year(self, year):
        for advanced in self.advanced_statistics:
            if(advanced.year == year):
                return advanced
        return -1
    def ret_stuff(self):
        return ((self.advanced_statistics[-1].secondaryassist+self.offensive_seasons[-1].ast)*2.678245121380469)+self.offensive_seasons[-1].pts+(self.offensive_seasons[-1].reb*1.2076782265205361)+(self.offensive_seasons[-1].stl*1.2076782265205361)+(self.offensive_seasons[-1].blk*1.2076782265205361)-(self.offensive_seasons[-1].tov*1.2076782265205361)-(self.offensive_seasons[-1].pf*1.2076782265205361)
def findById(id):
    for player in players:
        if int(player.id) == int(id):
            return player
    return -1

class PlayerContract:
    def __init__(self):
        self.name = ""
        self.team = ""
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.y4 = 0
        self.y5 = 0
        self.y6 = 0
        self.player_options = []
        self.team_options = []
        self.early_termination = []
        self.signed_using = ""
    def change_team(self,start, end):
        if self.team == start:
            self.team = end
    def dumps(self):
      return "Name "+self.name+" Current Year "+self.y1

class OffensiveSeason:
    def __init__(self, playerid, year, teamid, teamabr, age, gp, gs, min, fgm, fga, fgp,
    threem, threea, threep, ftm, fta, ftp, oreb, dreb, reb, ast, stl, blk, tov, pf, pts):

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
    def __init__(self, playerid, teamid, teamabr, age, gp, gs, min, wins, losses, win_p, offensive_rating, defensive_rating, net_rating, ast_pct, ast_to, ast_ratio, oreb_percentage, dreb_percentage, tm_tov_pct, ts_pct, usg_pct, pace, pie, year):
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
        self.year = year
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

class PlayerTracking:
    def __init__(self, year, rimfgm, rimfga, rimfgp, drivepts, driveast, drivepass,
    drivepf, drivefta, passesmade, passesreceived, secondaryassist, potentialassist,
    pointscreatedbyassist, overallassist, postups, touches, postpasses, posttov,
    postpf, pullupoints, catchshootpoints, posttouchpoints, elbowtouchpoints):
        self.year = year
        self.rimfgm = rimfgm
        self.rimfga = rimfga
        self.rimfgp = rimfgp
        self.drivepts = drivepts
        self.driveast = driveast
        self.drivepass = drivepass
        self.drivepf = drivepf
        self.drivefta = drivefta
        self.passesmade = passesmade
        self.passesreceived = passesreceived
        self.secondaryassist = secondaryassist
        self.potentialassist = potentialassist
        self.pointscreatedbyassist = pointscreatedbyassist
        self.overallassist = overallassist
        self.postups = postups
        self.touches = touches
        self.postpasses = postpasses
        self.posttov = posttov
        self.postpf = postpf
        self.pullupoints = pullupoints
        self.catchshootpoints = catchshootpoints
        self.posttouchpoints = posttouchpoints
        self.elbowtouchpoints = elbowtouchpoints

def findByName(name):
    # this is not good unless you are debugging something
    for player in players:
        if player.name == name:
            return player
"""
http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Defense&Season=2016-17&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=
drive statistics: http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Drives&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=
passing statistics: http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Passing&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=
postup statistics: http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=PostTouch&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=
efficiency statistics: http://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PerMode=PerGame&PlayerExperience=&PlayerOrTeam=Player&PlayerPosition=&PtMeasureType=Efficiency&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight=
"""
