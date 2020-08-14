import os
import json
import re

# ==================================================================================================================== #

state_province_map = {
    "ab": "AB",
    "alb": "AB",
    "alberta": "AB",
    "alta": "AB",
    "ak": "AK",
    "alaska": "AK",
    "al": "AL",
    "ala": "AL",
    "alab": "AL",
    "alabama": "AL",
    "ar": "AR",
    "ark": "AR",
    "arkansas": "AR",
    "americansamoa": "AS",
    "amersamoa": "AS",
    "as": "AS",
    "asamoa": "AS",
    "samoa": "AS",
    "ariz": "AZ",
    "arizona": "AZ",
    "az": "AZ",
    "bc": "BC",
    "britishcolumbia": "BC",
    "cb": "BC",
    "colombiebritannique": "BC",
    "ca": "CA",
    "cali": "CA",
    "calif": "CA",
    "california": "CA",
    "co": "CO",
    "colo": "CO",
    "colorado": "CO",
    "conn": "CT",
    "connecticut": "CT",
    "ct": "CT",
    "dc": "DC",
    "disofcol": "DC",
    "disofcolumbia": "DC",
    "distofcol": "DC",
    "distofcolumbia": "DC",
    "districtofcol": "DC",
    "districtofcolumbia": "DC",
    "de": "DE",
    "del": "DE",
    "delaware": "DE",
    "fl": "FL",
    "fla": "FL",
    "flo": "FL",
    "florida": "FL",
    "fm": "FM",
    "micronesia": "FM",
    "ga": "GA",
    "georgia": "GA",
    "gu": "GU",
    "guam": "GU",
    "hawaii": "HI",
    "hi": "HI",
    "ia": "IA",
    "iowa": "IA",
    "id": "ID",
    "idaho": "ID",
    "il": "IL",
    "ill": "IL",
    "illinois": "IL",
    "in": "IN",
    "ind": "IN",
    "indiana": "IN",
    "kans": "KS",
    "kansas": "KS",
    "ks": "KS",
    "kentucky": "KY",
    "ky": "KY",
    "la": "LA",
    "louisiana": "LA",
    "ma": "MA",
    "mass": "MA",
    "massachusetts": "MA",
    "man": "MB",
    "manitoba": "MB",
    "mb": "MB",
    "maryland": "MD",
    "md": "MD",
    "maine": "ME",
    "me": "ME",
    "marshallislands": "MH",
    "mh": "MH",
    "mi": "MI",
    "mich": "MI",
    "michigan": "MI",
    "minn": "MN",
    "minnesota": "MN",
    "mn": "MN",
    "missouri": "MO",
    "mo": "MO",
    "mp": "MP",
    "nmarianas": "MP",
    "northernmarianas": "MP",
    "mississippi": "MS",
    "ms": "MS",
    "mont": "MT",
    "montana": "MT",
    "mt": "MT",
    "nb": "NB",
    "newbrunswick": "NB",
    "nouveaubrunswick": "NB",
    "nc": "NC",
    "ncarolina": "NC",
    "norcar": "NC",
    "northcarolina": "NC",
    "nd": "ND",
    "ndakota": "ND",
    "nordak": "ND",
    "northdakota": "ND",
    "ne": "NE",
    "nebr": "NE",
    "nebraska": "NE",
    "newhamp": "NH",
    "newhampshire": "NH",
    "nh": "NH",
    "nhampshire": "NH",
    "newjer": "NJ",
    "newjersey": "NJ",
    "nj": "NJ",
    "njersey": "NJ",
    "labrador": "NL",
    "newfoundland": "NL",
    "newfoundlandandlabrador": "NL",
    "nl": "NL",
    "terreneuve": "NL",
    "terreneuveetlabrador": "NL",
    "tnl": "NL",
    "newmex": "NM",
    "newmexico": "NM",
    "nm": "NM",
    "nmexico": "NM",
    "nouvelleecosse": "NS",
    "novascotia": "NS",
    "ns": "NS",
    "northwestterritories": "NT",
    "nt": "NT",
    "nwt": "NT",
    "nwterr": "NT",
    "nwterritories": "NT",
    "territoiresdunordouest": "NT",
    "tno": "NT",
    "nu": "NU",
    "nunavut": "NU",
    "nvt": "NU",
    "nev": "NV",
    "nevada": "NV",
    "nv": "NV",
    "newyor": "NY",
    "newyork": "NY",
    "ny": "NY",
    "nyork": "NY",
    "oh": "OH",
    "ohio": "OH",
    "ok": "OK",
    "okla": "OK",
    "oklahoma": "OK",
    "on": "ON",
    "ont": "ON",
    "ontario": "ON",
    "or": "OR",
    "ore": "OR",
    "oregon": "OR",
    "pa": "PA",
    "penn": "PA",
    "pennsylvania": "PA",
    "ileduprinceedouard": "PE",
    "ipe": "PE",
    "pe": "PE",
    "pei": "PE",
    "princeedward": "PE",
    "princeedwardi": "PE",
    "princeedwardisl": "PE",
    "princeedwardisland": "PE",
    "pr": "PR",
    "puertorico": "PR",
    "palau": "PW",
    "pw": "PW",
    "pq": "QC",
    "qb": "QC",
    "qc": "QC",
    "que": "QC",
    "quebec": "QC",
    "rhodeisl": "RI",
    "rhodeisland": "RI",
    "ri": "RI",
    "sc": "SC",
    "scarolina": "SC",
    "southcarolina": "SC",
    "sd": "SD",
    "sdakota": "SD",
    "southdakota": "SD",
    "sask": "SK",
    "saskatchewan": "SK",
    "sk": "SK",
    "tenn": "TN",
    "tennessee": "TN",
    "tn": "TN",
    "tex": "TX",
    "texas": "TX",
    "tx": "TX",
    "ut": "UT",
    "utah": "UT",
    "va": "VA",
    "virginia": "VA",
    "usvi": "VI",
    "usvirginislands": "VI",
    "vi": "VI",
    "virginislands": "VI",
    "ver": "VT",
    "verm": "VT",
    "vermont": "VT",
    "vt": "VT",
    "wa": "WA",
    "wash": "WA",
    "washington": "WA",
    "wi": "WI",
    "wis": "WI",
    "wisconsin": "WI",
    "westvirginia": "WV",
    "wv": "WV",
    "wva": "WV",
    "wvirginia": "WV",
    "wy": "WY",
    "wyo": "WY",
    "wyoming": "WY",
    "yn": "YT",
    "yt": "YT",
    "yukon": "YT",
    "national": "National"
}

