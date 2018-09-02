import json
import define_player

file = open("college_data.json").read()
json_data = json.loads(file)
seasons = []
for line in json_data:
    season = define_player.CollegeSeason(line["name"], line["season"], line["school"],
    line["classo"], line["gp"], line["gs"], line["min"], line["fgm"], line["fga"],
    line["fgp"], line["threem"], line["threea"], line["threep"], line["ftm"], line["fta"],
    line["ftp"], line["orb"], line["drb"], line["trb"], line["ast"], line["stl"],
    line["blk"], line["pf"], line["tov"], line["pts"], line["owinshares"],
    line["dwinshares"], line["winshares"], line["per"], line["offensive_rating"],
    line["defensive_rating"], line["usagerate"])
    season.rate()
    seasons.append(season)
seasons.sort(key=lambda x: x.rating, reverse=True)
for season in seasons:
    print(season.name, season.rating)
