from bs4 import BeautifulSoup

def scraper(html_content):
    soup = BeautifulSoup(html_content.content, "html.parser")
    
    scrapeprice(soup)


def scrapeprice(soup):
    parentscript = soup.find("script", {"type": "application/ld+json"})
    print(parentscript)


def scrapedescription(soup):
    parentnode = soup.find_all("div", {"class": "leiras"})
    for one in parentnode:
        description = one.find("div", {"data-hj-suppress": ""})
        if (description is not None):
            return description.contents[0]
