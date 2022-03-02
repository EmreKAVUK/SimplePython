from islem import *
print("""
1-) Şarkıları Göster
2-)Şarkı Ekle
3-)Şarkı Sil
4-)Toplam Şarkı Süresini Öğren
5-) Çıkış yap

""")
plak = Plak()
while True:
    a = int(input())
    if(a==1):
        plak.sarkilari_goster()
    elif(a == 2):
        isim = input("Sarkı ismi : ")
        sanatci = input("Sanatci ismi :")
        albüm = input("Albüm ismi :")
        prodüksiyon = input("Prodüksiyon İsmi: ")
        sarki_süresi = float(input("Şarkı Süresi : "))
        yeni_sarki = Sarki(isim,sanatci,albüm,prodüksiyon,sarki_süresi)
        print("Sarkı Ekleniyorrr...")
        time.sleep(3)
        plak.sarki_ekle(yeni_sarki)
        print("İşlem Başarılı...")
    elif (a == 3):
        k = input("Silinecek Şarkının İsmini girin : ")
        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Şarkı Siliniyor...")
            time.sleep(2)
            plak.sarki_sil(k)
            print("Şarkı silindi....")
    elif (a==4):
        plak.toplamsüre()
    elif (a==5):
        çıkış = input("Çıkmak İstediğinizden Emin misiniz ? (E/H)")
        if(çıkış == "E" or çıkış == "e"):
            print("Çıkış Yapılıyor...")
            time.sleep(2)
            print("Bizi Tercih Ettiğiniz İçin Teşekkürler...")
            break;





