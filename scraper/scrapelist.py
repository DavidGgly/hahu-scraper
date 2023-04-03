from bs4 import BeautifulSoup
import scraper.scrapecar as scrapecar
import requests

def scraper(soup):

    advertisementlinks = soup.find_all("h3")

    for i, onead in enumerate(advertisementlinks):
        one = onead.find("a")
        if one is not None:
            carhref = one.attrs.get("href").split("#")[0]
            # print(f"{(i+1)}. car: {carhref}")
            scrapecar.scraper(getcarhtml(carhref))

def getcarhtml(carhref):
    return requests.get(carhref)

def scrapermain(html_content):

    nextrun = True
    while nextrun:
        soup = BeautifulSoup(html_content.content, "html.parser")
        scraper(soup)
        
        # TODO: scraper(soup) iterates through the whole page so if next link exists then first go to the next page and call scraper just afterwards

        # If href "next" is active then go to the next page and call scraper again until href "next" is not active
        if soup.find("link", {"rel": "next"}) == None:
            nextrun = False
        else:
            # goto the next page - row below has been created by copilot, not tested yet
            html_content = requests.get(soup.find("link", {"rel": "next"}).attrs.get("href"))

