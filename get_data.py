# import urllib.request as urllb
# from bs4 import BeautifulSoup
# from selenium import webdriver

# while True:
#     isstracker_page = "http://www.isstracker.com/"

#     page = urllb.urlopen(isstracker_page)

#     soup = BeautifulSoup(page,'html.parser')

#     longitude_field = soup.find('p',attrs={'id':'longitudeValue'})
#     print(longitude_field)
# # longitude = longitude_field.text.strip()
# # print(longitude)    

# from bs4 import BeautifulSoup
# from selenium import webdriver

# browser = webdriver.PhantomJS()
# browser.get('http://www.isstracker.com/')

# soup = BeautifulSoup(browser.page_source, "html.parser")
# result = soup.find_all("p", {"id": "longitudeValue"})

# for item in result:
#     print(item.text)

# browser.quit()

# from ghost import Ghost
# ghost = Ghost()
# page, resources = ghost.open('http://www.isstracker.com/')
# result, resources = ghost.evaluate(
#     "document.getElementsById('longitudeValue');")
# print(result)

import requests
from bs4 import BeautifulSoup
import time
import urllib.request as urllb

def get_count():
    isstracker_page = "http://www.isstracker.com/"
    page = urllb.urlopen(isstracker_page)
    soup = BeautifulSoup(page,'html.parser')
    longitude_field = soup.find('p',attrs={'id':'longitudeValue'})
    longitude = longitude_field.text.strip()
    print(longitude)    

while True:
    get_count()