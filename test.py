from bs4 import BeautifulSoup
import time
from selenium import webdriver
# import pymongo
# from pymongo import MongoClient

# client = MongoClient('ec2-18-188-183-169.us-east-2.compute.amazonaws.com', 27017)

# db = client.tspace

url = "http://www.isstracker.com"
browser = webdriver.Chrome("D:\Goals\Projects\ISS\chromedriver.exe")
browser.get(url)
while True:
    time.sleep(1.5)
    # ts = time.time()
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    longitude_field = soup.find('p',attrs={'id':'longitudeValue'})
    latitude_field = soup.find('p',attrs={'id':'latitudeValue'})
    khm_field = soup.find('p',attrs={'id':'velocityValue'})

    latitude = latitude_field.text.strip()
    longitude = longitude_field.text.strip()
    khm = khm_field.text.strip()

    # db.iss.insert_one({"latitude":latitude,"longitude":longitude,"khm":khm})
    print("latitude : "+ latitude+" longitude: "+longitude+" khm: "+khm+" time: ",time.time())
# browser.close()
# browser.quit()