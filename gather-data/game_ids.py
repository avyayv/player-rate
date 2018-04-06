# this file will get team offensive data
from datetime import date, timedelta
from requests_futures.sessions import FuturesSession
import json
games_id = []
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}
dates = []
use_these_dates = []
d1 = date(2000, 1, 1)
d2 = date(2018, 4, 2)
delta = d2 - d1

for i in range(delta.days + 1):
    dates.append(d1 + timedelta(days=i))
for i in dates:
    use_these_dates.append(str(i.month)+"/"+str(i.day)+"/"+str(i.year))
with open('gameids.json', 'a') as file:
    file.write('[')
for date in use_these_dates:
    params = (
        ('GameDate', date),
        ('LeagueID', '00'),
        ('DayOffset', '0')
    )
    session = FuturesSession()
    response = session.get("http://stats.nba.com/stats/scoreboard", headers=headers, params=params)
    html = response.result().content
    data = json.loads(html)
    resultSets = data["resultSets"][0]
    
    for i in resultSets["rowSet"]:
        with open('gameids.json', 'a') as file:
            file.write(i[2])
            file.write(",\n")
            print(i[2])
with open('gameids.json', 'a') as file:
    file.write(']')
