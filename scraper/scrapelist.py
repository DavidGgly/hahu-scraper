from bs4 import BeautifulSoup
import scraper.scrapecar as scrapecar
import requests

def scraper(html_content):
    soup = BeautifulSoup(html_content.content, "html.parser")
    advertisementlinks = soup.find_all("h3")

    for i, onead in enumerate(advertisementlinks):
        one = onead.find("a")
        if one is not None:
            carhref = one.attrs.get("href").split("#")[0]
            # print(f"{(i+1)}. car: {carhref}")
            scrapecar.scraper(getcarhtml(carhref))

def getcarhtml(carhref):
    return requests.get(carhref)

