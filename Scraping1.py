#Documentation for Business Intelligence Project US Barcoders
#Task 1: 	Scraping and Parsing United Website for Store Service Details.
#The first Step in this Task was scraping the united website :-

from selenium import webdriver
from time import sleep
browser = webdriver.Chrome("C:/webdrivers/chromedriver.exe")
url = 'https://www.unitedsupermarkets.com/rs/StoreLocator'
abc = browser.get(url)
sleep(15)
browser.find_element_by_id('main-body').click()
a = browser.page_source
ab = open("scraping.txt", 'w')
ab.write(a)
ab.close()
browser.close()

#We used the selenium package to scrap the website using the chrome webdriver. Our store details were inside a javascript was a bit tricky to workout with. The major change we did in our code was to include the sleep(15) function to let the website load completely so that we can capture the whole javascript.

#The Second Step in this task was extracting the JSON data which contain information about all the stores:-
import json
import csv
with open('scraping.csv', 'w') as csvfile:
    fieldnames = [""]
    writer = csv.writer(csvfile,delimiter=',', quoting=csv.QUOTE_MINIMAL)
	filepath = 'scraping.txt'  
    with open(filepath) as fp:  
       line = fp.readline()
       cnt = 1
       while line:
           line = fp.readline()
           cnt += 1
           if "var stores" in line:
               line_v = line
    var = line_v.find('=')
    print(var)  
    var_2 = line_v.find(';')
    print(var_2)  
    json_data = line_v[var + 1 : var_2 ]
    data=json.loads(json_data)
    
    for d in data:
        services=json.loads(data[0]['Services'])
        for s in services['Services']:
            print("StoreName "+":"+d['StoreName']+","+" StoreID "+":"+str(d['StoreID'])+","+"LocationName "+":"+d['LocationName']+","+" State "+":"+d['State']+","+" Zipcode "+":"+d['Zipcode']+","+"Service Name "+":"+s['Name']+","+"Service Value "+":"+s['Value'])
            writer.writerow(["StoreName "+":"+d['StoreName']," StoreID "+":"+str(d['StoreID']),"LocationName "+":"+d['LocationName']," State "+":"+d['State']," Zipcode "+":"+d['Zipcode'],"Service Name "+":"+s['Name'],"Service Value "+":"+s['Value']])

#We first extracted the var stores variable from the javascript which contain our json data for the service details of different stores. Then we used json.loads function to convert json object to python dictionary.
#Then we printed the necessary details like Store Name, StoreID, LocationName, State, Zipcode and the Service Name and Service values of the respective stores.
#We printed all these information into a csv file which would further be processed by the ETL team to Mongodb.
#These steps were repeated for all the stores of United – United Supermarkets, Albertson, Amigos, MarketStreet.
