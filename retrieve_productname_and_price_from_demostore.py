import csv
from woocommerce import API

wcapi = API(
    url="http://dev.bootcamp.store.supersqa.com/",
    consumer_key="ck_8aaa7975d95710ba653193e0d97863e69fc4cdd4",
    consumer_secret="cs_94f4527162cce839d17270c622ab5a64919bd733",
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
