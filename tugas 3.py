# program input angka positif

while True:
    angka = int(input("Masukkan angka: "))
    
    if angka < 0:
        print("Harus positif!")
    else:
        break  # keluar dari loop jika angka sudah positif

print(f"Angka yang dimasukkan: {angka}")
