import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
# print(response.text)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

movie_info = soup.find_all(name="img", class_="jsx-952983560 loading")
movies = []
for name in movie_info:
    movies.append(name.get("alt"))
# print(movies)
movies_list = list(filter(None, movies))
# print(movies_list)
movies_reversed = movies_list[::-1]
# print(movies_reversed)

hundred_list = [num for num in range(1,101)]
# print(hundred_list)

formatted_nums = []
for num in hundred_list:
    formatted_nums.append(str(num) + ") ")
# print(formatted_nums)

final_list = [ a + b for (a,b) in zip(formatted_nums, movies_reversed)]
print(final_list)

with open('top_100_movies.txt', mode='w') as file:
    for movie in final_list:
        file.write(f"{movie}\n")