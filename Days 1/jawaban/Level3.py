#Tuliskan contoh dari tipe data yang berbeda seperti Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set dan Dictionary.
#Tentukan jarak Euclidian antara (2, 3) dan (10, 8)

#1

#Integer:
print (10)
#Float: 
print (3.14)
#Complex: 
print (1+2j)
#String: 
print ("Spectre")
#Boolean: 
print (True)
#List: 
A = [1, 4, 6,]
#Tuple: 
T = ("Spectre", 1, "Solitude", 2)
#Set: 
S = ([2, 4, 6, 8, 10])

#Dictionary:
Dct = {1:'Spectre', 2:'Solitude'}

#2

import numpy as np
point1 = np.array([2,3])
point2 = np.array([10, 8])
D = np.linalg.norm(point2-point1)
print(D)

