import sqlite3
import time
class Sarki():
    def __init__(self,Sarki_ismi,Sanatci,Albüm,Prodüksiyon_Sirketi,Sarki_süresi):
        self.Sarki_ismi = Sarki_ismi
        self.Sanatci = Sanatci
        self.Albüm = Albüm
        self.Prodüksiyon_Sirketi = Prodüksiyon_Sirketi
        self.Sarki_süresi = Sarki_süresi
    def __str__(self):
        return "Şarkının İsmi ---> {} Sanatçısı --->{} Albüm İsmi ---> {} Prodüksiyon Şireketi ---> {} Şarkinin Süresi ---> {}".format(self.Sarki_ismi,self.Sanatci,self.Albüm,self.Prodüksiyon_Sirketi,self.Sarki_süresi)

class Plak():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti  = sqlite3.connect("sarki.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table if not exists Sarkilik (SARKI TEXT, SANATCİ TEXT, ALBÜM TEXT, PRODÜKSİYON TEXT, SARKİ_SÜRESİ FLOAT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kapat(self):
        self.baglanti.close()
    def sarkilari_goster(self):
        sorgu = "Select *From Sarkilik"
        self.cursor.execute(sorgu)
        sarkilar = self.cursor.fetchall()
        if(len(sarkilar) == 0):
            print("Şarkılıkta Şarkı bulunmuyor...")
        else:
            for i in sarkilar:
                sarki = Sarki(i[0],i[1],i[2],i[3],i[4])
                print(sarki)
    def sarki_ekle(self,sarki):
        sorgu = "Insert into Sarkilik Values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.Sarki_ismi,sarki.Sanatci,sarki.Albüm,sarki.Prodüksiyon_Sirketi,sarki.Sarki_süresi))
        self.baglanti.commit()
    def sarki_sil(self,Sarki_ismi):
        sorgu = "Delete From Sarkilik where SARKI = ?"
        self.cursor.execute(sorgu,(Sarki_ismi,))
        self.baglanti.commit()

    def toplamsüre(self):
     sorgu = "Select SARKİ_SÜRESİ from Sarkilik"
     self.cursor.execute(sorgu)
     tutacak = self.cursor.fetchall()
     if(len(tutacak) == 0):
         print("Şarkı bulunmamaktadır...")
     else:
         sum = 0
         for i in tutacak:
             for j in i:
                 sum += j

         print("Mp3 içindeki bütün şarkıların toplam süresi: ", sum)


