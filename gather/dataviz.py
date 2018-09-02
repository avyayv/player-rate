# import tensorflow as tf

import numpy
import json
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

X = []

class ThirtySixTest:
    def __init__(self, name):
        self.name = name
        self.season = []
class

data = json.load(open('analyze_with_statistics/newer_data.json'))
for player in data:
    new_player = Player(name=player["name"])
    for counter, season in enumerate(player["defensive_seasons"]):
        if counter < len(player["defensive_seasons"]):
            try:
                a = player["defensive_seasons"][counter]
                n = player["offensive_seasons"][counter]
                height = (int(player["height"].split("-")[0])*12)+int(player["height"].split("-")[1])
                weight = int(player["weight"])
                position = player["position"]
                if position == "Center" and a["gp"]>50.0:
                    if int(a["year"].split("-")[0])<2009:
                        X.append({"Time": "Before","net_rating":a["net_rating"], "pie":a["pie"], "ast_to":a["ast_to"], "ts_pct":a["ts_pct"], "tm_tov_pct":a["tm_tov_pct"], "ast_ratio":a["ast_ratio"], "win_p":a["win_p"], "usg_pct":a["usg_pct"], "defensive_rating":a["defensive_rating"], "offensive_rating":a["offensive_rating"], "pace":a["pace"], "age":n["age"], "pts":n["pts"], "ast":n["ast"], "reb":n["reb"], "stl":n["stl"], "blk":["blk"], "minutes":a["min"], "height":height, "weight":weight, "position":position})
                    else:
                        X.append({"Time": "After","net_rating":a["net_rating"], "pie":a["pie"], "ast_to":a["ast_to"], "ts_pct":a["ts_pct"], "tm_tov_pct":a["tm_tov_pct"], "ast_ratio":a["ast_ratio"], "win_p":a["win_p"], "usg_pct":a["usg_pct"], "defensive_rating":a["defensive_rating"], "offensive_rating":a["offensive_rating"], "pace":a["pace"], "age":n["age"], "pts":n["pts"], "ast":n["ast"], "reb":n["reb"], "stl":n["stl"], "blk":["blk"], "minutes":a["min"], "height":height, "weight":weight, "position":position})

            except (IndexError, ValueError, ZeroDivisionError):
                continue

# panda_frame = pd.DataFrame(X)
#
# sns.set_style('whitegrid')
#
# sns.boxplot(x='Time', y='usg_pct', data=panda_frame)
# print(panda_frame)
# plt.show()
