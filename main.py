import requests
import scraper.scrapecar as scrapecar
import scraper.scrapelist as scrapelist
import urls

for url in urls.URLs.url_list:
    page = requests.get(url)
    if page.status_code == 200:
        scrapelist.scraper(page)
