from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import xlrd

rainfall = []
waterlevel = []

loc = ("comparison.xlsx")

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    rainfall.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    waterlevel.append(sheet.cell_value(i, 3))

fig, ax = pyplot.subplots()
ax.plot(rainfall, label="rainfall")
ax.plot(waterlevel, label="waterlevel")
ax.legend()

pyplot.show()

