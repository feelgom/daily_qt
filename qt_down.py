import requests
from bs4 import BeautifulSoup
import urllib.request
import time
date = time.strftime('%m%d', time.localtime(time.time()))


req = requests.get('http://www.amazinggrace.or.kr/kor/sub04/menu_08_3.html')
html = req.text
soup = BeautifulSoup(html, 'html.parser')


my_titles = soup.select(
    'ul > li > div > p > img'
    )
today_url = my_titles[0].get('src')
url = "http://www.amazinggrace.or.kr/"+ today_url[6:]

print(url)
urllib.request.urlretrieve(url,"Today_QT.jpg")
