# this file will get player offensive statistics
import get_ids
import json
import time
import datetime

from requests_futures.sessions import FuturesSession

headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

number = 0
with open('data.json', 'a') as file:
    file.write('[')
for player in get_ids.define_player.players:
    number = number + 1
    try:
        params = (
            ('LeagueID', '00'),
            ('PerMode', 'PerGame'),
            ('PlayerID', player.id)
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
        response = session.get("http://stats.nba.com/stats/playerprofilev2", headers=headers, params=params)
        advanced_response = session.get("http://stats.nba.com/stats/playerdashboardbyyearoveryear", headers=headers, params=advanced_params)
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
        print player.name, str((float(number)/float(len(get_ids.define_player.players)))*100)+"%"
        with open('data.json', 'a') as file:
            file.write(json.dumps(player, default=lambda o: o.__dict__))
            if get_ids.define_player.players.index(player) != len(get_ids.define_player.players)-1:
                file.write(',')
            else:
                file.write(']')
        time.sleep(0.2)

    except KeyError:
        print("Whoops, weird guy just appeared "+player.name)
    # file.write(player.toJSON())
