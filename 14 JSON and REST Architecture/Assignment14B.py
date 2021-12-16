import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = 'Indian Institute of Technology Kharagpur India'

params = dict()
params['address'] = address
params['key'] = api_key
url = serviceurl + urllib.parse.urlencode(params)

# print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
# print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)
    exit()

# print(json.dumps(js, indent=4))
print(js['results'][0]['place_id'])
