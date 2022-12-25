# Day 3

# Lvl 1
print("Lvl 1")
print("====================")
umur = 19
tinggi = 171.5
comp = (2j +5)

alas = float(input("Masukkan alas: "))
tinggi = float(input("Masukkan tinggi: "))
luas = float((alas*tinggi/2))
print ("==============")
print(luas)

a = float(input("Masukkan sisi A: "))
b = float(input("Masukkan sisi B: "))
c = float(input("Masukkan sisi C: "))
Keliling = a+b+c
print ("==============")
print(Keliling)

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
LuasPersegiPanjang = panjang*lebar
KelilingPersegiPanjang = 2*(panjang+lebar)
print("======================")
print ('Luas persegi panjang: %0.2f' %LuasPersegiPanjang)
print ('Keliling persegi panjang: %0.2f' %KelilingPersegiPanjang)

r = float(input("Masukkan jari-jari: "))
pi = 3.14
LuasLingkaran = pi*r*r
KelilingLingkaran=pi*r*2
print ("==============================")
print ('Luas LIngkaran: %0.2f' %LuasLingkaran)
print ('Keliling Lingkaran: %0.2f' %KelilingLingkaran)

# Lvl 2
print("====================")
print("Lvl 2")
print("====================")

x= int(input("input x: "))
y = (2*(x) -2)
print("y = (2*(x) -2)")
print("y = %0.2f" %y)


import numpy as np
print ("point 1 = (2, 2)")
print ("point 2 = (6, 10)")
point1 = np.array([2,2])
point2 = np.array([6, 10])
D = np.linalg.norm(point2-point1)
print("D = %0.2f" %D)
