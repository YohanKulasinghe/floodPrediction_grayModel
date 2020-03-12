# Flood Forcasting - Gray Model (1,1)

Grey forecast can be used to predict behavior of non-linear time series. This is a non-statistical forecasting method that is particularly effective when the number of observations is insufficient.

This Project contains two approches for implement gray model.

    1. Project with Angular frontend and flask(python) backend using gray 1.1 model 
    2. Full python project to predict flood using gray 1.1 model.

**Here How to Run Angular Project**

(You need only two folder to run _grayModelAPI_ and _floodprediction_. (Other contents for further referance if needed)

Clone the repo. 
```
git clone https://github.com/YohanKulasinghe/floodPrediction_grayModel.git
```

From root folder run followings (Root folder - floodForcasting)
```
cd floodForcasting
npm install
ng serve
```

From root folder run followings (Root folder - grayModel)
```
cd grayModel
pip install Flask
pip install -U flask-cors
pip install flask-restful
pip install flask-jsonpify
pip install matplotlib
pip install pandas
pip install xlrd
python run model.py
```

You will find a tab in nav bar to navigate prediction Precision checker.

https://colab.research.google.com/drive/1pLc1RD-NyBu4xamPgRY5u5A7W6whqpnv 

**Here How to Run Python Project**

(You need only one folder to run _completePython_. (Other contents for further referance if needed)

Clone the repo. 
```
git clone https://github.com/YohanKulasinghe/floodPrediction_grayModel.git
```

From root folder run following (root folder - completePython)
```
python fulPythonProject.py
```

**Other Content**

_Corrilation_ folder contains the proof of rainfall and water level is having
positive corrilation 

```
cd in to correlation folder and execute following line 
python fulPythonProject.py
```

_Comparrision_ folder contains the graph shows waterlevel and rainfall fluctuation 
 
```
cd in to Comparrision folder and execute following line
python comparison.py
```