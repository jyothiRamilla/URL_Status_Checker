## Mongodb -connection:
    
##Create a mongo db srv cluster url 

from pymongo import MongoClient  

def connect_db():

    client=MongoClient()  
    # Connect with the portnumber and host  

    client = MongoClient("mongodbsrvclusterurlhere")      
    # Access database  

    mydatabase = client['Url_checker']  
    # Access collection of the database  
    collection=mydatabase['url_status_collection'] 
    return collection
