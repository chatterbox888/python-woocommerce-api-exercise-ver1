"""
Pre-requisite - Ecommerce Wordpress site and API credentials

This script will get a list of all users for the website.
The script will output a csv file with a list of email addresses.

Assigned to: Jeniffer Lagman
Date:        7-05-2023
"""


from woocommerce import API

wcapi = API(
    url="http://localhost:8888/mysite1/",
    consumer_key="ck_8e8ae1e5992cc2ccdd3ca276279b21b3e18fcda8",
    consumer_secret="cs_88d97b24beaa2fc723b40bcb592606d79bad80c8",
    version="wc/v3"
)

rs_api = wcapi.get("customers", params={"per_page": 100})

all_customers = rs_api.json()

#write the emails into a csv file
with open('./customer_emails.csv', 'w') as f:
    for i in all_customers:
        f.write(i['email'] + '\n')








