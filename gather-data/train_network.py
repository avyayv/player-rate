# import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import numpy
import json
import matplotlib.pyplot as plt

X = []
Y = []
an = []
actual = 0
data = json.load(open('data.json'))
positions = {"Guard":1.0, "Forward":2.0, "Guard-Forward":3.0, "Forward-Guard":4.0, "Forward-Center":5.0, "Center-Forward":6.0, "Center":7.0}
for player in data:
    for counter, season in enumerate(player["defensive_seasons"]):
        if counter < len(player["defensive_seasons"]):
            try:
                a = player["defensive_seasons"][counter]
                n = player["offensive_seasons"][counter]
                nt = player["offensive_seasons"][counter+1]
                at = player["defensive_seasons"][counter+1]
                height = (int(player["height"].split("-")[0])*12)+int(player["height"].split("-")[1])
                weight = int(player["weight"])
                position = positions[player["position"]]
                X.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0, height/90.0, weight/400.0, position/7.0])
                if player["name"] == "Victor Oladipo":
                    an.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0, height/90.0, weight/400.0, position/7.0])
                    actual = nt["pts"]
                Y.append(nt["pts"])
                print("yes")
            except (IndexError, ValueError, ZeroDivisionError):
                continue
model = Sequential()
model.add(Dense(23, input_dim=23, activation='relu'))
model.add(Dense(11, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='mse')
model.fit(X, Y, epochs=1000, batch_size=10)
scores = model.evaluate(X, Y)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
predictions = model.predict(an)


model_json = model.to_json()
with open("points_model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("points_model.h5")
print("Saved model to disk")
