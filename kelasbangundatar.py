import math

class BangunDatar:
    def hitung_luas(self):
        pass

    def hitung_keliling(self):
        pass


class Persegi(BangunDatar):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi * self.sisi

    def hitung_keliling(self):
        return 4 * self.sisi


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


class Lingkaran(BangunDatar):
    def __init__(self, r):
        self.r = r

    def hitung_luas(self):
        return math.pi * self.r ** 2

    def hitung_keliling(self):
        return 2 * math.pi * self.r


# Program utama
print("PILIH BANGUN DATAR")
print("1. Persegi")
print("2. Persegi Panjang")
print("3. Lingkaran")

pilihan = int(input("Masukkan pilihan: "))

if pilihan == 1:
    sisi = int(input("Masukkan sisi: "))
    obj = Persegi(sisi)

elif pilihan == 2:
    p = int(input("Panjang: "))
    l = int(input("Lebar: "))
    obj = PersegiPanjang(p, l)

elif pilihan == 3:
    r = int(input("Jari-jari: "))
    obj = Lingkaran(r)

else:
    print("Pilihan tidak valid")
    exit()

print("Luas:", obj.hitung_luas())
print("Keliling:", obj.hitung_keliling())