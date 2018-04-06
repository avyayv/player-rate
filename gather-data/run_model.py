from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
import tensorflow as tf
import json
import numpy
import os
X = []
Y = []
a = []
an = []
n = []
nt = []
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

data = json.load(open('data.json'))
print("What's his name")
player_name = input()
print("What do you predict his usage percentage'll be")
usage_rate = input()
print("How many minutes?")
minutes = input()
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

                X.append([a["net_rating"]/30.0, a["pie"]/30.0, a["ast_to"]/5.0, a["ts_pct"]/5.0, a["tm_tov_pct"]/100.0, a["ast_ratio"]/100.0, a["win_p"], a["usg_pct"], a["defensive_rating"]/200.0, a["offensive_rating"]/200.0, a["pace"]/170.0, n["age"]/50.0, n["pts"]/50.0, n["ast"]/20.0, n["reb"]/40.0, n["stl"]/40.0, n["blk"]/40.0, at["usg_pct"], a["min"]/48.0, at["min"]/48.0])
                Y.append(nt["ast"]/50.0)
            except IndexError:
                pass

        if player["name"] == player_name:
            an.append([advanced["net_rating"]/30.0, advanced["pie"]/30.0, advanced["ast_to"]/5.0, advanced["ts_pct"]/5.0, advanced["tm_tov_pct"]/100.0, advanced["ast_ratio"]/100.0, advanced["win_p"], advanced["usg_pct"], advanced["defensive_rating"]/200.0, advanced["offensive_rating"]/200.0, advanced["pace"]/170.0, nota["age"]/50.0, nota["pts"]/50.0, nota["ast"]/20.0, nota["reb"]/40.0, nota["stl"]/40.0, nota["blk"]/40.0, usage_rate, nota["min"]/48.0, float(minutes)/48.0])
            an.append([advanced["net_rating"]/30.0, advanced["pie"]/30.0, advanced["ast_to"]/5.0, advanced["ts_pct"]/5.0, advanced["tm_tov_pct"]/100.0, advanced["ast_ratio"]/100.0, advanced["win_p"], advanced["usg_pct"], advanced["defensive_rating"]/200.0, advanced["offensive_rating"]/200.0, advanced["pace"]/170.0, nota["age"]/50.0, nota["pts"]/50.0, nota["ast"]/20.0, nota["reb"]/40.0, nota["stl"]/40.0, nota["blk"]/40.0, usage_rate, nota["min"]/48.0, float(minutes)/48.0])

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

print("PTS: "+str((predictionstwo[0]*50).round(1)[0]))
print("AST: "+str((predictionsone[0]*50).round(1)[0]))
print("REB: "+str((predictionsthree[0]*50).round(1)[0]))
