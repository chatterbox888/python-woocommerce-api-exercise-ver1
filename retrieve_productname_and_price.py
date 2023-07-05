"""
Use woocommerce API Python library, to make API calls to list all products.

Create a csv file that will have a list of products and their price (use only the
field 'price'. So the csv will have two columns 'name' and 'price'.

Assigned to: Jeniffer Lagman
Date:        7/5/2023

"""


import csv
from woocommerce import API

wcapi = API(
    url="http://localhost:8888/mysite1/",
    consumer_key="ck_8e8ae1e5992cc2ccdd3ca276279b21b3e18fcda8",
    consumer_secret="cs_88d97b24beaa2fc723b40bcb592606d79bad80c8",
    version="wc/v3"
)

rs_api = wcapi.get("products", params={"per_page": 100})

all_products = rs_api.json()

data = []
for product in all_products:
        name = product["name"]
        price = product["price"]
        data.append({"name": name, "price": price})

with open('./products.csv', "w", newline="") as csv_file:
    fieldnames = ["name", "price"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

