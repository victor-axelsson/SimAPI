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
OR OTHER DEALINGS IN THE SOFTWARE.
"""

from flask import Flask
from flask import request
import sys
import json
from flask_cors import CORS, cross_origin

from helpers.data_analys import svd
from helpers.data_analys import distribution

#FLASK_APP=main.py flask run --port=6001 
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
sessionData = "./dataOut.json"

svd_truncated = svd.SVD(sessionData, "")
svd_truncated.runSvdOnJsonGraph(100, 200)

@app.route("/device")
def hello():
    return json.dumps(list(svd_truncated.getWordlist().keys()))

@app.route("/device/similar")
@cross_origin()
def getSimilarDevice():
	deviceName = request.args.get('device')
	threshold = float(request.args.get('threshold'))
	concepts = svd_truncated.u[svd_truncated.wl[deviceName]]
	device, bestRow, score, items = svd_truncated.getMostSimilarInU(concepts, threshold=threshold)

	return json.dumps({
		'devices': items,
		'score': score
	})


@app.route("/device/similar/compare", methods=['POST'])
@cross_origin()
def compareDeviceSimilarity():
	data = request.get_json()
	print(len(data['devices']))
	allScore = 0
	individualScores = []

	for i in range(len(data['devices']) -1):
		d1 = data['devices'][i]
		concepts_i = svd_truncated.u[svd_truncated.wl[d1]]

		for j in range(i +1, len(data['devices'])):
			d2 = data['devices'][j]
			concepts_j = svd_truncated.u[svd_truncated.wl[d2]]
			score = svd_truncated.cosineSimilarity(concepts_i, concepts_j)
			allScore += score
			individualScores.append({
				'd1': d1,
				'd2': d2,
				'score': score
			})

	score = 0
	if len(individualScores) > 0:
		score = float(allScore / len(individualScores))

	return json.dumps({
		'deviceScores': individualScores,
		'absoluteScore': allScore,
		'n_devices': len(data['devices']),
		'n_comparisons': len(individualScores),
		'sim_score': score,
		'diversity': 1 - score
	})

app.run(port=6001, threaded=True)
