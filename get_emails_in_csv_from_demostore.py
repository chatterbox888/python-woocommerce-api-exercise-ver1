"""
Pre-requisite - Ecommerce Wordpress site and API credentials

This script will get a list of all users for the website.
The script will output a csv file with a list of email addresses.
"""


from woocommerce import API

wcapi = API(
    url="http://dev.bootcamp.store.supersqa.com/",
    consumer_key="ck_8aaa7975d95710ba653193e0d97863e69fc4cdd4",
    consumer_secret="cs_94f4527162cce839d17270c622ab5a64919bd733",
    version="wc/v3"
)

rs_api = wcapi.get("customers", params={"per_page": 100})

all_customers = rs_api.json()

#write the emails into a csv file
with open('./customer_emails.csv', 'w') as f:
    for i in all_customers:
        f.write(i['email'] + '\n')
