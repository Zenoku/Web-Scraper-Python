from urllib.request import urlopen
from bs4 import BeautifulSoup

# request a url
url = input("Insert URL:")
page = urlopen(url)

# extract and decode the html
html = page.read().decode("utf-8")

# create soup object (the actual webpage w/o the html)
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())