from bs4 import BeautifulSoup

import requests

url = input("Enter a website to extract the emails from: ")

data = requests.get("https://" + url)


soup = BeautifulSoup(data.text, "html.parser")

file = open("../data/emails.txt", "w")

for email in soup.select('a[href^=mailto]'):
    emailString = email.get('href')
    strippedEmail = emailString.replace("mailto:", "")
    file.write(strippedEmail + "\n")

    print(strippedEmail)


file.close()
