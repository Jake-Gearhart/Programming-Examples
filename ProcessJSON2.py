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

os.chdir(os.getcwd() + '/files/ProcessJSON2')

input_file = open("input.json", 'r')
file_data = json.load(input_file)
input_file.close()

output_data = []

#Delete entries with no website
file_data = [entry for entry in file_data if "website" in entry]
for entry in file_data:
    entry["website"] = entry["website"] \
        .strip() \
        .replace('https://', '') \
        .replace('http://', '') \
        .replace('www.', '') \
        .split('/')[0] \
        .split('#')[0]

#Add sites to list
websites = []
for i in range(0, len(file_data)):
    print "Adding site " + str(i + 1) + "/" + str(len(file_data))
    if file_data[i]["website"] not in websites:
        websites.append(file_data[i]["website"])

#Group data with sites
for i in range(0, len(websites)):
    website = websites[i]
    print "Forming data from " + str(i+1) + "/" + str(len(websites)) + " " + websites[i]

    #Check for other site data
    data = []
    new_file_data = []
    for item in file_data:
        new_website = item["website"]
        if website is new_website:
            data.append(item)
        else:
            new_file_data.append(item)
    file_data = new_file_data

    #Format data
    for entry in data:
        del entry["website"]
        for attribute in entry:
            entry[attribute] = entry[attribute].encode('utf-8')
    site = {
        "website": website,
        "occurrences_of_site": len(data),
        "data": data
    }
    output_data.append(site)

output_data = sorted(output_data, key=lambda k: k["occurrences_of_site"], reverse=True)

output_file = open('output.json', 'w')
json.dump(output_data, output_file, indent=4, ensure_ascii=False)
output_file.close()
