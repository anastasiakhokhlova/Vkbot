from tqdm import tqdm
import requests as r
from bs4 import BeautifulSoup as bs
import sqlite3

headers=headers = {"accept":"*/*" ,"user-agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
base_url='https://coinmarketcap.com/all/views/all'

session=r.Session()
request=session.get(base_url, headers=headers)
if request.status_code==200:
    print ("it's ok")

    soup=bs(request.content, 'html.parser')
    divs=soup.find_all('td', attrs={'class':'no-wrap text-right'})
    print(len(divs))
    for div in divs:
        name=div.find('a', attrs={'class':"currency-name-container link-secondary"})[href='']
        #price=div.find('a', attrs={'price'})

        print(name)
        #print(price)
        break

else:
    print('error')
