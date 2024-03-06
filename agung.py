nama = input("Masukkan nama anda: ")
hari_kerja = int(input("Masukkan jumlah hari kerja: "))
hari_kerja_perbulan = 25
gaji = 100000

if hari_kerja > hari_kerja_perbulan:
    lembur = (hari_kerja - hari_kerja_perbulan) * 2000
else:
    lembur = 0

total_gaji = (hari_kerja / hari_kerja_perbulan) * gaji
total_gaji += lembur

# Menggunakan string formatting untuk menambahkan titik sebagai pemisah ribuan
total_gaji_formatted = "{:,.2f}".format(total_gaji)

print("\nNama:", nama)
print("Total gaji yang diterima adalah: Rp.", total_gaji_formatted)
