from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from matplotlib import pyplot
import xlrd

loc = ("2007-2012.xlsx")
jan_rain = []
feb_rain = []
mar_rain = []
apr_rain = []
may_rain = []
jun_rain = []
jul_rain = []
aug_rain = []
sep_rain = []
oct_rain = []
nov_rain = []
dec_rain = []

jan_wl = []
feb_wl = []
mar_wl = []
apr_wl = []
may_wl = []
jun_wl = []
jul_wl = []
aug_wl = []
sep_wl = []
oct_wl = []
nov_wl = []
dec_wl = []

month = [2007,2008,2009,2010,2011,2012]

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

# Get monthly rain Data
for i in range(sheet.nrows):
    jan_rain.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    feb_rain.append(sheet.cell_value(i, 6))

for i in range(sheet.nrows):
    mar_rain.append(sheet.cell_value(i, 10))

for i in range(sheet.nrows):
    apr_rain.append(sheet.cell_value(i, 14))

for i in range(sheet.nrows):
    may_rain.append(sheet.cell_value(i, 18))

for i in range(sheet.nrows):
    jun_rain.append(sheet.cell_value(i, 22))

for i in range(sheet.nrows):
    jul_rain.append(sheet.cell_value(i, 26))

for i in range(sheet.nrows):
    aug_rain.append(sheet.cell_value(i, 30))

for i in range(sheet.nrows):
    sep_rain.append(sheet.cell_value(i, 34))

for i in range(sheet.nrows):
    oct_rain.append(sheet.cell_value(i, 38))

for i in range(sheet.nrows):
    nov_rain.append(sheet.cell_value(i, 42))

for i in range(sheet.nrows):
    dec_rain.append(sheet.cell_value(i, 46))

# Get monthly waterlevel Data
for i in range(sheet.nrows):
    jan_wl.append(sheet.cell_value(i, 3))

for i in range(sheet.nrows):
    feb_wl.append(sheet.cell_value(i, 7))

for i in range(sheet.nrows):
    mar_wl.append(sheet.cell_value(i, 11))

for i in range(sheet.nrows):
    apr_wl.append(sheet.cell_value(i, 15))

for i in range(sheet.nrows):
    may_wl.append(sheet.cell_value(i, 19))

for i in range(sheet.nrows):
    jun_wl.append(sheet.cell_value(i, 23))

for i in range(sheet.nrows):
    jul_wl.append(sheet.cell_value(i, 27))

for i in range(sheet.nrows):
    aug_wl.append(sheet.cell_value(i, 31))

for i in range(sheet.nrows):
    sep_wl.append(sheet.cell_value(i, 35))

for i in range(sheet.nrows):
    oct_wl.append(sheet.cell_value(i, 39))

for i in range(sheet.nrows):
    nov_wl.append(sheet.cell_value(i, 43))

for i in range(sheet.nrows):
    dec_wl.append(sheet.cell_value(i, 47))

fig, ax = pyplot.subplots()
pyplot.xlabel('Year')
pyplot.ylabel('Rainfall')
ax.plot(month,jan_rain, label="January")
ax.plot(month,feb_rain, label="February")
ax.plot(month,mar_rain, label="March")
ax.plot(month,apr_rain, label="April")
ax.plot(month,may_rain, label="May")
ax.plot(month,jun_rain, label="June")
ax.plot(month,jul_rain, label="July")
ax.plot(month,aug_rain, label="August")
ax.plot(month,sep_rain, label="September")
ax.plot(month,oct_rain, label="October")
ax.plot(month,nov_rain, label="November")
ax.plot(month,dec_rain, label="December")
ax.legend()


fig, ax = pyplot.subplots()
pyplot.xlabel('Year')
pyplot.ylabel('WaterLevel')
ax.plot(month,jan_wl, label="January")
ax.plot(month,feb_wl, label="February")
ax.plot(month,mar_wl, label="March")
ax.plot(month,apr_wl, label="April")
ax.plot(month,may_wl, label="May")
ax.plot(month,jun_wl, label="June")
ax.plot(month,jul_wl, label="July")
ax.plot(month,aug_wl, label="August")
ax.plot(month,sep_wl, label="September")
ax.plot(month,oct_wl, label="October")
ax.plot(month,nov_wl, label="November")
ax.plot(month,dec_wl, label="December")
ax.legend()
pyplot.show()