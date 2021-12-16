import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1437881.xml'
html = urllib.request.urlopen(url, context=ctx).read().decode()
xml = ET.fromstring(html)
# print(xml)
results = xml.findall("comments/comment")
print(results)
sum = 0
for element in results:
    sum += int(element.find("count").text)
print(sum)
