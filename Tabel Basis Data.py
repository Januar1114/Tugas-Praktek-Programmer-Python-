import mysql.connector

# Koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_angka"
)

cursor = db.cursor()

# Menampilkan tabel data base
def tampil_data():
    cursor.execute("SELECT * FROM angka")
    data = cursor.fetchall()

    print("+----+----------+")
    print("| id | angka    |")
    print("+----+----------+")
    for d in data:
        print(f"| {d[0]:<2} | {d[1]:<8} |")
    print("+----+----------+")

print("Tabel Data Base")
tampil_data()


# Update kolom angka menjadi simbol angka
mapping = {
    "satu": 1, "dua": 2, "tiga": 3, "empat": 4,
    "lima": 5, "enam": 6, "tujuh": 7,
    "delapan": 8, "sembilan": 9, "sepuluh": 10
}

for kata, angka in mapping.items():
    cursor.execute("UPDATE angka SET angka=%s WHERE angka=%s", (angka, kata))
db.commit()

print("\nSETELAH DI UPDATE")
tampil_data()

# Sorting dan cek bilangan ganjil atau genap
cursor.execute("SELECT * FROM angka ORDER BY angka ASC")
data = cursor.fetchall()

print("\nSORTING DAN CEK BILANGAN GANJIL/GENAP")
print("+----+--------+---------+")
print("| id | angka  | status  |")
print("+----+--------+---------+")

for d in data:
    angka = int(d[1])
    status = "Genap" if angka % 2 == 0 else "Ganjil"
    print(f"| {d[0]:<2} | {angka:<6} | {status:<7} |")

print("+----+--------+---------+")

# Hapus bilangan ganjil 
cursor.execute("DELETE FROM angka WHERE angka % 2 != 0")
db.commit()

print("\nSETELAH BILANGAN GANJIL DI HAPUS")
tampil_data()
