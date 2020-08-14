import grequests
import os
from lxml import html
import json
import math


def get_xml(urls, timeout, concurrent_requests):
    total_requests = len(urls)
    num_of_requests = int(math.ceil(total_requests / float(concurrent_requests)))
    output = []
    for i in range(0, num_of_requests):

        lower = i * concurrent_requests
        upper = i * concurrent_requests + concurrent_requests

        if upper > total_requests:
            upper = total_requests
        print str(lower + 1) + " -> " + str(upper) + " (" + str(total_requests) + " Total Requests)"

        cycle = urls[lower:upper]

        responses = grequests.map((grequests.get(url, timeout=timeout) for url in cycle))
        for response in responses:
            try:
                source = response.content
                xml = html.fromstring(source)
                output.append(xml)
            except:
                print "Couldn't get XML"
    return output


def xpath(xml, xpath, join):
    if join is True:
        try:
            return ' '.join(xml.xpath(xpath))
        except:
            print "Couldn't join strings"
    else:
        try:
            return xml.xpath(xpath)
        except:
            print "Couldn't get XPATH"


def custom_code(xml):
    data = []
    hrefs = xpath(xml, "(//a)[position()>9]/@href", False)
    print hrefs
    # while len(hrefs) > 0:
    #     searches = []
    #     for href in hrefs:
    #         if ".htm" in href and href.count(".") == 1:
    #             searches.append("http://www.abyznewslinks.com/"+href)
    #             print "Searching " + "http://www.abyznewslinks.com/" + href
    #         else:
    #             data.append(href)
    #     xmls = get_xml(searches, 100, 5)
    #     new_hrefs = []
    #     for xml in xmls:
    #         new_hrefs.append(xpath(xml, "(//a)[position()>9]/@href", False))
    #     hrefs = new_hrefs





    # count = xpath(xml, "", False)
    # for i in range(0, len(count)):
        # pos = str(i)
    # data.append({
    #     "name":    xpath(xml, "//h1/text()", True),
    #     "address": xpath(xml, "//tr[2]/td/text()", True),
    #     "website": xpath(xml, "//tr[3]/td/a/@href", True),
    #     "city":    xpath(xml, "//tr[2]/td/a/text()", True),
    #     # "state":   xpath(xml, "", True),
    #     # "country": xpath(xml, "", True),
    #     "phone":   xpath(xml, "//tr[4]/td/text()", True)
    #     })
    #     # data.append(
    #     #     xpath(xml, "", True),
    #     # )
    return data


os.chdir(os.getcwd() + '/files/GetSites')

input_sites = open('input.txt', 'r')
lines = input_sites.readlines()
input_sites.close()


# ==================================================================================================================== #

# concurrentRequests = len(lines)
concurrentRequests = 5

# ==================================================================================================================== #

# totalRequests = len(lines)
#
# numOfRequests = int(math.ceil(totalRequests / float(concurrentRequests)))

data = []

responses = get_xml(lines, 20, 5)
print "Received Responses..."
print responses

for i in range(0, len(responses)):
    try:
        data = data + custom_code(responses[i])
        print str(i + 1) + "/" + str(len(responses))
    except:
        print str(i + 1) + "/" + str(len(responses)) + " Exception!"

# for x in range(0, numOfRequests):
#     lower = x * concurrentRequests
#     upper = x * concurrentRequests + concurrentRequests
#     if upper > totalRequests:
#         upper = totalRequests
#     print str(lower+1) + " -> " + str(upper) + " (" + str(totalRequests) + " Total Requests)"
#
#     urls = []
#     for i in range(lower, upper):
#         urls.append(lines[i].replace("\n", ""))
#
#     responses = get_xml(urls, 500)


output_sites = open('output.json', 'w')
json.dump(data, output_sites, indent=4)
output_sites.close()
