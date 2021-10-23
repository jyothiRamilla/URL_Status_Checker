import os
import requests
from selenium import webdriver
from db import connect_mongo
 
    
    
def depth_scraping(url_link,depth,driver,urllink_collection={}):
    try:
        driver.get(url_link)
        #for <a> tag use  driver.find_elements_by_css_selector("a")
        links = driver.find_elements_by_css_selector("link")
        urllink_collection[1]=links
    except Exception:
        pass
    if(depth>1):
        for val in range(1,depth):
            for link in urllink_collection[val]:
                try:
                    driver.get(link)
                    urllink_collection[val+1].append(driver.find_elements_by_css_selector("link"))
                except Exception:
                    pass
    
    final_links = {}
    for key,value in urllink_collection.items():
        if value not in final_links.values():
            final_links[key] = value
    return final_links

def Url_link_checker(url_link,depth=1,url_dict={}):
    # Access collection of the database     
    collection= connect_mongo.connect_db()
    CHROMEDRIVER_PATH = "/app/.chromedriver/bin/chromedriver"
    chrome_bin = os.environ.get('GOOGLE_CHROME_BIN', "chromedriver")
    options = webdriver.ChromeOptions()
    options.binary_location = chrome_bin
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=options)
    links = depth_scraping(url_link,depth,driver,urllink_collection={})
   
    for key,value in links.items():
        for link in value:
            if(link!=None):
                try:                    
                    r = requests.head(link.get_attribute('href'))
                    ##Insert each record at a time to the database
                    collection.insert_one({"Domain_Name":url_link,"URL":link.get_attribute('href'),"status_code":r.status_code,"Response_time":r.elapsed.total_seconds()})

                    url_dict[link.get_attribute('href')] = [{"Domain_Name":url_link,"URL":link.get_attribute('href'),"status_code":r.status_code,"Response_time":r.elapsed.total_seconds()}]
    
                except Exception:
                    pass            

    return url_dict

