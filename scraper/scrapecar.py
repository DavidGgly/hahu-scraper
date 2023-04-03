from bs4 import BeautifulSoup
import datetime as dt
import json

def scraper(html_content, sw):
    soup = BeautifulSoup(html_content.content, "html.parser")

    titleprice = scrapetitleprice(soup)
    output = {
        "scrapeDate": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "title": titleprice[0],
        "price": titleprice[1],
        "description": scrapedescription(soup) 
    }

    sw.write(json.dumps(output, indent=4, ensure_ascii=False))


def scrapetitleprice(soup):
    parentscript = soup.find("script", {"type": "application/ld+json"})
    if parentscript is not None:
        parentjson = json.loads(parentscript.contents[0])
        return parentjson["description"], parentjson["offers"]["price"]


def scrapedescription(soup):
    parentnode = soup.find_all("div", {"class": "leiras"})
    for one in parentnode:
        description = one.find("div", {"data-hj-suppress": ""})
        if (description is not None):
            return description.contents[0]
