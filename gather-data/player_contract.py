from bs4 import BeautifulSoup
from lxml import html
import requests
import json
import argparse

parser = argparse.ArgumentParser(description='What is the JSON file name?.')
parser.add_argument('jsonfile', metavar='N', type=str, nargs='+',
                    help='file name for JSON to go to')
args = parser.parse_args()
with open(args.jsonfile[0], 'a') as file:
    file.write('[\n')
headers = {'Accept-Encoding': 'identity'}
class PlayerContract:
    def __init__(self):
        self.name = ""
        self.team = ""
        self.y1 = 0
        self.y2 = 0
        self.y3 = 0
        self.y4 = 0
        self.y5 = 0
        self.y6 = 0
        self.player_options = []
        self.team_options = []
        self.early_termination = []
        self.signed_using = ""
    def change_team(self,start, end):
        if self.team == start:
            self.team = end
    def dumps(self):
      return "Name "+self.name+" Current Year "+self.y1

htmldata = requests.get("https://www.basketball-reference.com/contracts/players.html", headers=headers).text
soup = BeautifulSoup(htmldata, "html.parser")
for counter,i in enumerate(soup.tbody.find_all('tr')):
    try:
        player = PlayerContract()
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

        with open(args.jsonfile[0], 'a') as file:
            file.write(json.dumps(player, default=lambda o: o.__dict__))
            if counter != len(soup.tbody.find_all('tr'))-1:
                file.write(',\n')
        print(player.dumps())
    except (IndexError, KeyError):
        continue
with open(args.jsonfile[0], 'a') as file:
    file.write(']')
