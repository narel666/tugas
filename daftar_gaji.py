nama_karyawan = input("Masukkan nama anda: ")
while True:
    try:
        hari_kerja = int(input("Hari Anda Kerja Dalam Sebulan (1-30): "))
        if 1 <= hari_kerja <= 30:
            break
        else:
            print("Error: Jumlah hari kerja tidak valid.")
    except ValueError:
        print("Error: Masukkan angka.")

hari_kerja_sebulan = 24
gaji = 4000000

if hari_kerja > hari_kerja_sebulan:
    gaji_lembur = (hari_kerja - hari_kerja_sebulan) * 200000
else:
    gaji_lembur = 0

gaji_anda = (hari_kerja / hari_kerja_sebulan) * gaji
total_gaji = gaji_anda + gaji_lembur

gaji_anda = f"{gaji_anda:,.2f}"
gaji_lembur = f"{gaji_lembur:,.2f}"
total_gaji = f"{total_gaji:,.2f}"

print("\nNama karyawan:", nama_karyawan)
print("Hari kerja:", hari_kerja)
print("Gaji anda:", gaji_anda)
print("Gaji lembur:", gaji_lembur)
print("total:", total_gaji)
