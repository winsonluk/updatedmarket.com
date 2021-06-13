import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wellsfargoadvisors.com/research-analysis/commentary/stock-market-news.htm')
soup = BeautifulSoup(response.content, 'html.parser')
article = soup.find_all('p', class_='article__p')
subjects = soup.find_all('h3')

opening_date = subjects[4].text
opening_markets = article[8].text.split('\n')
opening_dji = opening_markets[0]
opening_inx = opening_markets[2]
opening_ixic = opening_markets[4]

opening_subject = subjects[5].text
opening_p1 = article[9].text
opening_p2 = article[10].text
opening_p3 = article[11].text

midday_date = subjects[2].text
midday_markets = article[4].text.split('\n')
midday_dji = midday_markets[0]
midday_inx = midday_markets[2]
midday_ixic = midday_markets[4]

midday_subject = subjects[3].text
midday_p1 = article[5].text
midday_p2 = article[6].text
midday_p3 = article[7].text

closing_date = subjects[0].text
closing_markets = article[0].text.split('\n')
closing_dji = closing_markets[0]
closing_inx = closing_markets[2]
closing_ixic = closing_markets[4]

closing_subject = subjects[1].text
closing_p1 = article[1].text
closing_p2 = article[2].text
closing_p3 = article[3].text

print(opening_date)
print('---')
print(opening_dji)
print('---')
print(opening_inx)
print('---')
print(opening_ixic)
print('---')
print(opening_subject)
print('---')
print(opening_p1)
print('---')
print(opening_p2)
print('---')
print(opening_p3)
print('---')

print(midday_date)
print('---')
print(midday_dji)
print('---')
print(midday_inx)
print('---')
print(midday_ixic)
print('---')
print(midday_subject)
print('---')
print(midday_p1)
print('---')
print(midday_p2)
print('---')
print(midday_p3)
print('---')

print(closing_date)
print('---')
print(closing_dji)
print('---')
print(closing_inx)
print('---')
print(closing_ixic)
print('---')
print(closing_subject)
print('---')
print(closing_p1)
print('---')
print(closing_p2)
print('---')
print(closing_p3)

pd.read_csv('market.csv')
