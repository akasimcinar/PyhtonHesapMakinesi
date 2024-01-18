ilkSayi = int(input("İlk Sayı Giriniz."))
ikinciSayi = int(input("İkinci Sayı Giriniz"))

islem = input("""Yapmak istediğiniz işlemi giriniz.
(Toplama: +, Çıkarma: -, Çarpma: x, Bölme: /)
""")

if islem == "+":
    print("Sonuç: " + str(ilkSayi+ikinciSayi))
elif islem == "-":
    print("Sonuç: " + str(ilkSayi-ikinciSayi))
elif islem == "x":
    print("Sonuç: " + str(ilkSayixikinciSayi))
elif islem == "/":
    print("Sonuç: " + str(ilkSayi/ikinciSayi))