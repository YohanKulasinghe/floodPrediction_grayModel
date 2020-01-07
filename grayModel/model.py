from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import matplotlib.pyplot as plt
import numpy as np
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

@app.route('/getAccumilatedData',methods =['POST'])
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

if __name__ == '__main__':
    app.run(debug=True)

