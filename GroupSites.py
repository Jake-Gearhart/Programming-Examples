import os
import json

os.chdir(os.getcwd() + '/files/GroupSites')

input_file = open("input.json", 'r')
input_data = json.load(input_file)
input_file.close()

websites = []

for entry in input_data:
    entry["website"] = entry["website"].lower()
    print entry
    if entry["website"] not in websites:
        websites.append(entry["website"])

output_data = []
for i in range(0, len(websites)):
    website = websites[i]
    print str(i) + "/" + str(len(websites)) + " " + website
    new_data = []

    for entry in input_data:
        if entry["website"] == website:
            new_data.append(entry)

    print len(new_data)
    output_data.append(
        {
            "website": website,
            "data": new_data,
            "occurrences_of_site": len(new_data)
        }
    )

for thing in output_data:
    xyz = thing.get("data")
    for bla in xyz:
        del bla["website"]
    while {} in xyz:
        xyz.remove({})

output_data = sorted(output_data, key=lambda k: k["occurrences_of_site"], reverse=True)

output_file = open('output.json', 'w')
json.dump(output_data, output_file, indent=4)
output_file.close()