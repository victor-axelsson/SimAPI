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

import numpy as np

class Wordlist:
	def getWordlist(self, data):
		items = set()
		for row in data:
			for col in row:
				items.add(col)

		wordlist = dict()
		reversedList = []

		counter = 0
		for item in items:
			wordlist[item] = counter
			reversedList.append(item)
			counter += 1

		return items, wordlist, reversedList

	def getWordlistFromGraph(self, data):
		allItems = {}
		for k in data:
			allItems[k] = 1
			for innerKey in data[k]:
				allItems[innerKey] = 1 

		items = np.array(list(allItems.keys()))

		reversedList = []
		itemsKeys = {}
		for i in range(len(items)):
			itemsKeys[items[i]] = i
			reversedList.append(items[i])

		return items, itemsKeys, reversedList