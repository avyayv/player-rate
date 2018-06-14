import json
import define_player
import requests
import pdb
from bs4 import BeautifulSoup
from lxml import html

ids = []
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
data = json.loads(html)

for i in data["resultSets"]:
    for c in i["rowSet"]:
        if c[-1] == "Y":
            if int(c[4]) > 1950:
                player = define_player.Player(c[0], c[2], c[6])
                ids.append(c[0])
headers = {'Accept-Encoding': 'identity'}


htmldata = requests.get("https://www.basketball-reference.com/contracts/players.html", headers=headers).text
soup = BeautifulSoup(htmldata, "html.parser")
for counter,i in enumerate(soup.tbody.find_all('tr')):
    try:
        player = define_player.PlayerContract()
        years_and_info = i.find_all('td')
        player.name = years_and_info[0].a.text
        player.team = years_and_info[1].a.text
        player.change_team("BRK", "BKN")
        player.change_team("CHO", "CHA")
        player.change_team("PHO", "PHX")
        player.y1 = years_and_info[2].text
        if years_and_info[2]["class"][1] == "salary-tm":
            player.team_options.append("Year 1")
        if years_and_info[2]["class"][1] == "salary-pl":
            player.player_options.append("Year 1")
        if years_and_info[2]["class"][1] == "salary-et":
            player.player_options.append("Year 1")

        player.y2 = years_and_info[3].text
        if years_and_info[3]["class"][1] == "salary-tm":
            player.team_options.append("Year 2")
        if years_and_info[3]["class"][1] == "salary-pl":
            player.player_options.append("Year 2")
        if years_and_info[3]["class"][1] == "salary-et":
            player.player_options.append("Year 2")

        player.y3 = years_and_info[4].text
        if years_and_info[4]["class"][1] == "salary-tm":
            player.team_options.append("Year 3")
        if years_and_info[4]["class"][1] == "salary-pl":
            player.player_options.append("Year 3")
        if years_and_info[4]["class"][1] == "salary-et":
            player.player_options.append("Year 3")

        player.y4 = years_and_info[5].text
        if years_and_info[5]["class"][1] == "salary-tm":
            player.team_options.append("Year 4")
        if years_and_info[5]["class"][1] == "salary-pl":
            player.player_options.append("Year 4")
        if years_and_info[5]["class"][1] == "salary-et":
            player.player_options.append("Year 4")

        player.y5 = years_and_info[6].text
        if years_and_info[6]["class"][1] == "salary-tm":
            player.team_options.append("Year 5")
        if years_and_info[6]["class"][1] == "salary-pl":
            player.player_options.append("Year 5")
        if years_and_info[6]["class"][1] == "salary-et":
            player.player_options.append("Year 5")

        player.y6 = years_and_info[7].text
        if years_and_info[7]["class"][1] == "salary-tm":
            player.team_options.append("Year 6")
        if years_and_info[7]["class"][1] == "salary-pl":
            player.player_options.append("Year 6")
        if years_and_info[7]["class"][1] == "salary-et":
            player.player_options.append("Year 6")

        player.signed_using = years_and_info[8].text
        try:
<<<<<<< HEAD
=======
            print(define_player.findByName(player.name))
>>>>>>> 56beb951a7ff7bb02e1d3f2039a8be5a9324235a
            define_player.findByName(player.name).salary = player
        except AttributeError:
            continue
    except (IndexError, KeyError):
        continue
