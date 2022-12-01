# REGRESI LINEAR

import numpy as np                                    #untuk simbol-simbol
from sklearn.linear_model import LinearRegression     #memanggil library regresi linear

#database
#x = Data, y = target
x = [[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]] 
y = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]               #x dikali 2

regr = LinearRegression().fit(x,y)                    #untuk fitting grafik
regr.score(x, y)                                      #untuk menentukan grafik

#data uji
predict = np.array([[10]])                            #nilai yang di prediksi

#menampilkan data prediksi (menampilkan karakter)
print ("Prediksi") 
print ("input = ", predict)
print ("Output =", regr.predict(predict))
