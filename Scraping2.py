#Task 2: Scraping and parsing the barcode lookup website to extract information about the product details:-
from selenium import webdriver
import re
import csv
with open('barcode.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    list=["Barcode Formats","Category","Manufacturer"]
    spamwriter.writerow(list)
    browser = webdriver.Chrome("D:/webdriver/chromedriver.exe")
    browser.get("https://www.barcodelookup.com/609713860064")
    nav = browser.find_element_by_id("body-container")
    print(nav.text)
    data=nav.text.split('\n')
    #print "*******************"
    myData=[]
    for i in data:
        if re.compile('|'.join(list),re.IGNORECASE).search(i):
            #print i
            myData.append(i.encode('utf-8').split(":")[1])
        print myData
    spamwriter.writerow(myData)
#We used the selenium package again to scrap the product details data from the barcodelookup website since the required data was stored in html it was much simpler. We made a list of the required data which we wanted to extract from all the text data. Then filtered it and store it into a csv file.



