import os
import json
import re

os.chdir(os.getcwd() + '/files/FilterJSON')

input_file = open("input.json", 'r')
file_data = json.load(input_file)
input_file.close()

# for entry in file_data:
#     if "address" in entry:
#         addresses = entry["address"]
#         for address in addresses:
#             print address.encode('utf-8')


output_data = file_data


output_file = open('output.json', 'w')
json.dump(output_data, output_file, indent=4, ensure_ascii=False)
output_file.close()