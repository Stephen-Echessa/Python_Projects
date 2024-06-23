import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text

movies_list = []
soup = BeautifulSoup(contents, "html.parser")
movies_titles = soup.find_all(class_="jsx-952983560 loading")
for movie in movies_titles:
    movie = movie.get("alt")
    movies_list.append(movie)

print(movies_list)

with open("movies.txt", "w") as file:
    for i in range(1,101):
        file.write(f"{i}) {movies_list[-i]}\n")




