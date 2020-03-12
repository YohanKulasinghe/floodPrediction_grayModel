from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import xlrd

loc = ("relation.xlsx")
b_rainfall = []
b_temp = []
b_evaporation = []
b_waterlevel = []

c_rainfall = []
c_waterlevel = []

k_rainfall = []
k_temp = []
k_evaporation = []

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Get Bathalegoda Data
for i in range(sheet.nrows):
    b_rainfall.append(sheet.cell_value(i, 1))

for i in range(sheet.nrows):
    b_temp.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    b_evaporation.append(sheet.cell_value(i, 3))

for i in range(sheet.nrows):
    b_waterlevel.append(sheet.cell_value(i, 4)) 

# Get Chilaw Data
for i in range(sheet.nrows):
    c_rainfall.append(sheet.cell_value(i, 7)) 

for i in range(sheet.nrows):
    c_waterlevel.append(sheet.cell_value(i, 8))

# Get Kurunagala Data
for i in range(sheet.nrows):
    k_rainfall.append(sheet.cell_value(i, 10))

for i in range(sheet.nrows):
    k_temp.append(sheet.cell_value(i, 11))

for i in range(sheet.nrows):
    k_evaporation.append(sheet.cell_value(i, 12))


# Plot Bathalegoda Data 
pyplot.subplot(131)
pyplot.scatter(b_rainfall, b_temp)
pyplot.xlabel('Bathalegoda_Rainfall')
pyplot.ylabel('Bathalegoda_Temperature')

pyplot.subplot(132)
pyplot.scatter(b_rainfall, b_evaporation)
pyplot.xlabel('Bathalegoda_Rainfall')
pyplot.ylabel('Bathalegoda_Evaporation')

pyplot.subplot(133)
pyplot.scatter(b_rainfall, b_waterlevel)
pyplot.xlabel('Bathalegoda_Rainfall')
pyplot.ylabel('Bathalegoda_Waterlevel')
pyplot.show()

# Plot Kurunagala Data
pyplot.subplot(131)
pyplot.scatter(k_rainfall, k_temp)
pyplot.xlabel('Kurunagala_Rainfall')
pyplot.ylabel('Kurunagala_Evaporation')

pyplot.subplot(132)
pyplot.scatter(k_rainfall, k_evaporation)
pyplot.xlabel('Kurunagala_Rainfall')
pyplot.ylabel('Kurunagala_Waterlevel')
pyplot.show()

# Plot Chilaw Data
pyplot.subplot(131)
pyplot.scatter(c_rainfall, c_waterlevel)
pyplot.xlabel('Chilaw_Rainfall')
pyplot.ylabel('Chilaw_WaterLevel')
pyplot.show()

