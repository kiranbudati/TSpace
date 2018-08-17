from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = "http://www.isstracker.com"
browser = webdriver.Chrome("D:\Goals\Projects\ISS\chromedriver.exe")
browser.get(url)
while True:
    time.sleep(1.5)
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")
    longitude_field = soup.find('p',attrs={'id':'longitudeValue'})
    latitude_field = soup.find('p',attrs={'id':'latitudeValue'})
    khm_field = soup.find('p',attrs={'id':'velocityValue'})

    latitude = latitude_field.text.strip()
    longitude = longitude_field.text.strip()
    khm = khm_field.text.strip()

    print("latitude : "+ latitude+" longitude: "+longitude+" khm: "+khm)
# browser.close()
# browser.quit()