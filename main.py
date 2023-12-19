# Always check <root_url>/robots.txt and respect what is permitted in scraping a site.
# Example: https://news.ycombinator.com/robots.txt

# BeautifulSoup documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
response.raise_for_status()
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")

# List comprehensions work for these, but I'm parsing through the soup object twice for the same element.
# article_texts = [article.a.get_text() for article in soup.find_all(class_="titleline")]
# article_links = [article.a.get("href") for article in soup.find_all(class_="titleline")]

# Instead parse through the soup object once and append to both lists.
article_texts = []
article_links = []

for article in soup.find_all(class_="titleline"):
    article_texts.append(article.a.get_text())
    article_links.append(article.a.get("href"))

article_score = [int(article.getText().split(" ")[0]) for article in soup.find_all(class_="score")]

# print(article_texts)
# print(article_links)
# print(article_score)

max_score = max(article_score)
article_position = article_score.index(max_score)

print(article_texts[article_position])
print(article_links[article_position])

# Alternate approach I came up with. Get all elements needed in 1 parse.
# This approach works just as well, but it's not as clear/readable.
# elements = soup.find_all(class_=["titleline", "score"])
# print(elements)
#
# for i in range(len(elements)):
#     if i == 0 or i % 2 == 0:
#         print(elements[i].a.get_text())
#         print(elements[i].a.get("href"))
#     else:
#         print(elements[i].get_text())  # get the score for each article
