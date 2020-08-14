import grequests
import os

keywords = [
    'obit',
    'death note',
    'death notice',
    'funeral'
]

os.chdir(os.getcwd() + '/files/CheckSites')

Sites_file = open('Sites.txt', 'r')
urls = []
for url in Sites_file:
    urls.append(url.split('\n')[0])
Sites_file.close()

FoundObits = []
NoObits = []
noResponse_counter = 0
FoundObits_counter = 0
NoObits_counter = 0

responses = grequests.map((grequests.get(url, timeout=100) for url in urls))

for response in responses:
    if response is None:
        noResponse_counter = noResponse_counter + 1
        continue
    source = response.content
    url = response.url
    foundWords = []
    if any(word in source for word in keywords):
        for word in keywords:
            if word in source:
                foundWords.append(word)
        FoundObits.append(url + '\n   ' + str(foundWords) + '\n')
        FoundObits_counter = FoundObits_counter + 1
    else:
        NoObits.append(url)
        NoObits_counter = NoObits_counter + 1

print ('\n================================')
print ('Found '+str(FoundObits_counter)+' site(s) with obituaries')
print ('Found '+str(NoObits_counter)+' site(s) with no obituaries')
print ('Couldn\'t connect to '+str(noResponse_counter)+' site(s)')
print ('================================')


FoundObits_file = open('FoundObits.txt', 'w')
for url in FoundObits:
    FoundObits_file.write(url+'\n')
FoundObits_file.close()

NoObits_file = open('NoObits.txt', 'w')
for url in NoObits:
    NoObits_file.write(url+'\n')
NoObits_file.close()
