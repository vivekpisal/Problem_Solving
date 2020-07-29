from bs4 import BeautifulSoup
import requests

a=requests.get('https://timesofindia.indiatimes.com/india/coronavirus-in-india-live-news-updates-covid-19-cases-in-india-and-world/liveblog/74880442.cms').text

soup=BeautifulSoup(a,'lxml')
for i in soup.find_all('div',class_='_1KydD'):
    print(i.text)
    print()
    print()

