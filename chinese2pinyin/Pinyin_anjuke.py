# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:41:30 2013

@author: 子怿
"""

from anjuke import pinyin
import xlrd

def print_pinyin(name):
	converter = pinyin.Converter()
	converter.load_word_file('chars.txt')
	firstname_pool = converter.convert(name, fmt='fl', sc=False, pp=False)
	#fmt:df,tn,fl;
	#sc-False:no space,True:have space

#	result = converter.convert(name)
#	name_pool = result.split(" ")
#	firstname_pool = map(lambda x:x[0],name_pool)
	return firstname_pool

def print_pinyin_with_tone(name):
	converter = pinyin.Converter()
	converter.load_word_file('chars.txt')
#	result = converter.convert(name)
	firstname_pool_withtone = converter.convert(name, fmt='tn', sc=False, pp=False)#df,tn,fl
	return firstname_pool_withtone

def get_excel():
	name_pool = []
	data = xlrd.open_workbook('connection.xlsx')
	table = data.sheet_by_name(u'Sheet1')#通过名称获取
	begin = 0
	end = len(table.col_values(0))
	people_name = table.col_values(0)[begin:end]
	for p in people_name:
#		print p
		name_pool.append(p)
	return name_pool

def name_score(name):
	score = 0
	for i in name:
		if i in 'xyz':
			score += 1
	return score

def readexcel_translate(name):
#	name = get_excel()
	for i in xrange(len(name)):
		if name[i] != '':
			print name[i],print_pinyin_with_tone(name[i]),name_score(print_pinyin(name[i]))


name = get_excel()
#for i in name:
#	print print_pinyin(i)

readexcel_translate(name)