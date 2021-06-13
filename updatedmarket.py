import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.wellsfargoadvisors.com/research-analysis/commentary/stock-market-news.htm')
soup = BeautifulSoup(response.content, 'html.parser')
article = soup.find_all('p', class_='article__p')
subjects = soup.find_all('h3')

opening_date = subjects[4].text.split(' — ')[-1] + ' - Opening Comment'
opening_markets = [i.split(': ')[-1] for i in article[8].text.split('\n')]
opening_dji = opening_markets[0]
opening_inx = opening_markets[2]
opening_ixic = opening_markets[4]

opening_subject = subjects[5].text
opening_p1 = article[9].text
opening_p2 = article[10].text
opening_p3 = article[11].text

midday_date = subjects[2].text.split(' — ')[-1] + ' - Midday Comment'
midday_markets = [i.split(': ')[-1] for i in article[4].text.split('\n')]
midday_dji = midday_markets[0]
midday_inx = midday_markets[2]
midday_ixic = midday_markets[4]

midday_subject = subjects[3].text
midday_p1 = article[5].text
midday_p2 = article[6].text
midday_p3 = article[7].text

closing_date = subjects[0].text.split(' — ')[-1] + ' - Closing Comment'
closing_markets = [i.split(': ')[-1] for i in article[0].text.split('\n')]
closing_dji = closing_markets[0]
closing_inx = closing_markets[2]
closing_ixic = closing_markets[4]

closing_subject = subjects[1].text
closing_p1 = article[1].text
closing_p2 = article[2].text
closing_p3 = article[3].text

columns = ['Time', 'DJIA', 'S&P 500', 'Nasdaq', 'Subject', 'Comment']
opening = {'DJIA' : opening_dji, 'S&P 500' : opening_inx, 'Nasdaq' : opening_ixic, 'Subject' : opening_subject, 'Comment' : opening_p1 + '\n' + opening_p2 + '\n' + opening_p3}
midday = {'DJIA' : midday_dji, 'S&P 500' : midday_inx, 'Nasdaq' : midday_ixic, 'Subject' : midday_subject, 'Comment' : midday_p1 + '\n' + midday_p2 + '\n' + midday_p3}
closing = {'DJIA' : closing_dji, 'S&P 500' : closing_inx, 'Nasdaq' : closing_ixic, 'Subject' : closing_subject, 'Comment' : closing_p1 + '\n' + closing_p2 + '\n' + closing_p3}
df = pd.DataFrame([opening, midday, closing], index=[opening_date, midday_date, closing_date])

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

df.to_csv('market.csv')
