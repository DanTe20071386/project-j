import requests
r = requests.get('https://en.wikipedia.org/wiki/History_of_Python')
print (r)
print (type(r))
print (r.status_code)
print (r.url)
print (r.text)
print ('path' in r.text)

import bs4
data = r.text
soup = bs4.BeautifulSoup(data)
print (soup)
soup.select('title')
t = soup.select('title')
print (t)
print (t[0])
print (type(t[0]))
title = t[0]
print(title.get_text())
print (title.get_text())
t = soup.select('h1')
print (t)
t = soup.select('li')
print (t)
print (len(t))
