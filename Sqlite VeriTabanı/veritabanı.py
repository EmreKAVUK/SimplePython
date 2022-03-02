import sqlite3 

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor() 

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") 
    con.commit()
def deger_ekle(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("INSERT INTO kitaplık VALUES(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()
def veri_al():
    cursor.execute("Select *From kitaplık")
    liste = cursor.fetchall()
    print(liste)
def isimyazar_al():
    cursor.execute("Select Yazar,İsim From kitaplık")
    liste = cursor.fetchall()
    print(liste)
def veri_al2(yayınevi):
    cursor.execute("Select *From kitaplık where Yayınevi = ?",(yayınevi,))
    liste = cursor.fetchall()
    print(liste)
def verileri_güncelle(eski_yayinevi,yeni_yayinevi):
    cursor.execute("Update kitaplık set Yayınevi = ? where Yayınevi = ?",(yeni_yayinevi,eski_yayinevi))
    con.commit()
def verileri_sil(yazar):
    cursor.execute("Delete From kitaplık where Yazar = ?",(yazar,))
    con.commit()
#isim = input("İsim:")
#yazar = input("Yazar:")
#yayınevi = input("Yayınevi:")
#sayfa_sayısı =  int(input("Sayfa Sayısı:"))

#deger_ekle(isim,yazar,yayınevi,sayfa_sayısı)
#veri_al()
#isimyazar_al()
#veri_al2("Panama")
#veri_al()
#verileri_sil("Dmitry GLUKHOVSKY")
con.close()
