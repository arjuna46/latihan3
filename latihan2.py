a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")
print("Variable a =", a)
print("Variable b =", b)

# You can't use .format and % to format the string in the same line. You should choose one method. Here, I'm using .format.
print("Hasil penggabungan ({}) dan ({}) = {}".format(a, b, a + b))

# Konversi nilai variable
a = int(a)
b = int(b)
print("Hasil penjumlahan ({}) + ({}) = {}".format(a, b, a + b))
print("Hasil pembagian ({}) / ({}) = {}".format(a, b, a / b))