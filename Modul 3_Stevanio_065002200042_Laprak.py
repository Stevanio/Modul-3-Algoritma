import math

def akar_persamaan_kuadrat(a, b, c):

  diskriminan = b**2 - 4*a*c

  if a == 0:
    print("Bukan merupakan persamaan kuadrat, karena nilai A = 0")
    return None

  elif diskriminan > 0:
 
    x1 = (-b + math.sqrt(diskriminan)) / (2*a)
    x2 = (-b - math.sqrt(diskriminan)) / (2*a)
    print("Memiliki Akar Berbeda")
    print("Akar x1 =", x1)
    print("Akar x2 =", x2)

  elif diskriminan == 0:
    x = -b / (2*a)
    print("Merupakan Akar Kembar")
    print("Akar =", x)

  else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-diskriminan) / (2*a)
    print("Merupakan Akar Imajiner")
    print("Akar x1 =", complex(real_part, imaginary_part))
    print("Akar x2 =", complex(real_part, -imaginary_part))

a = float(input("Masukkan nilai A: "))
b = float(input("Masukkan nilai B: "))
c = float(input("Masukkan nilai C: "))

print("Persamaan kuadrat", a, "x^2 +", b, "x +", c)

diskriminan = b**2 - 4*a*c
print("Determinanya =", diskriminan)

akar_persamaan_kuadrat(a, b, c)
