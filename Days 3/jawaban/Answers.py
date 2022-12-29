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
#1
print("====================")
print("Lvl 2")
print("====================")

print(("y = 2x - 2"))
y2 = 2
x2 = 1
y1 = 0
x1 = 0
m = ((y2-y1)/(x2-x1)) 
print("slope = %0.2f" %m)
ycut = -2
print("y intercept: %0.2f" %ycut)
xcut = 1
print("x intercept: %0.2f" %xcut)

#2
print("====================")
print ("point 1 = (2, 2)")
print ("point 2 = (6, 10)")
x1 = 2
x2 = 6
y1 = 2
y2 = 10
m = ((y2-y1)/(x2-x1))
d = ((y2-y1)**2)+((x2-x1)**2)
print("Slope = %0.2f" %m)
print ("Euclidian Distance = %0.2f" %d)

#3
print ("Slope in task 1 == slope in task 2")

#4
print ("===============================")
print ("y = x^2 +6x + 9")