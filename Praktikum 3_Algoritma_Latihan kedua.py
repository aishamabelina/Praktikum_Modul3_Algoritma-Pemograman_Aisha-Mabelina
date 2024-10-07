#NAMA : AISHA MABELINA 
#NIM : 065002400026

import math
print("=====Selamat Datang di Program Mencari Akar Persamaan Kuadrat dan Determinan=====")
a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

if a == 0:
    print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")
else: 
    D = b**2 - 4*a*c
    print(f"Persamaan kuadrat {a}x^2 + {b}x + {c}")
    print(f"Determinan nya = {D}")
    
    if D > 0: 
        akarx1 = (-b + math.sqrt(D)) / (2*a)
        akarx2 = (-b - math.sqrt(D)) / (2*a)
        print("Memiliki Akar Berbeda.")
        print(f"Akar x1 = {akarx1}")
        print(f"Akar x2 = {akarx2}")
    elif D == 0:
        akar = -b / (2*a)
        print("Merupakan Akar Kembar.")
        print(f"Akar = {akar}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        print("Merupakan Akar Imaginer.")
        print(f"Akar x1 = {real_part} + {imaginary_part}i")
        print(f"Akar x2 = {real_part} - {imaginary_part}i")

    


