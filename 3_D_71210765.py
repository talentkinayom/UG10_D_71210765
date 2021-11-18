daftar = input("Masukan daftar belanja : ").title().split(",")
print("Daftar belanja :",daftar)

tambahan = input("Masukan barang yang ingin ditambahkan : ").lower()
if tambahan.title() in daftar:
    print("Barang",tambahan.upper(),"sudah berada dalam daftar belanja")
else:
    daftar.append(tambahan.title())
    print("Hasil penambahan pada daftar belanja",daftar)