from urllib.request import urlopen

# request a url
url = input("Insert URL:")
page = urlopen(url)

# extract and decode the html
html_bytes = page.read()
html = html_bytes.decode("utf-8")

# print html
print(html)