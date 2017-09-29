>>> from bs4 import BeautifulSoup
>>> import urllib.request
>>> import re
>>> def crawler(url):
	webpage_content = urllib.request.urlopen(url)
	soup = BeautifulSoup(webpage_content, 'html.parser')
	for link in soup.find_all('a'):
		print(link.get('href'))
		
>>> crawler("http:strathmore.edu")
