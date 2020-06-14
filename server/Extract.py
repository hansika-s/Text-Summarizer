from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs


def extract(url):
    """
    Returns the paragraph text '<p>' of the HTML content
    scraped from the url passed in as a parameter

    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    htmlDoc = urlopen(req)
    soupObject = bs(htmlDoc, 'html.parser')
    title = soupObject.findAll('title')
    content = soupObject.findAll('p')
    res = {
        "title": title,
        "content": content
    }
    return res
