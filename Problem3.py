#Menhitung Waktu Tempuh

print("Masukkan Waktu Mulai!")
j1=int(input("Masukkan Jam   :"))
m1=int(input("Masukkan Menit :"))
d1=int(input("Masukkan Detik :"))
print("Masukkan Waktu Selasai!")
j2=int(input("Masukkan Jam   :"))
m2=int(input("Masukkan Menit :"))
d2=int(input("Masukkan Detik :"))

t1=(j1*3600) + (m1*60) + (d1)
t2=(j2*3600) + (m2*60) + (d2)
totaltime = t2-t1

lamaj=(totaltime//3600)
sisa=(totaltime%3600)
lamam=(sisa//60)
lamad=(sisa-(60*lamam))

print(f"Tuan Riz berlari selama {lamaj} jam {lamam} menit {lamad} detik")