country_map = {
    "au": "AU",
    "aus": "AU",
    "australia": "AU",
    "ca": "CN",
    "can": "CN",
    "canada": "CN",
    "cn": "CN",
    "newzealand": "NZ",
    "nz": "NZ",
    "america": "US",
    "unitedstates": "US",
    "unitedstatesamerica": "US",
    "unitedstatesofamerica": "US",
    "us": "US",
    "usa": "US"
}

mappingAttributes = ["address", "state"]
mappings = [
    {
        "key": "state",
        "map": state_province_map,
    },
    {
        "key": "country",
        "map": country_map,
    },
]

# ==================================================================================================================== #

os.chdir(os.getcwd() + '/files/ProcessJSON')

input_file = open("input.json", 'r')
file_data = json.load(input_file)
input_file.close()

data = []

for i in range(0, len(file_data)):
    print "Checking for sites in " + str(i+1) + "/" + str(len(file_data))
    obj = file_data[i]
    if "website" in obj and (isinstance(obj["website"], int) or len(obj["website"]) > 0):
        data.append(obj)
    else:
        continue

for i in range(0, len(data)):
    print "Processing entry " + str(i + 1) + "/" + str(len(data))
    entry = data[i]

    for attribute in entry:
        entry[attribute] = entry[attribute]\
            .strip()\
            .replace('\n', '')\
            .encode('utf-8')

    entry["website"] = entry["website"]\
        .strip()\
        .replace('https://', '')\
        .replace('http://', '')\
        .replace('www.', '')\
        .split('/')[0]\
        .split('#')[0]

    if "state" in entry and not isinstance(entry["state"], list):
        entry["state"] = [entry["state"]]
    else:
        entry["state"] = []
    if "country" in entry and not isinstance(entry["country"], list):
        entry["country"] = [entry["country"]]
    else:
        entry["country"] = []
    if "phone" in entry and not isinstance(entry["phone"], list):
        entry["phone"] = [entry["phone"]]
    else:
        entry["phone"] = []
    if "zip" in entry and not isinstance(entry["zip"], list):
        entry["zip"] = [entry["zip"]]
    else:
        entry["zip"] = []
    if "city" in entry and not isinstance(entry["city"], list):
        entry["city"] = [entry["city"]]
    else:
        entry["city"] = []

    for attribute in mappingAttributes:
        if attribute in entry and (isinstance(entry[attribute], int) or len(entry[attribute]) > 0):

            stringList = re.split("[ ().,:]", entry[attribute])


            for mapping in mappings:
                key = mapping.get("key")
                map = mapping.get("map")

                deleteIndexes = []

                for i in range(0, len(stringList)):
                    if i+1 < len(stringList) and (stringList[i]+stringList[i+1]).lower() in map:
                        location = (stringList[i]+stringList[i+1]).lower()
                        abbreviation = map.get(location)
                        if not key in entry:
                            entry[key] = [abbreviation]
                        elif abbreviation not in entry[key]:
                            entry[key].append(abbreviation)
                        deleteIndexes.append(i)

                    elif stringList[i].lower() in map:
                        location = stringList[i].lower()
                        abbreviation = map.get(location)
                        if not key in entry:
                            entry[key] = [abbreviation]
                        elif abbreviation not in entry[key]:
                            entry[key].append(abbreviation)
                        deleteIndexes.append(i)

                entry[attribute] = stringList
                for index in sorted(deleteIndexes, reverse=True):
                    del entry[attribute][index]

            entry[attribute] = " ".join(entry[attribute]).strip()

