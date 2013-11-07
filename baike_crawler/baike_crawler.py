# -*- coding: utf-8 -*-
"""
Created on Mon Jun 03 22:02:24 2013

@author: Mars
"""
import urllib
import re
from bs4 import BeautifulSoup,SoupStrainer

#############
def GetUrl(url):
	page = urllib.urlopen(url)
	data = page.read()
	return data
#############
def GetBody(keyword):
	#keyword=c2u(keyword)
	url = 'http://www.baidu.com/s?wd=%s' % keyword
	bodydata = GetUrl(url)	
	linksToList = SoupStrainer('a', href=re.compile('http://www.baidu.com/link?'))
	titles = [tag for tag in BeautifulSoup(bodydata, parse_only=linksToList)]
	link = titles[0]['href']
	#print link
	msg = GetUrl(link)
	name = 'writer/'+keyword+'.html'
	name = name.replace("\n","")
	file = open(name,'w')
	file.write(msg)
	file.close()

	
for KeyWord in open('writer.txt'):
	print KeyWord + u'——Getting news on Baidu Baike now…………'
	GetBody(KeyWord)
	print u'Done……Next……'
