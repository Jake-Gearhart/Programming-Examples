import os
import geonamescache
import json
import us
geonames = geonamescache.GeonamesCache()

os.chdir(os.getcwd() + '/files/CombiningJSONFiles')

data = []
for fileName in os.listdir("Input"):
    if ".json" not in fileName:
        continue
    inputFile = open("Input/"+fileName, 'r')
    newData = json.load(inputFile)
    inputFile.close()

    data = data + newData


output_file = open('output_file.json', 'w')
json.dump(data, output_file, indent=4)
output_file.close()
