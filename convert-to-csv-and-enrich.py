import json
import os
import csv
import requests
import re
from urllib.parse import urlparse
from py_ms_cognitive import PyMsCognitiveWebSearch
search_service = PyMsCognitiveWebSearch('', search_term)
import clearbit
clearbit.key = 'sk_7177eb671d9fe0c5cbbc4d6113e2157a'

with open(os.path.abspath('out_1_sample.json'), 'r') as f:
    items_json = json.loads(f.read())

csv_f = open('out_1_enriched_sample.csv', 'w')
csv_writer = csv.writer(csv_f, dialect='excel')

# "name": "VelocityEHS", "logo": "https://ga0.imgix.net/logo/o/104315-1467798979-3301337?ixlib=rb-1.0.0&ch=Width%2CDPR&auto=format", "desc": "Environment, Health, Safety (EHS) Management Software", "rating": "4.67", "num_reviews": "3", "website_click_out": "/x/velocityehs-application?route=listing_detail&from_listing=104315", "category": "https://www.getapp.com/business-intelligence-analytics-software/data-visualization/?page=2"},
cols = ["name","domain","getapp_logo","clearbit_logo","desc","rating","num_reviews","cat","subcat","getapp_cat_link"]
csv_writer.writerow(cols)
for json_in in items_json:
    csv_out = [None] * len(cols)
    # csv_out[cols.index("")] = json_in[""]
    csv_out[cols.index("name")] = json_in["name"]
    csv_out[cols.index("getapp_logo")] = json_in["logo"]
    csv_out[cols.index("desc")] = json_in["desc"]
    csv_out[cols.index("rating")] = json_in["rating"]
    csv_out[cols.index("num_reviews")] = json_in["num_reviews"]
    csv_out[cols.index("getapp_cat_link")] = json_in["category"]
    csv_out[cols.index("cat")] = json_in["category"].split('/')[3]
    csv_out[cols.index("subcat")] = json_in["category"].split('/')[4]

    # if json_in["website_click_out"]: # find website via getapp link redirects
    #     try:
    #         redirect_req = requests.get("https://www.getapp.com"+json_in["website_click_out"], allow_redirects=True)
    #         redirect_req2 = requests.get(re.search(r'location\.replace\("(.*)"\);', redirect_req.text).group(1), allow_redirects=True)
    #         getapp_domain = urlparse(redirect_req2.url).hostname
    #         csv_out[cols.index("domain")] = getapp_domain
    #         print("Resolved getapp redirect to: "+getapp_domain)
    #     except:
    #         print("Error resolving getapp redirect")
    # else: # find website from name using clearbit

    # just use clearbit, getapp website was throwing errors
    try:
        clearbit_res = clearbit.NameToDomain.find(name=json_in["name"])
        if clearbit_res:
            csv_out[cols.index("domain")] = clearbit_res["domain"]
            csv_out[cols.index("clearbit_logo")] = clearbit_res["logo"]
            print("Found domain with clearbit: "+clearbit_res["domain"])
        elif json_in["website_click_out"]: # find website via getapp link redirects
            try:
                redirect_req = requests.get("https://www.getapp.com"+json_in["website_click_out"], allow_redirects=True)
                redirect_req2 = requests.get(re.search(r'location\.replace\("(.*)"\);', redirect_req.text).group(1), allow_redirects=True)
                getapp_domain = urlparse(redirect_req2.url).hostname
                csv_out[cols.index("domain")] = getapp_domain
                print("Resolved getapp redirect to: "+getapp_domain)
            except:
                print("Error resolving getapp redirect")
    except:
        print("Error hitting clearbit")

    # TODO: if clearbit is None, use getapp if its here, or fallback to Bing search if

    csv_writer.writerow(csv_out)
