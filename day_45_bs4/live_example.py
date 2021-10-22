# -------------------Imports-------------------------
from bs4 import BeautifulSoup
import requests
from pprint import pprint

# -----------------------------------------------------------
''' I want the story titles and the links'''

response = requests.get("https://news.ycombinator.com")
yc_web_page = response.text

soup =BeautifulSoup(yc_web_page, "html.parser")

# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.get("title"))
#     # print(tag.get("href"))
#     print(tag)


# print(titles)

hacker_dict = {}

articles = soup.find_all(name="a", class_="titlelink")
article_text = []
article_links = []


for article in articles:
    text = article.getText()
    article_text.append(text)
    link = article.get("href")
    article_links.append(link)

    # print(title.text)
    # print(title.string)

article_upvotes = [int(vote.getText().split()[0]) for vote in soup.find_all(name="span", class_="score")]
# print(article_tag.getText())

print(article_text)
print(article_links)
print(article_upvotes)

# print(len(article_text))
# print(len(article_links))
# print(len(article_upvotes))

# for i in range(len(article_text)):
#     temp_dict = {}
#     temp_dict['title'] = article_text[i]
#     temp_dict['link'] = article_links[i]
#     temp_dict['score'] = article_upvotes[i]
#     hacker_dict[i] = temp_dict
#
# print(hacker_dict)

max_num = 0
most_upvotes_index = 0
for i, num in enumerate(article_upvotes):
    if num > max_num:
        most_upvotes_index = i
        max_num = num

print(max_num)
print(most_upvotes_index)

print(article_text[most_upvotes_index])