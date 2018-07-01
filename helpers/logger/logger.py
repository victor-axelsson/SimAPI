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

import time
import datetime
import psutil

class Logger: 

	longRunning = False

	def __call__(self, message):
		self.log(message)

	def startLongRunningLog(self, totalIterations, tick):
		self.totalIterations = totalIterations
		self.tick = tick
		self.longRunning = True
		self.counter = 0
		self.ts = time.time()

	def endLongRunningLog(self):
		self.totalIterations = 0
		self.tick = 0
		self.longRunning = False
		self.counter = 0
		self.ts = time.time()

	def _logLongRunning(self, message):
		if(self.counter % self.tick == 0):
			diff = time.time() - self.ts 
			msPerTick = diff / self.tick
			remaining = msPerTick * (self.totalIterations - self.counter)
			self.ts = time.time()
			mem = psutil.virtual_memory().percent
			cpu = psutil.cpu_percent()

			print("{}, [CPU]=>{} [MEM]=>{} [ETA]=>{}, {}/{}=>{:.2} {}".format(datetime.datetime.fromtimestamp(self.ts).strftime('%Y-%m-%d %H:%M:%S'), cpu, mem, datetime.datetime.fromtimestamp(time.time() + remaining).strftime('%Y-%m-%d %H:%M:%S'), self.counter, self.totalIterations, self.counter / self.totalIterations, message))
		self.counter += 1

	def log(self, message):
		if(self.longRunning):
			self._logLongRunning(message)
		else:
			print("{} {}".format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'), message))
