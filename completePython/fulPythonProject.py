import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math
import xlrd

loc = ("dataSource/ChilawData.xlsx")
x0_rainfall = []
x0_waterlevel = []

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    x0_rainfall.append(sheet.cell_value(i, 2))

for i in range(sheet.nrows):
    x0_waterlevel.append(sheet.cell_value(i, 3))

def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

x1_rainfall = list(accumu(x0_rainfall))
x1_waterlevel = list(accumu(x0_waterlevel))

def avg(lis):
  pre = lis[0]
  for x in lis:
      avgVal = (pre + x)/2
      pre = x
      yield avgVal

z1_rainfall = [x * -1 for x in list(avg(x1_rainfall))]
z1_waterlevel = [x * -1 for x in list(avg(x1_waterlevel))]

z1_rainfall = np.delete(z1_rainfall ,0)
z1_waterlevel = np.delete(z1_waterlevel ,0)

B_rainfall = pd.DataFrame({'0':z1_rainfall})
B_waterlevel = pd.DataFrame({'0':z1_waterlevel})

B_rainfall['1']  = 1
B_waterlevel['1']  = 1

B_rainfall_ = B_rainfall.to_numpy()
B_rainfall_t = B_rainfall.transpose().to_numpy()

B_waterlevel_ = B_waterlevel.to_numpy()
B_waterlevel_t = B_waterlevel.transpose().to_numpy()


E1_pre_rainfall = B_rainfall_t.dot(B_rainfall_)
E1_pre_waterlevel = B_waterlevel_t.dot(B_waterlevel_)


E1_rainfall = np.linalg.inv(E1_pre_rainfall)
E1_waterlevel = np.linalg.inv(E1_pre_waterlevel)

Xn_rainfall = np.delete(x0_rainfall ,0)
Xn_waterlevel = np.delete(x0_waterlevel ,0)

E2_rainfall = B_rainfall_t.dot(Xn_rainfall)
E2_waterlevel = B_waterlevel_t.dot(Xn_waterlevel)

parameter_rainfall = E1_rainfall.dot(E2_rainfall)
parameter_waterlevel = E1_waterlevel.dot(E2_waterlevel)


a_rainfall = parameter_rainfall.item(0)
b_rainfall = parameter_rainfall.item(1)

a_waterlevel = parameter_waterlevel.item(0)
b_waterlevel = parameter_waterlevel.item(1)

def dif_eq_rainfall(k):
  return (x0_rainfall[1] - (b_rainfall/a_rainfall)) * math.exp(-1*a_rainfall*(k-1)) + (b_rainfall/a_rainfall)

def dif_eq_waterlevel(k):
  return (x0_waterlevel[1] - (b_waterlevel/a_waterlevel)) * math.exp(-1*a_waterlevel*(k-1)) + (b_waterlevel/a_waterlevel)

K = 30
X_forecast_rainfall = dif_eq_rainfall(K) - dif_eq_rainfall(K-1)
X_forecast_waterlevel = dif_eq_waterlevel(K) - dif_eq_waterlevel(K-1)

#print(x0_rainfall[K])
print(X_forecast_rainfall)
#print(x0_waterlevel[K])
print(X_forecast_waterlevel)

if X_forecast_rainfall > 400.7 and X_forecast_waterlevel > 2.75:
    print("Be alert, there might be a flood situation")
else:
    print("Be Relax, No flood risk")


###################### Following is the model without extra logic (for referance only) ###################################

"""
loc = ("dataSource/ChilawData.xlsx")
x0 = []

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    x0.append(sheet.cell_value(i, 2))

def accumu(lis):
    total = 0
    for x in lis:
        total += x
        yield total

x1 = list(accumu(x0))

def avg(lis):
  pre = lis[0]
  for x in lis:
      avgVal = (pre + x)/2
      pre = x
      yield avgVal

z1 = [x * -1 for x in list(avg(x1))]

z1 = np.delete(z1 ,0)

B = pd.DataFrame({'0':z1})
B['1']  = 1

B_ = B.to_numpy()
B_t = B.transpose().to_numpy()

E1_pre = B_t.dot(B_)

E1 = np.linalg.inv(E1_pre)

Xn = np.delete(x0 ,0)

E2 = B_t.dot(Xn)

parameter = E1.dot(E2)

a = parameter.item(0)
b = parameter.item(1)

def dif_eq(k):
  return (x0[1] - (b/a)) * math.exp(-1*a*(k-1)) + (b/a)

K = 30
X_forecast_rainfall = dif_eq(K) - dif_eq(K-1)

print(x0[K])
print(X_forecast_rainfall) """

