menu = "y" or "Y"
while menu == "y" or "Y":

    x = int(input('Masukkan NIM Mahasiswa: '))
    if (x >=0) and (x <=100 ) :
        if (x % 2 == 1):
            print("Masuk ke kelas K1")
        else:
            print("Masuk ke kelas K2")
    if (x >=101) and (x <=200 ) :
        if (x % 2 == 1):
            print("Masuk ke kelas K3")
        else:
            print("Masuk ke kelas K4")
    if (x >=201) and (x <=300 ) :
        if (x % 2 == 1):
            print("Masuk ke kelas K5")
        else:
            print("Masuk ke kelas K6")
    if (x >=301 ) :
        if (x % 2 == 1):
            print("Masuk ke kelas K7")
        else:
            print("Masuk ke kelas K8")

    menu=input(" Apakah anda ingin mengecek NIM mahasiswa lain (Y/N) = ")