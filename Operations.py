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

#To calculate average price per brand
brand_total_price = {}   
brand_count = {} 

for product in Products:
    brand = product['brand']
    price = float(product['price'])
    if brand in brand_total_price:
        brand_total_price[brand] += price
        brand_count[brand] += 1
    else:
        brand_total_price[brand] = price
        brand_count[brand] = 1

highest_avg = 0
highest_brand = ''

newdata = []

for brand in brand_total_price:
    avg_price = brand_total_price[brand] / brand_count[brand]
    newdata.append({'Brand': brand, 'AveragePrice': avg_price})
    if avg_price > highest_avg:
        highest_avg = avg_price
        highest_brand = brand

print(f"Brand with highest average price: {highest_brand} ({highest_avg})")


with open('brand_average_prices.csv', 'w') as f:
    csvFileWriter = csv.writer(f)
    csvFileWriter.writerow(['Brand', 'Average Price'])
    for data in newdata:
        csvFileWriter.writerow([data['Brand'], data['AveragePrice']])

#To calculate highest inventory
brand_inventory_value = {}

for product in Products:
    brand = product['brand']
    price = float(product['price'])
    stock = int(product['stock'])
    total_value = price * stock

    if brand in brand_inventory_value:
        brand_inventory_value[brand] += total_value
    else:
        brand_inventory_value[brand] = total_value

highest_value = 0
highest_brand = ''

for brand, value in brand_inventory_value.items():
    if value > highest_value:
        highest_value = value
        highest_brand = brand

print(f"Brand with the largest total inventory value: {highest_brand} {highest_value}")

with open('brand_inventory_values.csv', 'w') as f:
    csvFileWriter = csv.writer(f)
    csvFileWriter.writerow(['Brand', 'Total Inventory Value'])
    for brand, value in brand_inventory_value.items():
        csvFileWriter.writerow([brand, value])

#To calculate top 10 highest inventory values

tempcopy = brand_inventory_value.copy()
top_10 = []

for x in range(10):
    if not tempcopy:
        break
    
    highest_brand = ""
    highest_value = -1
    for brand, value in tempcopy.items():
        if value > highest_value:
            highest_value = value
            highest_brand = brand
    top_10.append((highest_brand, highest_value))
    del tempcopy[highest_brand]

print("\nTop 10 brands by inventory value:")
with open('Top 10 brand_inventory_values.csv', 'w') as f:
    csvFileWriter = csv.writer(f)
    csvFileWriter.writerow(['Brand', 'Total Inventory Value'])
    for brand, value in top_10:
        csvFileWriter.writerow([brand, value])
        print(f"{brand}: {value}")

#To calulate Categorywise product count
ccat=0
ccat=Counter(product['category'] for product in Products)
print("Number of products as per category:")
with open('Categorywise_Productcount.csv', mode ='w')as file:
    csvFileWriter = csv.writer(file)
    csvFileWriter.writerow(['Category', 'Total'])
    for c, count in ccat.items():
        print(f"{c}: {count}")
        csvFileWriter.writerow([c,count])

max_cat = ""
max_cnt = 0

for category, count in ccat.items():
    if count > max_cnt:
        max_cnt = count
        max_cat = category
    if count == max_cnt:
        max_cnt=count
        max_cat+=" "+category
print(f"category with highest products: {max_cat} ({max_cnt} products)")