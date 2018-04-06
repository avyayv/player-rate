# import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import numpy
import json
# # {
# # "current": "alex_abrines",
# # "defensive_seasons": [
# #   {
# #     "teamabr": "OKC",
# #     "gs": 0,
# #     "gp": 72,
#      "net_rating": 0.2,
#      "pie": 0.048,
#      "ast_to": 1.08,
#      "ts_pct": 0.569,
# #     "min": 15,
# #     "playerid": 203518,
#      "tm_tov_pct": 7.2,
# #     "teamid": 1610612760,
#      "ast_ratio": 7.8,
#      "win_p": 0.556,
#      "usg_pct": 0.129,
# #     "dreb_percentage": 0.092,
# #     "ast_pct": 0.036,
#      "defensive_rating": 106.7,
#      "offensive_rating": 106.9,
# #     "wins": 40,
# #     "age": 0,
# #     "losses": 32,
#      "pace": 98.39,
# #     "oreb_percentage": 0.024
# #   },
# #   {
# #     "teamabr": "OKC",
# #     "gs": 0,
# #     "gp": 68,
# #     "net_rating": -2.3,
# #     "pie": 0.052,
# #     "ast_to": 1.21,
# #     "ts_pct": 0.56,
# #     "min": 15.5,
# #     "playerid": 203518,
# #     "tm_tov_pct": 7.6,
# #     "teamid": 1610612760,
# #     "ast_ratio": 9.2,
# #     "win_p": 0.544,
# #     "usg_pct": 0.157,
# #     "dreb_percentage": 0.074,
# #     "ast_pct": 0.055,
# #     "defensive_rating": 108.3,
# #     "offensive_rating": 106,
# #     "wins": 37,
# #     "age": 0,
# #     "losses": 31,
# #     "pace": 101.04,
# #     "oreb_percentage": 0.019
# #   }
# # ],
# # "offensive_seasons": [
# #   {
#      "gs": 6,
#      "gp": 68,
#      "threep": 0.381,
#      "threem": 1.4,
# #     "year": "2016-17",
#      "pts": 6,
#      "threea": 3.6,
#      "min": 15.5,
# #     "playerid": 203518,
#      "tov": 0.5,
# #     "teamid": 1610612760,
#      "pf": 1.7,
#      "blk": 0.1,
#      "reb": 1.3,
#      "ftm": 0.6,
#      "ast": 0.6,
#      "fgp": 0.393,
#      "fgm": 2,
#      "dreb": 1,
#      "fga": 5,
#      "stl": 0.5,
#      "age": 23,
# #     "teamabr": "OKC",
#      "oreb": 0.3
# #   },
# #   {
# #     "gs": 8,
# #     "gp": 72,
# #     "threep": 0.388,
# #     "threem": 1.1,
# #     "year": "2017-18",
# #     "pts": 4.7,
# #     "threea": 2.9,
# #     "min": 15,
# #     "playerid": 203518,
# #     "tov": 0.3,
# #     "teamid": 1610612760,
# #     "pf": 1.6,
# #     "blk": 0.1,
# #     "reb": 1.5,
# #     "ftm": 0.5,
# #     "ast": 0.4,
# #     "fgp": 0.397,
# #     "fgm": 1.5,
# #     "dreb": 1.2,
# #     "fga": 3.8,
# #     "stl": 0.5,
# #     "age": 24,
# #     "teamabr": "OKC",
# #     "oreb": 0.3
# #   }
# # ],
# # "id": 203518,
# # "name": "Alex Abrines"
# # }
#
X = []
Y = []
an = []
actual = 0
data = json.load(open('data.json'))
for player in data:
    for counter, season in enumerate(player["defensive_seasons"]):
        if counter < len(player["defensive_seasons"]):
            try:
                a = player["defensive_seasons"][counter]
                n = player["offensive_seasons"][counter]
                nt = player["offensive_seasons"][counter+1]
                at = player["defensive_seasons"][counter+1]

                X.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0])
                if player["name"] == "Victor Oladipo":
                    an.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0])
                    actual = nt["pts"]
                Y.append(nt["reb"]/50.0)
            except IndexError:
                print("err")
model = Sequential()
model.add(Dense(20, input_dim=20, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse')
model.fit(X, Y, epochs=150, batch_size=10)
scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
predictions = model.predict(an)
print(predictions[-1]*50)
print(actual)

model_json = model.to_json()
with open("rebound_model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("rebound_model.h5")
print("Saved model to disk")
