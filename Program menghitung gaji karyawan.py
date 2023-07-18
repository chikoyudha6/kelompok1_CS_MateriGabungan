print("## PROGRAM PYTHON MENGHITUNG GAJI KARYAWAN ##")
print("=============================================")
print("")

def hitung_gaji(nama, golongan, jam_kerja):
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        print("Golongan tidak valid.")
        return

    if jam_kerja > 48:
        uang_lembur = (jam_kerja - 48) * 4000
    else:
        uang_lembur = 0

    gaji = (jam_kerja * upah_per_jam) + uang_lembur

    print("", nama , "menerima upah Rp." , gaji , "per minggu")
    


nama_karyawan = input("Masukkan nama karyawan: ")
golongan_karyawan = input("Masukkan golongan karyawan (A/B/C/D): ")
jam_kerja_karyawan = int(input("Masukkan jam kerja karyawan: "))

hitung_gaji(nama_karyawan, golongan_karyawan, jam_kerja_karyawan)