from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import define_player
import matplotlib.pyplot as plt
import tensorflow as tf
import json
import numpy as np
import os
import sys
X = []
Y = []
a = []
an = []
n = []
nt = []
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
valid_player = False
data = json.load(open("data.json"))
positions = {"Guard":1.0, "Forward":2.0, "Guard-Forward":3.0, "Forward-Guard":4.0, "Forward-Center":5.0, "Center-Forward":6.0, "Center":7.0}

print("What's his name")
player_name = input()


print("What do you predict his usage percentage'll be")
usage_rate = input()

print("Points, Rebounds, or Assists?")
poa = input()
# print("How many minutes?")
# minutes = input()
for player in data:
    for counter, season in enumerate(player["defensive_seasons"]):
        if counter < len(player["defensive_seasons"]):
            advanced = player["defensive_seasons"][-1]
            nota = player["offensive_seasons"][-1]
            try:
                a = player["defensive_seasons"][counter]
                n = player["offensive_seasons"][counter]
                nt = player["offensive_seasons"][counter+1]
                at = player["defensive_seasons"][counter+1]
                position = positions[player["position"]]
                height = (int(player["height"].split("-")[0])*12)+int(player["height"].split("-")[1])
                weight = int(player["weight"])
                X.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0, height/90.0, weight/400.0, position/7.0])
                Y.append(nt["ast"]/50.0)
            except (IndexError, ValueError, KeyError):
                pass

        if player["name"] == player_name:
            height = (int(player["height"].split("-")[0])*12)+int(player["height"].split("-")[1])
            weight = int(player["weight"])
            position = positions[player["position"]]

            if usage_rate == "":
                usage_rate = advanced["usg_pct"]
            an.append([advanced["net_rating"]/30.0, advanced["pie"]/30.0, advanced["ast_to"]/5.0, advanced["ts_pct"]/5.0, advanced["tm_tov_pct"]/100.0, advanced["ast_ratio"]/100.0, advanced["win_p"], advanced["usg_pct"], advanced["defensive_rating"]/200.0, advanced["offensive_rating"]/200.0, advanced["pace"]/170.0, nota["age"]/50.0, nota["pts"]/50.0, nota["ast"]/20.0, nota["reb"]/40.0, nota["stl"]/40.0, nota["blk"]/40.0, usage_rate, nota["min"]/48.0, 24.0/48.0, height/90.0, weight/400.0, position/7.0])
            an.append([advanced["net_rating"]/30.0, advanced["pie"]/30.0, advanced["ast_to"]/5.0, advanced["ts_pct"]/5.0, advanced["tm_tov_pct"]/100.0, advanced["ast_ratio"]/100.0, advanced["win_p"], advanced["usg_pct"], advanced["defensive_rating"]/200.0, advanced["offensive_rating"]/200.0, advanced["pace"]/170.0, nota["age"]/50.0, nota["pts"]/50.0, nota["ast"]/20.0, nota["reb"]/40.0, nota["stl"]/40.0, nota["blk"]/40.0, usage_rate, nota["min"]/48.0, 24.0/48.0, height/90.0, weight/400.0, position/7.0])

json_fileone = open('assist_model.json', 'r')
loaded_model_jsonone = json_fileone.read()
json_fileone.close()
loaded_modelone = model_from_json(loaded_model_jsonone)
loaded_modelone.load_weights("assist_model.h5")
# print("Loaded model from disk")
loaded_modelone.compile(optimizer='adam', loss='mse')
scoreone = loaded_modelone.evaluate(X, Y, verbose=0)
predictionsone = loaded_modelone.predict(an)

json_filetwo = open('points_model.json', 'r')
loaded_model_jsontwo = json_filetwo.read()
json_filetwo.close()
loaded_modeltwo = model_from_json(loaded_model_jsontwo)
loaded_modeltwo.load_weights("points_model.h5")
# print("Loaded model from disk")
loaded_modeltwo.compile(optimizer='adam', loss='mse')
scoretwo = loaded_modeltwo.evaluate(X, Y, verbose=0)
predictionstwo = loaded_modeltwo.predict(an)

json_filethree = open('rebound_model.json', 'r')
loaded_model_jsonthree = json_filethree.read()
json_filethree.close()
loaded_modelthree = model_from_json(loaded_model_jsonthree)
loaded_modelthree.load_weights("rebound_model.h5")
# print("Loaded model from disk")
loaded_modelthree.compile(optimizer='adam', loss='mse')
scorethree = loaded_modelthree.evaluate(X, Y, verbose=0)
predictionsthree = loaded_modelthree.predict(an)

# print("PTS: "+str((predictionstwo[0]*50).round(1)[0]))
# print("AST: "+str((predictionsone[0]*50).round(1)[0]))
# print("REB: "+str((predictionsthree[0]*50).round(1)[0]))
playerx = []
playery = []
number = 0.5
for i in range(1,24):
    an[-1][-4] += 0.02
    playerx.append(an[-1][-4]*48)
    if poa.lower() == "pts":
        playery.append(loaded_modeltwo.predict(an)[-1][0]*50)
        plt.xlabel(player_name+' Minutes', fontsize=15)
        plt.ylabel(player_name+' Points', fontsize=15)
    elif poa.lower() == "reb":
        print(loaded_modelthree.predict(an)[-1][0]*50)
        playery.append(loaded_modelthree.predict(an)[-1][0]*50)
        plt.xlabel(player_name+' Minutes', fontsize=15)
        plt.ylabel(player_name+' Rebounds', fontsize=15)
    else:
        print(loaded_modelone.predict(an)[-1][0]*50)
        playery.append(loaded_modelone.predict(an)[-1][0]*50)
        plt.xlabel(player_name+' Minutes', fontsize=15)
        plt.ylabel(player_name+' Assists', fontsize=15)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Stats Based on Minutes')
line, = ax.plot(playerx, playery, '-o', picker=5)


# line, = ax.plot(np.random.rand(100), 'o', picker=5)  # 5 points tolerance
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    points = xdata[ind].round(1), ydata[ind].round(1)
    print("MINS "+str(points[0][0]), poa.upper()+" "+str(points[1][0]))
fig.canvas.mpl_connect('pick_event', onpick)
plt.errorbar(playerx,playery,yerr=1.0, linestyle="None", barsabove=True)
plt.xlabel(player_name+' Minutes', fontsize=15)
plt.ylabel(player_name+' '+poa.upper(), fontsize=15)
plt.axis([24, 48, 0, 40])
plt.show()
end = input()
