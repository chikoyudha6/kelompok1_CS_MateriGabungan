print("##PROGRAM PYTHON DISKON POTONGAN HARGA##")
print("========================================")
print("")

total_belanja = float(input("masukan total belanja anda: Rp"))

if total_belanja < 100000:
    diskon = 0
elif 100000 <= total_belanja < 500000:
    diskon = 0.1
elif 500000 <= total_belanja < 1000000:
    diskon = 0.2
else:
    diskon = 0.3

harga_diskon = total_belanja - (total_belanja * diskon)

print("Total belanja :", total_belanja)
print("Selamat, anda mendapat diskon" , diskon * 100 , "%")
print("Total bayar: Rp", harga_diskon)