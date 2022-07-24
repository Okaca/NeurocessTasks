#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from selenium import webdriver
from bs4 import BeautifulSoup
import unicodedata



app = Flask(__name__)

def scrape():
    """
    In the web scraping part, we expect you to take name and price data of listed products.
    """

    scrape_url = 'https://www.amazon.com.tr/s?k=apple&rh=n%3A12466496031%2Cn%3A26232650031&dc&ds=' \
                 'v1%3A24QIKEr1whZX7fY03aG1Rzroi24YQzoigI1WMNytis0&__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid' \
                 '=9UPC9JZMBEZY&qid=1658327018&rnid=13818411031&sprefix=appl%2Caps%2C122&ref=sr_nr_n_4'
    # I have chrome version of 103, hence I downloaded respective chromedriver
    # chrome updates recently and is up to version 104, hence check before using the same chromedriver
    # chromedriver can be accessed here 'https://chromedriver.chromium.org/downloads'
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(scrape_url)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    product_html = soup.find_all('div', class_='a-section a-spacing-base')

    out_json = {}
    product_number = 1

    for i in product_html:
        product = 'product#{}'.format(product_number)
        product_number += 1
        name_content = i.find('span', class_='a-size-base-plus a-color-base a-text-normal')
        name = name_content.getText(strip=True)
        name = unicodedata.normalize("NFKD", name)

        price_content = i.find('span', class_='a-price')
        try:
            price = price_content.span.getText(strip=True)
            price = unicodedata.normalize("NFKD", price)
        except AttributeError:
            price = 'Not given'
        print(name,price)
        out_json[product] = {'name': name,
                             'price': price}

    browser.close()
    return out_json


# The route() function of the Flask class is a decorator,
@app.route('/', methods=['GET'])
def getData():
    if request.method == 'GET':
        return scrape()


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

