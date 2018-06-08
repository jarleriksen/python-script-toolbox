from bs4 import BeautifulSoup

import requests

#url = input("Enter a website to extract the URL's from: ")

r  = requests.get("http://civitas-software.com/")

data = r.text

soup = BeautifulSoup(data, "html.parser")

for link in soup.select('a[href^=mailto]'):
    print(link.get('href'))