# Ekspresi Logika
usia = 20
punya_ktp = True

bisa_masuk = (usia >= 18) and punya_ktp
print("Apakah bisa masuk?", bisa_masuk)  # True

# Ekspresi Keanggotaan
daftar_nama = ["Ali", "Budi", "Citra"]
nama = "Budi"

ada_dalam_daftar = nama in daftar_nama
print("Apakah Budi ada dalam daftar?", ada_dalam_daftar)  # True
