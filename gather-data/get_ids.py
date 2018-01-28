import urllib2
import json
import define_player
import requests
import pdb
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

params = (
    ('LeagueID', '00'),
    ('Season', '2016-17'),
    ('IsOnlyCurrentSeason', '0'),
)

response = requests.get('http://stats.nba.com/stats/commonallplayers', headers=headers, params=params)


html = response.text
data = json.loads(html.decode())

for i in data["resultSets"]:
    for c in i["rowSet"]:
        if c[-1] == "Y":
            player = define_player.Player(c[0], c[2], c[6])
