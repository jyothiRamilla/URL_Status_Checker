import os
import requests
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
from db import connect_mongo
 
    
    
def depth_scraping(url_link,depth,driver,urllink_collection={}):
    #if(depth==1):    
    try:
        driver.get(url_link)
        links = driver.find_elements_by_css_selector("link")
        urllink_collection[1]=links
    except Exception:
        pass
    if(depth>1):
        for val in range(1,depth):
            for link in urllink_collection[val]:
                try:
                    #driver = get_driver_link(link)
                    driver.get(url_link)
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
    #options = webdriver.ChromeOptions() 
    #options.add_argument("start-maximized")
    #options.add_argument('disable-infobars')
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_PATH")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    #links = depth_scraping(url_link=url_link,depth=depth)
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    print(driver)
    #driver = webdriver.Chrome(ChromeDriverManager().install())
    """
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
    #links = driver.find_elements_by_css_selector("link")
    print("Links are")
    print(links)
    
    """
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
    """
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

