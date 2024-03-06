nama_pekerja = input("Masukkan nama anda: ")
hari_kerja = int(input("Masukkan jumlah hari kerja: "))
hari_kerja_perbulan = 25
gaji = 6000000

if hari_kerja > hari_kerja_perbulan:
    lembur = (hari_kerja - hari_kerja_perbulan) * 100000
else:
    lembur = 0

total_gaji = (hari_kerja / hari_kerja_perbulan) * gaji
total_gaji += lembur

total_gaji_formatted = "{:,.2f}".format(total_gaji)

print("\nNama:", nama_pekerja)
print("Upah anda adalah: Rp.", total_gaji_formatted)
