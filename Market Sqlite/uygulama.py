from fonklar import *
print("""
Lütfen Seçim Yapınız...
1-)Ürün Ekle
2-)Ürün Sil
3-)Ürün Sorgula
4-)Çıkış 

""")
tezgah = Tezgah()
cevap = int(input())
if(cevap == 1):
    isim = input("Ürün İsmi: ")
    ürün_fiyatı = float(input("Ürün Fiyatı:  "))
    ürün_markası = input("Ürün Markası : ")
    son_kullanma = int(input("Son Kullanma Tarihi"))
    yeni_ürün = Ürünler(isim,ürün_fiyatı,ürün_markası,son_kullanma)
    print("Ürün Ekleniyorrr...")
    time.sleep(3)
    tezgah.ürün_ekle(yeni_ürün)
    print("İşlem Başarılı...")

elif(cevap == 2):
    silenecek = input("Silmek İstediğiniz ürünün İsmini girin..")
    onay = input("Silmek istediğinizden Emin misiniz ? E/H")
    if(onay == "E" or onay == "e"):
        print("Ürün Siliniyor..")
        time.sleep(3)
        tezgah.ürün_sil(silenecek)
        print("İşleminiz Başarı ile Gerçekleşti ")
elif(cevap == 3):
    sorgulanacak = input("Sorgulanacak Ürün İsmini giriniz...")
    tezgah.ürün_sorgula(sorgulanacak)