# this file will get player offensive statistics
import get_ids
import json
import time
import datetime
import argparse

from requests_futures.sessions import FuturesSession

parser = argparse.ArgumentParser(description='Get Information')
parser.add_argument('startid', metavar='N', type=str, nargs='+',
                    help='if there was an error you can start from here. if this is the beginning, 0. The start id will be printed onto the console next to the name')
parser.add_argument('filename', metavar='N', type=str, nargs='+',
                    help='file name.json')
args = parser.parse_args()

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

number = 0

# if you adjust start_id make sure to comment the [

start_id = args.startid
file_name = args.filename
# with open(file_name[0], 'a') as file:
#     file.write('[')
found_id = False
for player in get_ids.define_player.players:

    if start_id[0] == "0":

        found_id = True
    elif start_id[0] == str(player.id):
        found_id = True
    if found_id:
        number = number + 1
        try:
            params = (
                ('LeagueID', '00'),
                ('PerMode', 'PerGame'),
                ('PlayerID', player.id)
            )
            id_param = (
                ('PlayerID', player.id),
                ('h', "h")
            )
            advanced_params = (
                ('DateFrom', ''),
                ('DateTo', ''),
                ('GameSegment', ''),
                ('LastNGames', '0'),
                ('LeagueID', '00'),
                ('Location', ''),
                ('MeasureType', 'Advanced'),
                ('Month', '0'),
                ('OpponentTeamID', '0'),
                ('Outcome', ''),
                ('PORound', '0'),
                ('PaceAdjust', 'N'),
                ('PerMode', 'PerGame'),
                ('PlayerID', player.id),
                ('PlusMinus', 'N'),
                ('Period', '0'),
                ('Rank', 'N'),
                ('Season', '2017-18'),
                ('SeasonSegment', ''),
                ('SeasonType', 'Regular Season'),
                ('ShotClockRange', ''),
                ('Split', 'yoy'),
                ('VsConference', ''),
                ('VsDivision', '')
            )

            session = FuturesSession()
            height_weight_pos_response = session.get("http://stats.nba.com/stats/commonplayerinfo", headers=headers, params=id_param)
            response = session.get("http://stats.nba.com/stats/playerprofilev2", headers=headers, params=params)
            advanced_response = session.get("http://stats.nba.com/stats/playerdashboardbyyearoveryear", headers=headers, params=advanced_params)
            common_html = height_weight_pos_response.result().content
            common_data = json.loads(common_html)
            player.height = common_data["resultSets"][0]["rowSet"][0][10]
            player.weight = common_data["resultSets"][0]["rowSet"][0][11]
            player.position = common_data["resultSets"][0]["rowSet"][0][14]

            html = response.result().content
            data = json.loads(html)
            i = data["resultSets"][0]
            for c in i["rowSet"]:
                season = get_ids.define_player.OffensiveSeason(player.id, c[1], c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10],
                c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[18], c[19],
                c[20], c[21], c[22], c[23], c[24], c[25], c[26])
                player.offensive_seasons.append(season)
            html_advanced = advanced_response.result().content
            data_advanced = json.loads(html_advanced)
            i_advanced = data_advanced["resultSets"][1]
            for c in i_advanced["rowSet"]:
                season = get_ids.define_player.DefensiveSeason(player.id, c[2], c[3],
                0, c[5], 0, c[9], c[6], c[7], c[8], c[10], c[11], c[12], c[13], c[14],
                c[15], c[16], c[17], c[19], c[21], c[22], c[23], c[24])
                player.defensive_seasons.append(season)
            if get_ids.define_player.players.index(player) != len(get_ids.define_player.players)-1:
                print get_ids.define_player.players[get_ids.define_player.players.index(player)+1].id, player.name, player.height, player.weight, player.position, str((float(number)/float(len(get_ids.define_player.players)))*100)+"%"
            else:
                print "Its ZUBAC"
            with open(file_name[0], 'a') as file:
                file.write(json.dumps(player, default=lambda o: o.__dict__))
                if get_ids.define_player.players.index(player) != len(get_ids.define_player.players)-1:
                    file.write(',\n')
                else:
                    file.write(']')
            time.sleep(0.2)

        except KeyError:
            print("Whoops, weird guy just appeared "+player.name)
    # file.write(player.toJSON())v
