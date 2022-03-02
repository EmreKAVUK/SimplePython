from cryptography.fernet import Fernet
#anahtar oluşturma
key = Fernet.generate_key()
#anahtarın değeri bir değişkene atanır
f = Fernet(key)
#cümle =input("Lütfen şifrelenecek cümleyi giriniz...")
#düz metin sifreli metne dönüstürülür
token = f.encrypt(b"Merhaba dostum")
print("Şifreli metin : \n",token)
d = f.decrypt(token)
print("\n\nDüz metin: \n",d)