A1=int(input("Masukkan harga dasar barang A: ")) 
A2=int(input("Masukkan harga jual barang A: "))
B1=int(input("Masukkan harga dasar barang B: "))
B2=int(input("Masukkan harga jual barang B: "))
C1=int(input("Masukkan harga dasar barang C: "))
C2=int(input("Masukkan harga jual barang C: "))

O1=A2-A1
O2=B2-B1
O3=C2-C1

if O1>O2>O3 or O1>O3>O2:
    print ("Barang yang harus ditawarkan adalah barang A")
elif O2>O3>O1 or O2>O1>O3:
    print ("Barang yang harus ditawarkan adalah barang B")
elif O3>O1>O2 or O3>O2>O1:
    print ("Barang yang harus ditawarkan adalah barang C")
