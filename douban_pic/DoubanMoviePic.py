# -*- coding: utf-8 -*-
"""
Created on Sat Jun 01 09:54:21 2013

@author: Mars
"""
import urllib
import re
import os
from bs4 import BeautifulSoup, SoupStrainer

#############
def GetUrl(url):
	page = urllib.urlopen(url)
	data = page.read()
	return data
#############
def Label(keyword):
	url = 'http://www.douban.com/search?q=%s' % keyword
	data = GetUrl(url)
	movies = [p for p in BeautifulSoup(data).findAll('div',{"class":'title'})]
	return movies[0].a['href']
#############
def GetBody(url):
	movieset = set()
	url = url + 'all_photos'
	data = GetUrl(url)
	linksToList = SoupStrainer('a', href=re.compile('movie.douban.com/photos/photo'))
	titles = [tag for tag in BeautifulSoup(data, parse_only=linksToList)]
	for t in titles:
		movienum = t['href'][37:47]
		movieset.add(movienum)
	return movieset
#############
def DownPic(movieset):
	temp = sorted(movieset)
	for i in range(len(temp)):
		file_name = temp[i] + '.jpg'
		url = 'http://img4.douban.com/view/photo/photo/public/p' + temp[i] + '.jpg'
		print file_name
		dest_dir = os.path.join(path,file_name)
		urllib.urlretrieve(url,dest_dir)

if __name__ == '__main__':
	path = r'Pic'
	keyword = '勇敢传说'
	g = repr(keyword)
	g = g.upper().replace("\\X","%")
	DownPic(GetBody(Label(g)))
