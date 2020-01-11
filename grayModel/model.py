from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import xlrd
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/')
def index():
    return jsonify("Gray Model (1,1) is up and running")


@app.route('/getrainfalldata')
def getRainData():
    loc = ("dataSource/AMBANPITIYA.xlsx")
    my_list = []

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        my_list.append(sheet.cell_value(i, 1))

    return jsonify(my_list)


@app.route('/getwaterleveldata')
def getWaterData():
    return jsonify("no Data Found")


@app.route('/getAccumilatedData', methods=['POST'])
def generateAccumilatedData():
    req = json.loads(request.data.decode())
    x1 = req['rowData']

    def accumulation(lis):
        total = 0
        for x in lis:
            total += x
            yield total

    accData = list(accumulation(x1))
    return jsonify(accData)


@app.route('/initializesModel', methods=['POST'])
def generateZvalue():
    req = json.loads(request.data.decode())
    accuData = req['accuData']
    rowData = req['rowData']

    def mean(AccumulatedRainfaillDatails):
        data = AccumulatedRainfaillDatails[0]
        for AccumulatedRainfaillData in AccumulatedRainfaillDatails:
            meanValue = (data + AccumulatedRainfaillData)/2
            data = AccumulatedRainfaillData
            yield meanValue

    z1 = [x * -1 for x in list(mean(accuData))]
    z1 = np.delete(z1, 0)

    # Create metrix with mean value and 1 
    B = pd.DataFrame({'0':z1})
    B['1']  = 1
    B_ = B.to_numpy()
    
    # Get transpose of metrix B
    B_t = B.transpose().to_numpy()

    # Expression 01 = B_t * B ( multiply metrix B and it transpose )
    E1_pre = B_t.dot(B_)
    E1 = np.linalg.inv(E1_pre)

    # Expression 02 = B_t * x0 (inverse)
    Xn = np.delete(rowData ,0)
    Xn_t = pd.DataFrame(data = Xn).to_numpy()

    E2 = B_t.dot(Xn_t)

    # Final = Expression1 * Expression 2
    final = E1.dot(E2)

    # Get A and B hat values
    a = final[0].item()
    b = final[1].item()

    hats = [a,b]

    return jsonify(hats)

if __name__ == '__main__':
    app.run(debug=True)
