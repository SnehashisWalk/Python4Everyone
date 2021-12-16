import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1437882.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None

if js is None:
    print("====Failure To Retrieve====")
    exit()

# print(json.dumps(js, indent=4))
sum=0
for item in js['comments']:
    sum+=item['count']
print(sum)
