# REGRESI POLINOMIAL

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import numpy as np                                        #untuk simbol-simbol


#database 
#x = data, y = Target 
x = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]] 
y = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]          #x dipangkat 2

#data uji 
predict = np.array([[40]])                        #nilai yang di prediksi 
poly = PolynomialFeatures(degree=2)               #ordo yang digunakan
x_=poly.fit_transform(x)                          #fitting prediksi sumbu
predict_ = poly.fit_transform(predict)            #fitting jenis regresi
regr = linear_model.LinearRegression()            #meregresi
regr.fit(x_,y)                                    #menentukan grafik

#menampilkan data prediksi 
print ("Prediksi")
print ("input = ", predict)
print ("Output =", regr.predict(predict_))
