"""
The MIT License (MIT)
Copyright (c) 2018 Victor Axelsson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
OR OTHER D
""" 

from helpers.file import textFile
from helpers.cache import Cache

class Distribution:
	dataFolder = None
	textFileReader = None
	cache = None
	wordlist = None

	def __init__(self, dataFolder):
		self.dataFolder = dataFolder
		self.textFileReader = textFile.TextFile()
		self.cache = Cache()
		self.calcDistribution()

	def _readDataFromDisk(self):
		return self.textFileReader.read_folder(self.dataFolder)

	def _readSortedList(self, data):
		items = {}
		for row in data:
			for col in row:
				if col not in items:
					items[col] = 0
				items[col] += 1


		itemList = []
		for item in items.keys():
			itemList.append({
				'item': item,
				'val': items[item]
			})
			
		return sorted(itemList, key=lambda k: k['val'], reverse=True)

	def _readWordList(self):
		wordlist = {}
		for i in range(len(self.sortedList)):
			item = self.sortedList[i]
			wordlist[item['item']] = i

		return wordlist

	def calcDistribution(self):
		data, wasCached = self.cache.lazyCache("distribution.pkl", self._readDataFromDisk, {})
		if wasCached:
			print("Loaded distribution from cache")

		items = {}
		for row in data:
			for col in row:
				if col not in items:
					items[col] = 0
				items[col] += 1


		itemList = []
		for item in items.keys():
			itemList.append({
				'item': item,
				'val': items[item]
			})
			
		self.sortedList, sortedWasCached = self.cache.lazyCache("sortedDist.pkl", self._readSortedList, {'data': data})
		if sortedWasCached:
			print("Loaded sortedList from cache")
		self.wordlist, wordListWasCached = self.cache.lazyCache("wordListDist.pkl", self._readWordList, {})
		if wordListWasCached:
			print("Loaded wordlist from cache")

	def getDistribution(self):
		return self.sortedList, self.wordlist
