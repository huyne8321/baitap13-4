from bs4 import BeautifulSoup
import requests
url= requests.get("https://teky.edu.vn/blog/xml-la-gi/")
soup = BeautifulSoup(url.content,'lxml')
ss = soup.find_all(True , limit=1)
for a in ss:
    print(a.text)