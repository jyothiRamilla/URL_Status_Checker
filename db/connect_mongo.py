from pymongo import MongoClient  

def connect_db():

    client=MongoClient()  
    # Connect with the portnumber and host  

    client = MongoClient("mongodb+srv://Crediwatch_Db:Crediwatch_2021@cluster0.cxzmc.mongodb.net/test")      
    # Access database  

    mydatabase = client['Url_checker']  
    # Access collection of the database  
    collection=mydatabase['url_status_collection'] 
    return collection
