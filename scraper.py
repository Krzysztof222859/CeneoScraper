import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
#print(type(opinions))
#print(len(opinions))
opinion=opinions.pop(0)
opinion_id = opinion["data-entry-id"]
#author = opinion.select("span.user-post__author-name").pop(0)
author = opinion.select_one("span.user-post__author-name").get_text().strip()
recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
stars = opinion.select_one("span.user-post__score-count").get_text().strip()
content = opinion.select_one("div.user-post__text").get_text().strip()
useful = content = opinion.select_one("button.vote-yes").get_text().strip()
useless = content = opinion.select_one("button.vote-no").get_text().strip()
publish_date = content = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
purchase_date = content = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]

print(recommendation, stars, content, useful, useless, publish_date, purchase_date, sep="\n")



