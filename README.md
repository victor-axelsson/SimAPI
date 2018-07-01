# About
This project is a tool built by Victor Axelsson as a part of the thesis *Collaborative Recommendations for Music Session Instrumentation - Contrasting Graph to ML Based Approaches*. The purpose of this application is to find latent factor similarities between entities. The API exposes the functionality of finding items that take a similar role in a session using an adjecency list. This is done by the following steps: 

- From the json adjecency list `dataOut.json` build a n x n sparse matrix where the rows are the start device and the columns are the end device. If you create item A then item B it means that on row A and column B there will be a 1. When this happens again, the number will be incemented. It can be though of as a markow chain with one step. 
- On the ajecency matrix M a truncated Singlar Value Decomposition [SVD](https://en.wikipedia.org/wiki/Singular-value_decomposition) will be performed  with the help of the python library [sklearn](http://scikit-learn.org/stable/index.html).
- The created matrices, U, v, vT and sigma will be cached to disk so that they don't have to be created every time the API gets a request. 
- When the API gets a request it will multiply U and sigma, find the index corresponding to the posted device and use the [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity) to find similar devices. 

You might need a lot of data before the results are starting to become good. Using only a small data set wil probably not give very effective similarity measurments. You might also need to tweek the dimensionality reduction into a number of dimensions that fits your case. 

## Licence
All souce code of this project is licenced under MIT licence. 

```
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
```

Should any souce code be missing the MIT licence header, please let me know and I will fix it. The motivation behind this licence is so that you can utilize this tool for your domain but no warranty is given since the software is provided "as is". 

# Setup 

Start by adding your data file into the **root of the project**. It should be named `dataOut.json`. Here is an example of it might look like. 

```
{
    "device1": {
        "device2": {
            "weight": 10
        },
        "device3": {
            "weight": 2
        }
    },
    "device2": {
        "device1": {
            "weight": 4
        },
        "device3": {
            "weight": 1
        }
    },
     "device3": {
        "device1": {
            "weight": 3
        }
    }
}
```

There might be some libraries that you will need to install with [pip](https://pypi.org/project/pip/). For this project **python3** is used. The specific packages and their versions used during development are: 

```
numpy==1.14.3
Flask_Cors==3.0.3
matplotlib==2.2.2
Flask==0.12.2
scipy==0.19.1
seaborn==0.8.1 [OPTIONAL]
psutil==5.4.3
scikit_learn==0.19.1
```

It is unlikely that you will need the exact versions and getting the latest version *should* be fine. 

- `cd <project folder root>`
- `pip3 install numpy`
- `pip3 install Flask_Cors`
- `pip3 install matplotlib`
- `pip3 install Flask`
- `pip3 install scipy`
- `pip3 install seaborn` [OPTIONAL]
- `pip3 install psutil`
- `pip3 install scikit_learn`

To start the application simply run: 

- `cd <project folder root>`
- `FLASK_APP=main.py flask run --port=6001` OR `python3 main.py`

When you get it working you should see some output that its building the M matrix and some output similar to this example: 

```
2018-06-30 15:16:21, [CPU]=>45.6 [MEM]=>64.5 [ETA]=>2018-06-30 15:17:31, 15100/16992=>0.89 Building graph matrix...
2018-06-30 15:16:25, [CPU]=>36.8 [MEM]=>64.5 [ETA]=>2018-06-30 15:17:29, 15200/16992=>0.89 Building graph matrix...
2018-06-30 15:16:28, [CPU]=>37.4 [MEM]=>64.3 [ETA]=>2018-06-30 15:17:30, 15300/16992=>0.9 Building graph matrix...
2018-06-30 15:16:32, [CPU]=>41.7 [MEM]=>64.5 [ETA]=>2018-06-30 15:17:30, 15400/16992=>0.91 Building graph matrix...
2018-06-30 15:16:36, [CPU]=>40.1 [MEM]=>64.9 [ETA]=>2018-06-30 15:17:30, 15500/16992=>0.91 Building graph matrix...
2018-06-30 15:16:39, [CPU]=>41.0 [MEM]=>65.1 [ETA]=>2018-06-30 15:17:31, 15600/16992=>0.92 Building graph matrix...
2018-06-30 15:16:43, [CPU]=>45.0 [MEM]=>65.0 [ETA]=>2018-06-30 15:17:31, 15700/16992=>0.92 Building graph matrix...
2018-06-30 15:16:47, [CPU]=>47.1 [MEM]=>65.2 [ETA]=>2018-06-30 15:17:33, 15800/16992=>0.93 Building graph matrix...
2018-06-30 15:16:51, [CPU]=>43.3 [MEM]=>65.2 [ETA]=>2018-06-30 15:17:30, 15900/16992=>0.94 Building graph matrix...
2018-06-30 15:16:54, [CPU]=>35.5 [MEM]=>65.2 [ETA]=>2018-06-30 15:17:29, 16000/16992=>0.94 Building graph matrix...
2018-06-30 15:16:58, [CPU]=>42.7 [MEM]=>65.3 [ETA]=>2018-06-30 15:17:30, 16100/16992=>0.95 Building graph matrix...
2018-06-30 15:17:01, [CPU]=>36.6 [MEM]=>65.3 [ETA]=>2018-06-30 15:17:29, 16200/16992=>0.95 Building graph matrix...
2018-06-30 15:17:06, [CPU]=>54.5 [MEM]=>66.4 [ETA]=>2018-06-30 15:17:35, 16300/16992=>0.96 Building graph matrix...
2018-06-30 15:17:09, [CPU]=>41.2 [MEM]=>66.5 [ETA]=>2018-06-30 15:17:31, 16400/16992=>0.97 Building graph matrix...
2018-06-30 15:17:13, [CPU]=>33.1 [MEM]=>66.6 [ETA]=>2018-06-30 15:17:30, 16500/16992=>0.97 Building graph matrix...
2018-06-30 15:17:16, [CPU]=>34.6 [MEM]=>66.1 [ETA]=>2018-06-30 15:17:30, 16600/16992=>0.98 Building graph matrix...
2018-06-30 15:17:20, [CPU]=>31.9 [MEM]=>66.1 [ETA]=>2018-06-30 15:17:30, 16700/16992=>0.98 Building graph matrix...
2018-06-30 15:17:23, [CPU]=>38.0 [MEM]=>65.9 [ETA]=>2018-06-30 15:17:30, 16800/16992=>0.99 Building graph matrix...
2018-06-30 15:17:27, [CPU]=>35.2 [MEM]=>65.9 [ETA]=>2018-06-30 15:17:30, 16900/16992=>0.99 Building graph matrix...
```

When the matrix M is build it will perform a truncated SVD on it with the help of some of the classes in the `helpers` folder. This might take a while so please have some patiance. The output looks something like this: 

```
2018-06-30 15:17:30 Factorization was not present, calculating... (Might take a while)
2018-06-30 15:17:30 Fitting the randomized_svd with 200 iterations and 100 components
```

At this point the application should have produced some cached files for you. 

- `device_device_adjecency.matrix`
- `sigma.bin`
- `u.bin`
- `v.bin`
- `vt.bin`

If you want to rebuild the matrix and redo the SVD it's safe to delete them and restart the API. 

# API
The easiest way to get started is by importing the `SimAPI.postman_collection.json` collection into [Postman](https://www.getpostman.com/). 

## Get all registered devices
Get all the available devices you can use in the API. 

```
GET localhost:6001/device
RESPONSE
[.... <devices> ....]
```

## Find session intra similarity
Find the diversity between different devices. The devices can be used to find the diversity of a session for example. 
```
POST localhost:6001/device/similar/compare
REQUEST
{
	"devices": ["<device 1>", "<device 2>", "<device n>"]
}
RESPONSE
{
    "deviceScores": [{"d1": <device 1>, "d2": <device 2>} ....], // Cathesian product take 2 (higly unefficient for larger set of devices) 
    "absoluteScore": 1.9320018247180752, 
    "n_devices": n, 
    "n_comparisons": n * (n - 1) / 2, 
    "sim_score": 0.6440006082393585, 
    "diversity": 0.35599939176064155
}
```

## Find similar devices
Find devices that are similar to the one given. You should set a threshold where an item is considered similar. The domain for the threshold is [-1, 1] where -1 is as opposite one can be, 1 is identical and 0 is neither similar or dissimilar. 

```
GET http://localhost:6001/device/similar?device=<device>&threshold=0.85
RESPONSE
{
    "devices": [{
        "item": "<device>", 
        "score": 0.8586729859578377
    }, {
        "item": "<device>",
        "score": 1.0000000000000002
    }, {
        "item": ""<device>", 
        "score": 0.8575312677965277
    }, {
        "item": "<device>", 
        "score": 0.8955778236030165
    }, {
        "item": ""<device>", 
        "score": 0.871651609543985
    }, {
        "item": ""<device>a", 
        "score": 0.8699710664546415
    }], 
    "score": 1.0000000000000002 // The best score 
}
```
