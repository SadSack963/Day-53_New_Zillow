"""
Program to scrape the Zillow website for links and prices
Date: 08/01/2023
Author: SadSack963
"""

URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

FILE = 'data/raw_html.html'  # Create a "data" directory in the project tree

# http://myhttpheader.com/
ACCEPT = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"

# User-Agent HTTP Headers
#   https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
USER_AGENT = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
    "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.60 (Windows NT 6.0; U; en) Presto/2.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
]


def get_webpage(url: str = URL, file: str = FILE, test: bool = False) -> str:
    """
    Function to get the HTML of a webpage.
    If an HTML file exists and test is True then the HTML is loaded from file,
    otherwise the HTML is downloaded from the URL.

    :param url: webpage URL - defaults to constant URL
    :type url: string
    :param file: path to HTML file - defaults to constant FILE
    :type file: string
    :param test: if True, load webpage from file if available
    :type test: boolean
    :return: HTML of the webpage
    :rtype: string
    """
    import os

    if os.path.exists(file) and test:
        print(
            "Loading Webpage From File"
            "========================="
        )
        with open(file, mode='r', encoding='utf-8') as fp:
            html = fp.read()
    else:
        print(
            "Retrieving Webpage from URL"
            "==========================="
        )
        html = download_webpage(url=url, file=file)
    return html


def download_webpage(url: str = URL, file: str = FILE) -> str:
    """
    Function to download the raw (unrendered) HTML code from a webpage.
    The HTML is saved in a file of your choice for future use, e.g. during code testing.
    To download a fresh copy of the web page, simply delete the existing file.

    :param url: webpage URL - defaults to constant URL
    :type url: string
    :param file: path to HTML file - defaults to constant FILE
    :type file: string
    :return: HTML downloaded from webpage
    :rtype: string
    """
    import requests
    import random

    # Send a User-Agent string to avoid CAPTCHA
    headers = {
        'Accept': ACCEPT,
        'User-Agent': random.choice(USER_AGENT),
    }
    print(headers)

    # Download the webpage
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()
    html = response.text
    with open(file, mode='w', encoding='utf-8') as fp:
        fp.write(html)
    return html


if __name__ == '__main__':
    raw_html = get_webpage(test=True)
