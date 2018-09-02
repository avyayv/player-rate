# this file will get college data
# will be completed in future
from bs4 import BeautifulSoup
import requests
import pdb
import define_player
import json
headers = {'Accept-Encoding': 'identity'}
htmldata = requests.get("https://basketball.realgm.com/nba/draft/prospects/stats", headers=headers).text
soup = BeautifulSoup(htmldata, "html.parser")
seasons = []
for player_html in soup.tbody.find_all('tr'):
    try:
        tdtags = player_html.find_all('td')
        tags = []
        for tag in tdtags:
            tags.append(tag)
        url = tags[0].find('a')['href']
        newdata = requests.get("https://basketball.realgm.com"+url, headers=headers).text
        indsoup = BeautifulSoup(newdata, "html.parser")
        playerdata = indsoup.find("div", class_="half-column-right")
        paras = playerdata.find_all('p')
        ar = []
        for a in indsoup.tbody.find_all('tr')[-1].find_all('td'):
            ar.append(a.text)
        miscstats = indsoup.find_all('tr', class_="per_game")[-4]
        advancedstats = indsoup.find_all('tr', class_="per_game")[-2]
        ar.extend((miscstats.find_all('td')[-3].text, miscstats.find_all('td')[-4].text, miscstats.find_all('td')[-5].text))
        ar.extend((advancedstats.find_all('td')[-1].text, advancedstats.find_all('td')[-3].text, advancedstats.find_all('td')[-2].text, advancedstats.find_all('td')[-7].text))
        for p in paras:
            if p.text[:15] == "Pre-Draft Team:":
                if ("(Fr)" not in p.text[16:] and "(So)" not in p.text[16:] and "(Jr)" not in p.text[16:] and "(Sr)" not in p.text[16:]):
                    print("International "+tags[0].text)
                    continue
                else:
                    season = define_player.CollegeSeason(tags[0].text, ar[0], ar[1], ar[2], ar[3], ar[4], ar[5], ar[6], ar[7], ar[8],
                    ar[9], ar[10], ar[11], ar[12], ar[13], ar[14], ar[15], ar[16], ar[17], ar[18], ar[19], ar[20], ar[21], ar[22], ar[23],
                    ar[24], ar[25], ar[26], ar[27], ar[28], ar[29], ar[30])
                    seasons.append(season)

                    with open("college_data.json", 'a') as file:
                        file.write(json.dumps(season, default=lambda o: o.__dict__))
                        file.write(",")
                    print(season.name, season.classo, season.pts, season.offensive_rating)
    except(IndexError):
        continue
