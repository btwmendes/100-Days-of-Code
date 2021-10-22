from bs4 import BeautifulSoup


with open("website.html") as file:
    contents = file.read()

# print(contents)

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)
# print(soup.a)

print()

for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

print()

heading = soup.find(name="h1", id="name")
print(heading.text)

print()

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.text)

print()

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))