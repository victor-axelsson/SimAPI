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

import pickle
import os.path
import numpy as np

class Cache: 

	def pickleIt(self, variable, name):
		pickle.dump(variable, open( name, "wb" ))

	def loadPickle(self, name):
		return pickle.load(open( name, "rb" ))

	def loadIfExists(self, name):
		if os.path.isfile(name):
			return self.loadPickle(name), True
		else:
			return None, False

	def loadNPIfExists(self, name):
		if os.path.isfile(name):
			return np.load(name), True
		else:
			return None, False

	def lazyCache(self, name, callable, args=None):
		if os.path.isfile(name):
			return self.loadPickle(name), True
		else:
			data = callable(**args)
			self.pickleIt(data, name)
			return data, False
