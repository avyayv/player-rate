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

with open('data.json', 'a') as file:
    number = 0
    for player in get_ids.define_player.players:
        number = number + 1
        try:
            time_start = datetime.datetime.now()
            params = (
                ('LeagueID', '00'),
                ('PerMode', 'PerGame'),
                ('PlayerID', player.id)
            )
            session = FuturesSession()
            response = session.get("http://stats.nba.com/stats/playerprofilev2", headers=headers, params=params)
            html = response.result().content
            data = json.loads(html)
            i = data["resultSets"][0]
            for c in i["rowSet"]:
                season = get_ids.define_player.Season(player.id, c[3], c[4], c[5], c[6], c[7], c[8], c[9], c[10],
                c[11], c[12], c[13], c[14], c[15], c[16], c[17], c[18], c[19],
                c[20], c[21], c[22], c[23], c[24], c[25], c[26])
                player.seasons.append(season)
            time_end = datetime.datetime.now()
            diff = time_end-time_start
            print player.name, str((float(number)/float(len(get_ids.define_player.players)))*100)+"%"
            time.sleep(0.2)
        except KeyError:
            print("Whoops, weird guy just appeared "+player.name)

        # file.write(player.toJSON())
