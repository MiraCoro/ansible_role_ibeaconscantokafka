import re
import requests
from bs4 import BeautifulSoup
html_page = 'https://kb.epam.com/display/EPMLSTR/iBeacon+scanners'
page = (requests.get(html_page)).text
soup = BeautifulSoup(page, 'html.parser')
table = soup.find('div', {"class": "table-wrap"})
#table = soup.find('table', {"class": "wrapped confluenceTable"})
print(table)
for row in table.find('tbody').find_all("tr", recursive=False):
    cols = row.find_all("td")
    name = cols[1].text.strip()
                      #{"class": "confluenceTd"}):
    #name = re.search ("blescan-*", row)
    print (name)
