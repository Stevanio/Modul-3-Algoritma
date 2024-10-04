def jenis_segitiga(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        # Cek apakah segitiga sama sisi
        if a == b == c:
            return "Segitiga Sama Sisi"
        elif a == b or b == c or a == c:
            return "Segitiga Sama Kaki"
        elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
            return "Segitiga Siku-Siku"
        else:
            return "Segitiga Sembarang"
    else:
        return "Bukan Segitiga"

a = float(input("Masukkan panjang sisi pertama: "))
b = float(input("Masukkan panjang sisi kedua: "))
c = float(input("Masukkan panjang sisi ketiga: "))

print(jenis_segitiga(a, b, c))
