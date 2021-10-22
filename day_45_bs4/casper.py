import requests
from bs4 import BeautifulSoup
from pprint import pprint

response = requests.get('https://casper.com/mattresses/casper-wave/v1/?size=california-king')

casper_info = response.text

soup = BeautifulSoup(casper_info, "html.parser")

upvote_tag = soup.find(name="span", class_="affirm-price")
print(upvote_tag)

# print(soup.prettify())

# price = soup.find_all(name="body", class_="affirm-price-container")
# print(price)

# pricy = soup.select(selector="span")
# print(pricy)

# print(soup.title.string)
# print()

# print(soup.div)

# divs = soup.find_all("div")
# for div in divs:
#     pprint(div.getText())


# body = soup.body
# print(body)
#
# heading = soup.find(name="h1", id="name")
# print(heading.text)

# lists = soup.find_all(name="li")
# pprint(lists)

find_by_class = soup.find(class_="zylhtj-30 hqWPES")
print(find_by_class.prettify())

# spans = soup.find_all('span', {'class' : 'affirm-price'})
# print(spans)