import requests
from bs4 import BeautifulSoup
a = input("Şampiyon ismi giriniz:")
url = "https://mobatr.net/sampiyon/"+a+"/counter-ct"
response = requests.get(url)
print(response)
icerik = response.content
soup = BeautifulSoup(icerik,"html.parser")

counter = soup.find_all("div",{"class":"c-guides__list list-unstyled"})
for ct in counter:
    ct = ct.text

    ct = ct.strip()
    ct = ct.replace("\n","")
    print("{}'nun counterları : {}\n".format(a, ct),sep="/n")


