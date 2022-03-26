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

job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# authors = meta.find_all(property = "author")
# print(authors)