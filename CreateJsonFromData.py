import os
from lxml import html
import json

os.chdir(os.getcwd() + '/files/CreateJsonFromData')

input_sites = open('input_data.txt', 'r')


def create_json(name, address, website):
    return {"name": name, "address": address, "website": website}


data = []
for site in input_sites:
    data.append(create_json('', '', site.replace('\n', '')))

output_sites = open('output_sites.json', 'w')
json.dump(data, output_sites, indent=4)
output_sites.close()
