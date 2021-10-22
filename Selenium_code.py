import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from db import connect_mongo

def depth_scraping(url_link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url_link)
    links = driver.find_elements_by_css_selector("a")
    return links

def Url_link_checker(url_link,url_dict={},depth=1):
    # Access collection of the database     
    collection= connect_mongo.connect_db()
    options = webdriver.ChromeOptions() 
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    links = depth_scraping(url_link)
    for link in links:
        if(link!=None):
            try:                    
                r = requests.head(link.get_attribute('href'))
                ##Insert each record at a time to the database
                collection.insert_one({"Domain_Name":url_link,"URL":link.get_attribute('href'),"status_code":r.status_code,"Response_time":r.elapsed.total_seconds()})

                url_dict[link.get_attribute('href')] = [{"Domain_Name":url_link,"URL":link.get_attribute('href'),"status_code":r.status_code,"Response_time":r.elapsed.total_seconds()}]
 
            except Exception:
                pass            

    return url_dict
