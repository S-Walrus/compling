import requests
import re

#text = requests.get("https://en.wikipedia.org/wiki/Special:Random").text

with open('page.html') as f:
    text = f.read()

res = {}

res['header'] = re.search(r'id="firstHeading".*?>(.*?)<', text).group(1)
res['table'] = [re.search(r'<th scope="row">(.*?)<\/th>', item).group(1) + '   :::   ' + re.search(r'<td>(.*?)<\/td>', item).group(1) \
    for item in re.findall(r'<tr>(.*?)<\/tr>', re.search(r'<table class="infobox vcard".*?>.*?<tbody>(.*?)<\/tbody>', text).group(1)) \
    if re.search(r'<th scope="row">(.*?)<\/th>', item) and re.search(r'<td>(.*?)<\/td>', item)]

res['table'] = [item for item in res['table'] if len(item) < 200]

print(res['table'])
