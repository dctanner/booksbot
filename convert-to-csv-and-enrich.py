import json
import os
import csv
import requests

with open(os.path.abspath('out_1.json'), 'r') as f:
    items_json = json.loads(f.read())

csv_f = open('out_1_enriched.csv', 'w', dialect='excel')
csv_out = csv.writer(csv_f)

# "name": "VelocityEHS", "logo": "https://ga0.imgix.net/logo/o/104315-1467798979-3301337?ixlib=rb-1.0.0&ch=Width%2CDPR&auto=format", "desc": "Environment, Health, Safety (EHS) Management Software", "rating": "4.67", "num_reviews": "3", "website_click_out": "/x/velocityehs-application?route=listing_detail&from_listing=104315", "category": "https://www.getapp.com/business-intelligence-analytics-software/data-visualization/?page=2"},
cols = ["name","website","getapp_logo","clearbit_logo","desc","rating","num_reviews","cat","subcat"]
csv_out.writerow(cols)
for json_in in items_json:
    csv_out = []
    csv_out[cols.index("")] = json_in[""]
    csv_out[cols.index("name")] = json_in["name"]
    csv_out[cols.index("getapp_logo")] = json_in["logo"]
    csv_out[cols.index("desc")] = json_in["desc"]
    csv_out[cols.index("rating")] = json_in["rating"]
    csv_out[cols.index("num_reviews")] = json_in["num_reviews"]

    if json_in["website_click_out"]:
        redirect_req = requests.head(json_in["website_click_out"])
        print r.url
