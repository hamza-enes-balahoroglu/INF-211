# -*- coding: utf-8 -*-
"""
====================================================
INF211 Python Dersi - Hamza Tarzında
----------------------------------------------------
Dosya: [01_variable.py]

Amacı: Python'daki temel veri tiplerini anlatır.
       int, float, str, bool gibi tipler
       ve bunlarla yapılabilecek temel işlemler.
       
İpucu: Kodları oku, çalıştır, boz, düzelt ve
       anlamaya çalış. Sadece kopyala yapıştır
       sihirli yapmaz, merak ve anlamak lazım 😉

Yazan: Hamza Enes Balahoroğlu
====================================================


    Önceee "Değişken Nedir?" onu konuşmamız lazım. 
    
        - Değişken derse geciken arakadaşımıza tuttuğumuz yere benzer. Arkadaşımız daha sınıfa gelmemiştir
        belki ama onun sınıfa gelip yanımıza oturacağını bildiğimiz için ona yer ayırırız. Yani değişken
        tutuğumuz sırranın ta kendisidir. Daha teknik düşünürsek bilgisayarımızın RAM'inde içine sonradan 
        birşey koyacağımızı bildiğimiz bir alan tutmak için değişkenleri kullanırız.
        
        - Birazdan vereceğim örnekte kimseyi incitme kırma amacım olmadığını belirtmek isterim.
        Arkadaşınıza göre sıra tutmak da önemli. Arkadaşınız belki tek sıraya sığamıyor adam belki derste
        yatıp uyuyacak bunun içinde ihtiyacı olduğu sıra sayısı farklı olabilir. Hatta ve hatta belki bu
        arkadaş ön sırayı sevmiyor, cam kenarı ya da koridor tarfında durmak istiyor. Fantazi değil mi
        kardeş. Heh burada da devreye değişken tipleri giriyor. Değişken tipleri dediğimiz yapılar, bu
        bahsettiğimiz farklı(psikopat) arkadaşları tanımamızı sağlıyor. Hangi arkadaş gelecek int, str vb.
        Bu sayede hafızada tutulacak alanın boyutuna, yerine, yönüne karar veriliyor.
        
    Artık değişken tiplerini tanımaya hazırız.


integer
    - integer yapsı ondalık basamak bulundurmayan bir değişken yapısıdır. Yani tam sayıların saklanması
    için kullanılır.
    - Aşağıdaki gibi atama yapmanız durumunda python otomatik olarak tipi tanır ve bu bir integer der.
"""
integer_degisken = 12

"""
float
    - float yapsı da integer'a benzer şekide sayısal ifade saklamak içindir ama ondalık bölümleri de 
    saklayabilir.
    - Aşağıdaki gibi atama yapmanız durumunda python otomatik olarak tipi tanır ve bu bir integer der.
"""
float_degisken = 3.14

print(integer_degisken / float_degisken)    #  Bu tip işlemlerde pythonun gelişmiş sistemi sonucu 
                                            # otomatik olarak float değere çeviri.

"""
string
    - string yapılar aslında ileride de bahsedeceğimiz listeler ile doğrudan bağlantılıdır.
    String demek karakter listesi demektir.
    - Atama esnasında süslü parantez(" ") ya da tırnak işareti(' ') kullanılır.
"""

string_degisken = "Hamza buradaydı."

print(string_degisken)

"""
bool
    - bool değişken en gariban değişkendir. ihtiyacı olan alan 1 bit boyurtundadir.
    Daha somut olması açısından integer yapısı 64 bit'e kadar alan kaplayabilir.
    - değer olarak 1 ya da 0 yani true ya da false değerleri alır. genelde mantıksal
    ifadelerin doğruluk durumunun hafızada tutulması için kullanılır.
"""

gariban_bool = True

print(gariban_bool)


# Eğer üşenmezsem ileride veri tiplerinin kullanımı ile alakalı detaylı bir dosya oluşturacağım. 
# Bu dosya sadece veri tipi nedir sorusuna cevap olarak hazırlanmıştır.