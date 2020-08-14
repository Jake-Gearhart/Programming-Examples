import os
import json
import re

# ==================================================================================================================== #

state_province_map_single = {
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
    "as": "AS",
    "asamoa": "AS",
    "samoa": "AS",
    "ariz": "AZ",
    "arizona": "AZ",
    "az": "AZ",
    "bc": "BC",
    "cb": "BC",
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
    "mississippi": "MS",
    "ms": "MS",
    "mont": "MT",
    "montana": "MT",
    "mt": "MT",
    "nb": "NB",
    "nc": "NC",
    "nd": "ND",
    "ne": "NE",
    "nebr": "NE",
    "nebraska": "NE",
    "nh": "NH",
    "nj": "NJ",
    "labrador": "NL",
    "nl": "NL",
    "tnl": "NL",
    "nm": "NM",
    "ns": "NS",
    "nt": "NT",
    "nwt": "NT",
    "tno": "NT",
    "nu": "NU",
    "nunavut": "NU",
    "nvt": "NU",
    "nev": "NV",
    "nevada": "NV",
    "nv": "NV",
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
    "ipe": "PE",
    "pe": "PE",
    "pei": "PE",
    "pr": "PR",
    "palau": "PW",
    "pw": "PW",
    "pq": "QC",
    "qb": "QC",
    "qc": "QC",
    "que": "QC",
    "quebec": "QC",
    "ri": "RI",
    "sc": "SC",
    "sd": "SD",
    "sask": "SK",
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
    "vi": "VI",
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
    "wv": "WV",
    "wva": "WV",
    "wy": "WY",
    "wyo": "WY",
    "wyoming": "WY",
    "yn": "YT",
    "yt": "YT",
    "yukon": "YT",
    "national": "National"
}

state_province_map_multiple = {
    "american samoa": "AS",
    "amer samoa": "AS",
    "british columbia": "BC",
    "colombie britannique": "BC",
    "dis of col": "DC",
    "dis of columbia": "DC",
    "dist of col": "DC",
    "dist of columbia": "DC",
    "district of col": "DC",
    "district of columbia": "DC",
    "marshall islands": "MH",
    "n marianas": "MP",
    "northern marianas": "MP",
    "new brunswick": "NB",
    "nouveau brunswick": "NB",
    "north carolina": "NC",
    "n carolina": "NC",
    "north dakota": "ND",
    "n dakota": "ND",
    "new hamp": "NH",
    "new hampshire": "NH",
    "n hampshire": "NH",
    "new jersey": "NJ",
    "new jer": "NJ",
    "n jersey": "NJ",
    "newfoundland": "NL",
    "newfoundland and labrador": "NL",
    "terre neuve": "NL",
    "terre neuveet labrador": "NL",
    "new mexico": "NM",
    "new mex": "NM",
    "n mexico": "NM",
    "nouvelleecosse": "NS",
    "nova scotia": "NS",
    "north westterritories": "NT",
    "n wterritories": "NT",
    "n wterr": "NT",
    "territoires dunordouest": "NT",
    "new yorm": "NY",
    "new yor": "NY",
    "ile duprinceedouard": "PE",
    "prince edward": "PE",
    "prince edwardi": "PE",
    "prince edwardisl": "PE",
    "prince edward island": "PE",
    "puerto rico": "PR",
    "rhode island": "RI",
    "rhode isl": "RI",
    "south carolina": "SC",
    "s carolina": "SC",
    "south dakota": "SD",
    "s dakota": "SD",
    "saskatchewan": "SK",
    "virgin islands": "VI",
    "west virginia": "WV",
    "w virginia": "WV",
}

country_map_single = {
    "au": "AU",
    "aus": "AU",
    "australia": "AU",
    "ca": "CN",
    "can": "CN",
    "canada": "CN",
    "cn": "CN",
    "nz": "NZ",
    "america": "US",
    "us": "US",
    "usa": "US"
}

country_map_multiple = {
    "newzealand": "NZ",
    "unitedstates": "US",
    "unitedstatesamerica": "US",
    "unitedstatesofamerica": "US",
}

mappings = [
    {
        "key": "state",
        "singlemap": state_province_map_single,
        "multimap": state_province_map_multiple,
    },
    {
        "key": "country",
        "singlemap": country_map_single,
        "multimap": country_map_multiple,
    }
]

check = ["address", "city"]

# ==================================================================================================================== #

def process_text(string):
    return string\
            .strip()\
            .replace('\n', '')\
            .encode('utf-8')

def remove_word(string, word):
    return re.sub(re.escape(word), "", string, flags=re.IGNORECASE)\
            .replace("  ", " ")\
            .replace("()", "")\
            .strip()


os.chdir(os.getcwd() + '/files/ProcessGroupedSites')

input_file = open("input.json", 'r')
input_data = json.load(input_file)
input_file.close()

for i in range(0, len(input_data)):
    print "Processing " + str(i+1) + "/" + str(len(input_data))
    for data in input_data[i]["data"]:

        #Make all data in lists
        for field in data:
            if isinstance(data[field], basestring):
                data[field] = [process_text(data[field])]
            elif isinstance(data[field], list):
                for i in range(0, len(data[field])):
                    if isinstance(data[field][i], basestring):
                        data[field][i] = process_text(data[field][i])

        #Add missing fields
        for field in ["name", "country", "state", "city", "zip", "phone", "address"]:
            if not field in data:
                data[field] = []

        #Process Data
        for search in check:
            if search in data:
                for i in range(0, len(data[search])):
                    text = data[search][i]
                    splitText = re.split("[ ().,:]", text)
                    for word in splitText:
                        word = word.lower()
                        for mapping in mappings:
                            matches = []
                            key = mapping["key"]
                            singlemap = mapping["singlemap"]
                            multimap = mapping["multimap"]
                            #Singlemap
                            for match in singlemap:
                                if word == match:
                                    matches.append(singlemap[match])
                                    data[search][i] = remove_word(text, word)
                                    text = remove_word(text, word)
                            #Multimap
                            combinedText = "".join(splitText)
                            for match in multimap:
                                if match.replace(" ", "") in combinedText:
                                    matches.append(multimap[match])
                                    data[search][i] = remove_word(text, word)
                                    text = remove_word(text, word)

                            if key in data:
                                data[key] = data[key] + matches
                            else:
                                data[key] = matches
                    

                        regex = re.findall("\d+", word)

                        # 000-000-0000 or 0-000-000-0000
                        if (len(regex) == 3 and len(regex[0]) == 3 and len(regex[1]) == 3 and len(regex[2]) == 4) or (len(regex) == 4 and len(regex[0]) == 1 and len(regex[1]) == 3 and len(regex[2]) == 3  and len(regex[3]) == 4):
                            result = "-".join(regex)
                            data[search][i] = remove_word(text, word)
                            data["phone"] = data["phone"] + [result]

                        # 00000 or 00000-0000
                        elif (len(regex) == 1 and len(regex[0]) == 5) or (len(regex) == 2 and len(regex[0]) == 5 and len(regex[1]) == 4):
                            result = "-".join(regex)
                            data[search][i] = remove_word(text, word)
                            data["zip"] = data["zip"] + [result]
                                
        #Remove Duplicates
        for field in data:
            if not data[field]:
                data[field] = None
            else:
                removeDuplicates = []
                for item in data[field]:
                    if item not in removeDuplicates:
                        removeDuplicates.append(item)
                data[field] = removeDuplicates

                

output_data = input_data

output_file = open('output.json', 'w')
json.dump(output_data, output_file, indent=4, ensure_ascii=False)
output_file.close()