# -*- coding: utf-8 -*-
"""
====================================================
INF211 Python Dersi - Hamza Tarzında
----------------------------------------------------
Dosya: [02_some_rules.py]

Amacı:  Yazılım yazarken değişken tanımlamak vb.
        işlemler için yazılımcılar tarafından kabul
        görmüş bazı kuralları anlamak ve kullanmak.

Yazan: Hamza Enes Balahoroğlu
====================================================
"""

"""
    Bu dosyada bahsedeceğim konu :
    Yapıların isimlendirilmesi konusu. Bu konu basit 
    projelerde genelde önemsenmez. Kullanıcılar 
    isimlendirmeleri rastgele ya da düzensiz seçer.
    Gelişmiş projelerde bu durum tam bir kargaşadır.
        
    İsimlendirmeler kullanılan yapı hakkında hızlıca
    fikir edinmemizi sağlar.
    Kodunuzu okuyacak insanlara merhamet edin.(KAMU SPOTU)
    
    Bu süreçte ben Python Enhancement Proposal 
    8(PEP8) kurallarına uyacağım. Ve bu dosyada 
    bazı kuralları basitçe anlatacağım.
      
"""


"""
snake_case
    Tüm harfler küçük ve kelimeler arasında alt 
    çizgi (_) var. Bu kullanım fonksiyon 
    tanımlamalarında ve değişke tanımlamalarında
    kullanılır.
"""

def merhaba(name, age):     # fonksiyonlar için isimlendirme örneği
    print("Ben "+str(name)+". "+str(age)+" yaşındayım.")
    pass

my_name = "Hamza"           # değişkenler için isimlendirme örneği
my_age  = 19

merhaba(my_name, my_age)



"""
UPPER_CASE

    Tüm harfler büyük ve kelimelerin arasında alt çizgi var(_).
    Sabit değişmeyen ifadelerin tanımlanmasında kullanılır.
"""
PI_SAYISI = 3.14


"""
PascalCase
    Tüm kelimelerin ilk harfleri büyük. Class yapılarını 
    isimlendirirken kullanılır.
"""

"""
_snake_case

    Normal snake_case den farklı olarak değişkenin başına 
    da alt çizgi konulur. Bunun anlamı o değişkenin sadece 
    o dosyaya ya da class'a özel olmasıdır. Dışarıdan 
    doğrudan erişilmesi istenmeyen değişkenler bu kalıpla 
    isimlendirilir.
"""


class MyCar:                        # PascalCase Öneğidir.
    def __init__(self):
        self._engine_status = False # private değişken, motor durumu ve 
                                    # isimlendirmesi _snake_case e örnektir.

arabam = MyCar()

"""
    Bunlara ek olarak değişken tanımlarken, çok parametreli 
    fonksiyon kullanırken vb. dikkat edilmesi gereken bir
    konu da boşluk karakterleridir. Örnek üzrinde anlatmak
    daha kolay.
"""

a = 12 - 2  # Doğru

b=12-2      # Yanlış

# Teknik olarak her iki kod da çalışır ama kodu okuyan 
# biri b yi daha zor algılar.
# göze hoş görünmüyor da denebilir estetik değil.

name  = "Hamza_Enes_Balahoroğlu"

words = name.split("_", 1)  # Aynı şelilde fonsiyona gönderilen prarametreler
            # arasına  ^ da boşluk eklemekte fayda var.

print(words)