import requests
from bs4 import BeautifulSoup

# request a url
url = input("Insert URL:")

try:
    page = requests.get(url)
except:
    print("Not a valid url")
    exit()

# create soup object + gets everything
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "ResultsContainer")
meta = soup.find_all(id = "meta")

# stuff to get
title = soup.title.string
print(title)