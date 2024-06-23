from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
article_tag = soup.find_all(class_="titleline")
article_text = []
article_link = []
for article in article_tag:
    article_text.append(article.getText())
    link = article.find(name="a").get("href")
    article_link.append(link)

upvotes = soup.find_all(class_="score")
article_upvotes = [int(score.getText().split()[0]) for score in upvotes]

max_value = max(article_upvotes)
index = article_upvotes.index(max_value)
print(index)

print(article_text[index])
print(article_link[index])
print(article_upvotes)

# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h3", class_="heading")
# print(heading)
