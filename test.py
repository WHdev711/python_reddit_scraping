import schedule
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
 
def check_stock():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    browser = webdriver.Chrome(options=options)
    #--| Parse or automation
    browser.get('https://www.morningstar.com/stocks/XOSL/XXL/quote.html')
    time.sleep(1)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    bid_size = soup.select('div.dp-value.price-down.ng-binding.ng-scope')
    price_sales = soup.select('li:nth-child(9) > div > div.dp-value.ng-binding')
    print(price_sales[0].text.strip())
 
def check_size():
    options = Options()
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--log-level=3')
    browser = webdriver.Chrome(options=options)
    #--| Parse or automation
    browser.get('https://www.morningstar.com/stocks/XOSL/XXL/quote.html')
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    bid_size = soup.select('div.dp-value.price-down.ng-binding.ng-scope')
    price_sales = soup.select('li:nth-child(9) > div > div.dp-value.ng-binding')
    print(bid_size[0].text.strip())
 
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
 
schedule.every(60).seconds.do(run_threaded, check_stock)
schedule.every(20).seconds.do(run_threaded, check_size)
while True:
    schedule.run_pending()
    time.sleep(1)