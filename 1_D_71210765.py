hargamakanan = int(input("Harga makanan sebesar Rp "))
hargasnack = int(input("Harga snack sebesar Rp "))
hargaminuman = int(input("Harga minuman sebesar Rp "))
uang = int(input("Uang yang anda bawa sebesar Rp "))
hargatotal = hargamakanan+hargasnack+hargaminuman

print("Total yang harus anda bayar sebesar Rp",hargatotal)
if uang == hargatotal:
    print("Uang anda pas! Tidak ada kembalian dan Utang :D")
elif uang < hargatotal:
    print("Uang Anda kurang! Anda memiliki utang sebesar Rp",hargatotal-uang)
else:
    print("Anda memiliki kembalian sebesar Rp",uang-hargatotal)