import sqlite3
import  time
class Kitap():
    def __init__(self,yazar,isim,sayfa_sayisi,yayinevi):
        self.yazar = yazar
        self.isim = isim
        self.sayfa_sayisi = sayfa_sayisi
        self.yayinevi = yayinevi

    def __str__(self):
        return "İsmi {} --> Yazarı {} --> sayfa_sayisi --> {} Yayınevi --> {}".format(isim,yazar,sayfa_sayisi,yayinevi)

class Kütüphane():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti  = sqlite3.connect("kütüphane.db")
        self.cursor = baglanti.cursor()
        sorgu = "Create Table if not exists kitaplar (İSİM TEXT, YAZAR TEXT, YAYINEVİ TEXT,SAYFA_SAYİSİ İNT)"
        self.cursor.execute(sorgu)
        self.cursor.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def kitaplari_göster(self):
        sorgu = " Select *From kitaplar"
        self.execute(sorgu)
        self.cursor.fetchall()
        if(len(kitaplar)== 0):
            print("Kütühanede Kitap bulunmamaktadır...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_bul(self,isim):
        sorgu = "Select *From kitaplar where isim  = ?"
        self.cursor.execute(sorgu,(isim,))
        self.cursor.fetchall()
        if(len(kitaplar)==0) :
            print("Aradığınız Kitap Kütüphanemizde bulunmamakta....")
        else:

            kitap = Kitap(kitaplar[0][0], kitaplar[0][1], kitaplar[0][2], kitaplar[0][3], kitaplar[0][4])
            print(kitap)
    def kitap_ekle(self,yazar,isim,sayfa_sayisi,yayinevi):
        sorgu = "Insert İnto kitaplar Values(?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.sayfa_sayisi,kitap.yayinevi))
        self.baglanti.commit()

    def kitap_sil(self, isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu, (isim,))

        self.baglanti.commit()

    
