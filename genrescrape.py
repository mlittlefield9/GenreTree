import requests
import csv
import httplib
import urllib2
from BeautifulSoup import BeautifulSoup


def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner

httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)


httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
url = 'http://rateyourmusic.com/rgenre/'

response = requests.get(url)


html = response.content

soup = BeautifulSoup(html)
divcontent = soup.find('div', attrs={'id': 'content'})


"""
Grab each one with either the style background string or A tag with title
"""

i = 1;

for categoryOne in divcontent.findAll('div', attrs={'style': 'background:#f8f8f8;border:#bbb 1px solid;padding:6px;margin:10px;'})
	print categoryOne.prettify


#print divcontent.prettify()



"""
Name, Description, children

list_of_rows = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./inmates.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)
"""