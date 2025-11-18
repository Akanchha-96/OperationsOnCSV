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

#To calulate Brandwise product count
cc=0
cc=Counter(product['brand'] for product in Products)
print("Number of products as per Brand:")
with open('brandwise_Productcount.csv', mode ='w')as file:
    csvFileWriter = csv.writer(file)
    csvFileWriter.writerow(['Brand', 'Total'])
    for b, count in cc.items():
        print(f"{b}: {count}")
        csvFileWriter.writerow([b,count])

max_brand = ""
max_count = 0

for brand, count in cc.items():
    if count > max_count:
        max_count = count
        max_brand = brand
print(f"Brand with highest products: {max_brand} ({max_count} products)")