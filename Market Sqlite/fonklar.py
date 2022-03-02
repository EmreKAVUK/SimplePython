import sqlite3
import time
class Ürünler():
    def __init__(self,ürün_ismi,ürün_fiyatı,ürün_markası,ürün_sonkullanmatarihi):
        self.ürün_ismi = ürün_ismi
        self.ürün_fiyatı = ürün_fiyatı
        self.ürün_markası = ürün_markası
        self.ürün_sonkullanmatarihi = ürün_sonkullanmatarihi
    def __str__(self):
        return "Ürünün İsmi : {} --> Ürünün Fiyatı --> {} --> Ürünün Markası --> {}  --> Ürünün Son Kullanma Tarihi {}".format(self.ürün_ismi,self.ürün_fiyatı,self.ürün_markası,self.ürün_sonkullanmatarihi)
class Tezgah():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("market.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists liste (İSİM TEXT, FİYAT FLOAT, MARKA TEXT, SONKULLANMA INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kapat(self):
        self.baglanti.close()
    def ürün_ekle(self,isim):
        sorgu  = "Insert into liste VALUES (?,?,?,?)"
        self.cursor.execute(sorgu,(isim.ürün_ismi,isim.ürün_fiyatı,isim.ürün_markası,isim.ürün_sonkullanmatarihi))
        self.baglanti.commit()
    def ürün_sil(self,ürün_ismi):
        sorgu = "Delete From liste where İSİM = ?"
        self.cursor.execute(sorgu,(ürün_ismi,))
        self.baglanti.commit()
    def ürün_sorgula(self,ürün_ismi):
        sorgu  = "Select *From liste where İSİM = ? "
        self.cursor.execute(sorgu,(ürün_ismi,))
        tutacak = self.cursor.fetchall()
        if(len(tutacak)== 0):
            print("Böyle Bir Ürün bulunmuyor")
        else:
            for i in tutacak:
                ürünler = Ürünler(i[0], i[1], i[2], i[3])
                print(ürünler)
