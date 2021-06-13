from flask import Flask, make_response, render_template_string
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

columns = ['Time', 'DJIA', 'S&P 500', 'Nasdaq', 'Subject', 'Paragraph 1', 'Paragraph 2', 'Paragraph 3']
opening = {'DJIA' : opening_dji, 'S&P 500' : opening_inx, 'Nasdaq' : opening_ixic, 'Subject' : opening_subject, 'Paragraph 1' : opening_p1, 'Paragraph 2' : opening_p2, 'Paragraph 3' : opening_p3}
midday = {'DJIA' : midday_dji, 'S&P 500' : midday_inx, 'Nasdaq' : midday_ixic, 'Subject' : midday_subject, 'Paragraph 1' : midday_p1, 'Paragraph 2' : midday_p2, 'Paragraph 3' : midday_p3}
closing = {'DJIA' : closing_dji, 'S&P 500' : closing_inx, 'Nasdaq' : closing_ixic, 'Subject' : closing_subject, 'Paragraph 1' : closing_p1, 'Paragraph 2' : closing_p2, 'Paragraph 3' : closing_p3}
df = pd.DataFrame([opening, midday, closing], index=[opening_date, midday_date, closing_date])
df.to_csv('market.csv')

application = Flask(__name__)

@application.route('/')
def home():
    return make_response(render_template_string(df.to_html()))

if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
