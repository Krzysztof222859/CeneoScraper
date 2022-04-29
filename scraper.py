import requests
from bs4 import BeautifulSoup
import json

url = "https://www.ceneo.pl/91714422#tab=reviews"
response = requests.get(url)

page = BeautifulSoup(response.text, 'html.parser')

opinions = page.select("div.js_product-review")
all_opinions=[]
#print(type(opinions))
#print(len(opinions))

for opinions in opinions:
    opinion=opinions.pop(0)
    opinion_id = opinion["data-entry-id"]
    #author = opinion.select("span.user-post__author-name").pop(0)
    author = opinion.select_one("span.user-post__author-name").get_text().strip()
    try:
        recommendation = opinion.selet_one("span.user-post__author-recomendation > em").get_text().strip()
    except AttributeError:
        recommendation = None
    
    stars = opinion.select_one("span.user-post__score-count").get_text().strip()
    content = opinion.select_one("div.user-post__text").get_text().strip()
    useful = content = opinion.select_one("button.vote-yes").get_text().strip()
    useless = content = opinion.select_one("button.vote-no").get_text().strip()
    publish_date = content = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]

    try:
        pourchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
    except: TypeError:
    purchase_date=None

    pros = opinion.select("div[class$=\"positives\"]~ div.review-feature_item")
    pros = [item.get_text().strip() for item in pros]
    cons = opinion.select("div[class$=\"negatives\"]~ div.review-feature_item")
    cons = [item.get_text().strip() for item in cons]

    single_opinion = {
        "opinion_id": opinions,
        "author":author,
        "recommendation":recommendation,
        "stars":stars,
        "content":content,
        "useful":useful,
        "useless":useless,
        "publish_date":publish_date,
        "purchase_date":purchase_date,
        "pros":pros,
        "cons":cons
    }
    all_opinions.append(single_opinion)


with open("opinions/91714422.json", "w", encoding="UTF-8") as jf:
    print(json.dumps(all_opinions, jf,  indent=4, ensure_ascii=False))



