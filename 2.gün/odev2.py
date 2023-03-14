ogrenciler = []  # bos ogrenci listesi olusturma

def ogrenci_ekle(ad, soyad): # ogrenci ekleme fonksiyonu
    ogrenciler.append((ad, soyad))

def ogrenci_sil(ad, soyad): #ogrenci silme fonksiyonu 
    while (ad, soyad) in ogrenciler: # dongu ile girilen öğrencileri silme
        ogrenciler.remove((ad, soyad))

def tum_ogrencileri_yazdir(): # oğrencileri index numarasina göre ekrana yazdirma fonksiyonu
    for i, ogrenci in enumerate(ogrenciler): #for dongusu ile ogrenciler listesinin icinde donme
        print(f"{i}: {ogrenci[0]} {ogrenci[1]}")

def ogrenci_numarasi(ad, soyad): # listedeki index numarsina gore ogrenci numarasi yazdirma
    numara = ogrenciler.index((ad, soyad))
    print(numara)

ogrenci_ekle("Ali", "Aslan") #konsolda test etme
ogrenci_ekle("Ayşe", "Demir")
ogrenci_ekle("Mehmet", "Kurt")
tum_ogrencileri_yazdir()
ogrenci_sil("Ali", "Aslan")
tum_ogrencileri_yazdir()
ogrenci_numarasi("Mehmet", "Kurt")
