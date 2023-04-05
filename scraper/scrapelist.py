from bs4 import BeautifulSoup
import datetime as dt
import scraper.scrapecar as scrapecar
import requests

def scraper(soup, sw, counter):

    advertisementlinks = soup.find_all("h3")
    i = 0

    for onead in advertisementlinks:
        one = onead.find("a")
        if one is not None:
            carhref = one.attrs.get("href").split("#")[0]
            print(f"Processing {counter * 100 + i + 1}. car ...", end="\r")
            scrapecar.scraper(requests.get(carhref), sw)
            i += 1


def scrapermain(html_content):

    nextrun = True
    counter = 0
    sw = open(f"scraped_{dt.datetime.today().strftime('%Y-%m-%d')}.txt", "w", encoding="utf-8")

    while nextrun:
        soup = BeautifulSoup(html_content.content, "html.parser")
        scraper(soup, sw, counter)

        # If href "next" is active then go to the next page and call scraper again until href "next" is not active
        if soup.find("link", {"rel": "next"}) == None:
            nextrun = False
        else:
            # Load the next page
            html_content = requests.get(soup.find("link", {"rel": "next"}).attrs.get("href"))
            counter += 1
    
    sw.close()
