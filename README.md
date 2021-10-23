# URL_Status_Checker
<h1> 
<p align="center" >Python-flask-mongo-selenium-swagger for checking the status of a url and its hyperlinks</h1>

## Problem Statement:
Write a program that visits a particular url. It then finds all the hyperlinks on that page, visits them and checks whether those hyperlinks are alive or dead.Also Capture the below fields  in any database.
    Schema - (Sr No., Domain Name,Url,Status Code,Response Time)
    Note:- Give configuration variable as depth.
    Host this in a cloud platform with some frontend.
    Example Url:- https://www.flipkart.com/

## Tech Stack:
    Python-Flask,Selenium,webdriver,pymongo
    Database- Mongodb
    Cloud-Heroku
    
    
## Code Modules:
    db folder - mongodb configuration(used mongodb srv url cluster)
    routes - requests/responses for the application
    static - swagger.json file for documentation of the requests/responses for OAS3 Specification
    Selenium_code.py - Logic for checking the status of the url
    
## Mongodb -connection:
    
    mongodb+srv://Crediwatch_Db:Crediwatch_2021@cluster0.cxzmc.mongodb.net/test
    Password: Crediwatch_2021
    
## The application is deployed in heroku: 

[Linkforthedeployedapplication](https://crediwatch-flask-urlchecker.herokuapp.com/swagger/)

https://crediwatch-flask-urlchecker.herokuapp.com/swagger/
