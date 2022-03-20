import requests
from bs4 import BeautifulSoup

# request a url
url = input("Insert URL:")

try:
    page = requests.get(url)
except:
    print("Not a valid url")
    exit()

# create soup object 
soup = BeautifulSoup(page.text, "html.parser")

# stuff to get
title = soup.title.string
print(title)

authors = soup.find("meta", property = "author")
print(authors)