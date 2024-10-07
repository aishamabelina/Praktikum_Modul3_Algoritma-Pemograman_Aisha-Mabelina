#NAMA : AISHA MABELINA
#NIM : 065002400026 

#Latihan Pertama
print("=============Selamat datang di Segitiga Detektor=============")

a = int(input("Isi sisi a: "))
b = int(input("Isi sisi b: "))
c = int(input("Isi sisi c: "))


if a == b == c:
  print("Jenis segitiga : Segitiga Sama Sisi")
elif a == b or a == c or b == c:
  print("Jenis segitiga : Segitiga Sama Kaki")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
  print("Jenis segitiga : Segitiga Siku-Siku")
elif a+b<= c or a + c <= b or b + c <= a:
   print ("Jenis segitiga : Ini bukan merupakan segitiga")
else:
  print("Jenis segitiga : Segitiga Sembarang")


print("===============Terima kasih================")



