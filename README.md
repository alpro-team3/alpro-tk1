# alpro-tk1
Project team-3 untuk tugas alpro ke-1

## Struktur Proyek

### 1. **Anggota A: Operator Aritmatika dan Penugasan**
**Nama:** [Isi nama Anggota A] </br>
**Nim:** [Isi nim Anggota A] </br>
**Branch:** `arith-assign` </br>

#### Deskripsi
Anggota A bertanggung jawab untuk memberikan contoh penggunaan:
- **Operator Aritmatika**: Penjumlahan, pengurangan, perkalian, pembagian, dan modulus.
- **Operator Penugasan**: Contoh seperti `+=`, `*=`, dll.

#### Contoh Kode
```python
# Ekspresi Aritmatika
hasil = (10 + 5) * 2 - 10 / 2
print("Hasil ekspresi aritmatika:", hasil)  # 25.0

# Ekspresi Penugasan
x = 7
x += 3
x *= 2
print("Hasil ekspresi penugasan:", x)  # 20
```

---

### 2. **Anggota B: Operator Perbandingan**
**Nama:** Muhammad Radja Rivaldi </br>
**Nim:** I.2410157 </br>
**Branch:** `compare` </br>

#### Deskripsi
Anggota B bertanggung jawab untuk memberikan contoh penggunaan:
- **Operator Perbandingan**: Contoh seperti `>`, `<`, `==`, `!=`, `>=`, dan `<=`.

#### Contoh Kode
```python
# Ekspresi Perbandingan
nilai_ujian = 85
nilai_minimal = 75

lulus = nilai_ujian >= nilai_minimal
print("Apakah lulus?", lulus)  # True

nilai_tinggi = nilai_ujian > 90
print("Apakah nilai sangat tinggi?", nilai_tinggi)  # False
```

---

### 3. **Anggota C: Operator Logika dan Keanggotaan**
**Nama:** [Isi nama Anggota C] </br>
**Nim:** [Isi nim Anggota C]  </br>
**Branch:** `logic-membership` </br>

#### Deskripsi
Anggota C bertanggung jawab untuk memberikan contoh penggunaan:
- **Operator Logika**: Contoh seperti `and`, `or`, dan `not`.
- **Operator Keanggotaan**: Contoh seperti `in` dan `not in`.

#### Contoh Kode
```python
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
```

---

## Cara Kerja

### Langkah Pengembangan
1. Setiap anggota membuat branch sesuai tugas masing-masing.
   - Anggota A: `arith-assign`
   - Anggota B: `compare`
   - Anggota C: `logic-membership`

2. Tambahkan contoh kode di branch masing-masing.
3. Lakukan commit dan push ke repository remote.
4. Setelah selesai, merge branch ke `main`.

### Menggabungkan Branch
Gunakan perintah berikut untuk menggabungkan branch:
```bash
git checkout main
git merge arith-assign
git merge compare
git merge logic-membership
git push origin main
```

## Catatan
- Harap memastikan kode telah diuji sebelum di-commit.
- Resolusi konflik dilakukan bersama jika terdapat perbedaan pada file yang sama.
