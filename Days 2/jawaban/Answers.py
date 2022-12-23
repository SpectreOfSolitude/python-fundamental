#Hari ke-2: Fundamental Python

## Lvl 1
nama = "Akasyah"
jurusan = "Ilmu Komputer"
angkatan = 2021
umur = 19
asal_daerah = "DKI Jakarta"
money_amount = 500000
is_mahasiswa = True
is_alien = False
MoreFacts = ("Anak Tunggal", "Single", "Loves Dota")

## Lvl 2
print (type(nama))
print (type(jurusan))
print (type(angkatan))
print (type(umur))
print (type(asal_daerah))
print (type(money_amount))
print (type(is_mahasiswa))
print (type(is_alien))
print (type(MoreFacts))

print (len(nama))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two * num_one
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one//num_two

nama = input("input nama: ")
print ("Nama Baru: "+nama)
umur = input("input umur: ")
print ("Umur Baru: "+umur)
asal_daerah = input("input asal daerah: ")
print ("Daerah baru: "+asal_daerah)

radius = 30.0
pi = 3.14

_area_of_circle_ = pi * radius * radius
_circum_of_circle_ = pi*radius*2
print(_area_of_circle_)
print(_circum_of_circle_)

radius = input("input radius: ")
_area_of_circle_ = pi * radius * radius
print (_area_of_circle_)