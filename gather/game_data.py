from nba_py import game
import define_player
import pdb
import json
ids = []
pdb.set_trace()
with open('../data_json_files/gameids.json') as json_data:
    d = json.load(json_data)
    for i in d["ids"]:
        ids.append(i)
        print(i)

with open('../data_json_files/game_data.json', 'a') as file:
    file.write("[")
    for id in ids:
        try:
            boxscore = game.Boxscore(id)
            boxscore_summary = game.BoxscoreSummary(id)
            # print(boxscore_summary.game_summary())
            pdb.set_trace()
            g = define_player.Game(boxscore_summary.game_summary()["GAME_DATE_EST"], str(id), 0, 0, boxscore_summary.game_info()["ATTENDANCE"], boxscore_summary.game_summary()["HOME_TEAM_ID"], boxscore_summary.game_summary()["VISITOR_TEAM_ID"], [], [], [], [])
            for i in boxscore.player_stats():
                if i["MIN"] != None:
                    if i["TEAM_ID"] == g.home_team_id:
                        g.home_players.append(i["PLAYER_ID"])
                    else:
                        g.away_players.append(i["PLAYER_ID"])
                else:
                    if i["TEAM_ID"] == g.home_team_id:
                        g.home_inactive_players.append(i["PLAYER_ID"])
                    else:
                        g.away_inactive_players.append(i["PLAYER_ID"])
            for i in boxscore.team_stats():
                if i["TEAM_ID"] == g.home_team_id:
                    g.home_score = i["PTS"]
                else:
                    g.away_score = i["PTS"]
            print(g.id, g.date, g.home_score, g.away_score, len(g.home_players), len(g.home_inactive_players), len(g.away_players), len(g.away_inactive_players))
            with open('../data_json_files/game_data.json', 'a') as file:
                file.write(json.dumps(g, default=lambda o: o.__dict__))
                file.write(",")
        except IndexError:
            print("err")
    with open('../data_json_files/game_data.json', 'a') as file:
        file.write("]")