websites = []
dedupedData = []

for i in range(0, len(data)):
    if not "website" in data[i] or data[i]["website"] is None or data[i]["website"] is "":
        continue
    website = data[i]["website"]
    if website not in websites:
        newData = []
        newData.append(data[i])
        websites.append(website)
        for n in range(i+1, len(data)):
            if "website" in data[n] and (isinstance(data[n]["website"], int) or len(data[n]["website"]) > 0):
                if data[n]["website"] == website:
                    newData.append(data[n])
        print str(i+1) + "/" + str(len(data)) + " " + website + " x" + str(len(newData))
        dedupedData.append(newData)

dedupedData = sorted(dedupedData, key=len, reverse=True)

for i in range(0, len(dedupedData)):
    print "Processing deduped data " + str(i + 1) + "/" + str(len(dedupedData))
    website = dedupedData[i][0]["website"]
    name = []
    country = []
    state = []
    address = []
    city = []
    zip = []
    phone = []
    for item in dedupedData[i]:
        for check in [["name", name], ["country", country], ["state", state], ["address", address],]:
            field = check[0]
            if field in item and (isinstance(item[field], int) or len(item[field]) > 0):
                if isinstance(item[field], list):
                    for entry in item[field]:
                        if entry not in check[1]:
                            check[1].append(entry)
                else:
                    if item[field] not in check[1]:
                        check[1].append(item[field])
    fields = {
        "occurrences_of_this_site": len(dedupedData[i]),
        "website": website,
        "name": name,
        "country": ", ".join(country),
        "state": ", ".join(state),
        "city": city,
        "zip": zip,
        "phone": phone,
        "address": address
    }
    dedupedData[i] = {}
    for field in fields:
        attribute = fields.get(field)
        if isinstance(attribute, int) or len(attribute) > 0:
            dedupedData[i][field] = attribute

output_file = open('output.json', 'w')
json.dump(dedupedData, output_file, indent=4, ensure_ascii=False)
output_file.close()
