from bs4 import BeautifulSoup
import requests


def scraper():

    url = input("Enter a website to extract the emails from: ")
    data = requests.get("https://" + url)
    soup = BeautifulSoup(data.text, "html.parser")
    # Had to use absolute path when calling from another file
    file = open("../data/emails.txt", "w")

    for email in soup.select('a[href^=mailto]'):
        emailString = email.get('href')
        strippedEmail = emailString.replace("mailto:", "")
        file.write(strippedEmail + "\n")

        print(strippedEmail)

    file.close()