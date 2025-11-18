import csv
import time
from collections import Counter

#To read a CSV file
Products=[]
#def csvread():
#print("start time",time.time())
with open('C:/Python Course/CSVFile/my-first-git-project/OperationsOnCSV/products.csv', mode='r') as file:
   csvFile = csv.DictReader(file)
   for lines in csvFile:
    temp_set = {}
    temp_set['index'] = lines['Index']
    temp_set['name'] = lines['Name']
    temp_set['description'] = lines['Description']
    temp_set['brand'] = lines['Brand']
    temp_set['category'] = lines['Category']
    temp_set['price'] = lines['Price']
    temp_set['currency'] = lines['Currency']
    temp_set['stock'] = lines['Stock']
    temp_set['ean'] = lines['EAN']
    temp_set['color'] = lines['Color']
    temp_set['size'] = lines['Size']
    temp_set['availability'] = lines['Availability']
    temp_set['id'] = lines['Internal ID']
    Products.append(temp_set)