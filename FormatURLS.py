import os
import json

os.chdir(os.getcwd() + '/files/FormatURLS')

input_file = open("input.json", 'r')
file_data = json.load(input_file)
input_file.close()

#Format URLS
has_website = []
for entry in file_data:
    if "website" in entry:
        entry["website"] = entry["website"]\
            .strip()\
            .replace('https://', '')\
            .replace('http://', '')\
            .replace('www.', '')\
            .split('/')[0]\
            .split('#')[0]\
            .lower()
    if "website" in entry:
        print entry["website"]
        has_website.append(entry)

output_file = open('output.json', 'w')
json.dump(has_website, output_file, indent=4, ensure_ascii=True)
output_file.close()