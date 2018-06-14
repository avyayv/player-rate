# this file will get college data
# will be completed in future
from bs4 import BeautifulSoup
import requests
import pdb
headers = {'Accept-Encoding': 'identity'}
htmldata = requests.get("https://basketball.realgm.com/nba/draft/prospects/stats", headers=headers).text
soup = BeautifulSoup(htmldata, "html.parser")
for player_html in soup.tbody.find_all('tr'):
    tdtags = player_html.find_all('td')
    tags = []
    for tag in tdtags:
        tags.append(tag)
    url = tags[0].find('a')['href']
    newdata = requests.get("https://basketball.realgm.com"+url, headers=headers).text
    indsoup = BeautifulSoup(newdata, "html.parser")
    playerdata = indsoup.find_all("div", class_="half-column-right")
    for d in playerdata:
        paras = d.find_all('p')
        for p in paras:
            if p.text[:15] == "Pre-Draft Team:":
                if ("(Fr)" not in p.text[16:] and "(So)" not in p.text[16:] and "(Jr)" not in p.text[16:] and "(Sr)" not in p.text[16:]):
                    print("International "+tags[0].text)
                else:
                    print("Domestic "+tags[0].text)

    # print(tags)
