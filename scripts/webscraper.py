from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the URL's from: ")

r = requests.get("https://" + url)

data = r.text

soup = BeautifulSoup(data, "html.parser")

for email in soup.select('a[href^=mailto]'):
    emailString = email.get('href')

    print(emailString.replace("mailto:", ""))



