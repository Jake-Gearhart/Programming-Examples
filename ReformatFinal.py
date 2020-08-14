import os
import json

os.chdir(os.getcwd() + '/files/ReformatFinal')

input_file = open("input.json", 'r')
input_data = json.load(input_file)
input_file.close()

def process_text(string):
    return string\
            .strip()\
            .replace('\n', '')\
            .encode('utf-8')\
            .split(',')[0]
output_data = []
keys = ["city", "name", "zip", "country", "phone", "state", "address"]
for i in range(0, len(input_data)):
    data = input_data[i]["data"]
    website = input_data[i]["website"]
    occurrences_of_site = input_data[i]["occurrences_of_site"]

    # Remove null fields and get longest entry in field
    for i in range(0, len(data)):
        entry = data[i]
        new_entry = {}
        for field in entry:
            if entry[field] and entry[field] is not None:
                new_string = process_text(max(entry[field], key=len))
                new_entry[field] = new_string
        data[i] = new_entry

    # Find best entry
    best_entry = {}
    if len(data):
        best_entries = []
        for entry in data:
            if "state" in entry and "city" in entry and "zip" in entry:
                best_entries.append(entry)
        if len(best_entries) < 1:
            for entry in data:
                if "state" in entry and "city" in entry:
                    best_entries.append(entry)
        if len(best_entries) < 1:
            for entry in data:
                if ("state" in entry and "zip" in entry) or ("city" in entry and "zip" in entry):
                    best_entries.append(entry)
        if len(best_entries) < 1:
            for entry in data:
                if "state" in entry or "city" in entry:
                    best_entries.append(entry)
        if len(best_entries) < 1:
            for entry in data:
                if "zip" in entry:
                    best_entries.append(entry)
        if len(best_entries) < 1:
            for entry in data:
                best_entries.append(entry)
        if len(best_entries) > 0:
            best_entry = max(best_entries, key=len)
    best_entry["website"] = website
    best_entry["                                occurrences_of_site"] = occurrences_of_site

    # Get city from address
    if "address" in best_entry and "city" not in best_entry:
        best_entry["city"] = best_entry["address"].split(" ")[0]

    # Fill in nulls
    for key in keys:
        if key not in best_entry or len(best_entry[key]) < 1:
            best_entry[key] = None

    print best_entry
    output_data.append(best_entry)


output_file = open('output.json', 'w')
json.dump(output_data, output_file, indent=4, ensure_ascii=False)
output_file.close()