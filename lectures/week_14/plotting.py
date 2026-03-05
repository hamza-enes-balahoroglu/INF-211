import matplotlib.pyplot as plt
import numpy as np

# 1. ADIM: Veri Hazırlama
# 1000 öğrencinin sınav notlarını rastgele üretiyoruz.
# Ortalaması 75, standart sapması 10 olan bir "Normal Dağılım" (Çan Eğrisi) kullanıyoruz.
np.random.seed(42) 
notlar = np.random.normal(75, 10, 1000)

# 2. ADIM: Grafiği Oluşturma
plt.figure(figsize=(10, 6))

# plt.hist() fonksiyonu histogramı çizer.
# x: Verimiz (notlar)
# bins=20: Veriyi 20 eşit aralığa (kutuya) böl demektir.
# edgecolor='black': Sütunların sınırlarını siyah çizgiyle belirginleştirir.
plt.hist(notlar, bins=20, color='orange', edgecolor='black')

# 3. ADIM: Etiketler ve Başlık (Ders notlarında vurgulanan "İyi Grafik" kuralları)
plt.title('Örnek Histogram: Sınav Notu Dağılımı')
plt.xlabel('Sınav Puanı')            # X ekseni: Değer aralığı
plt.ylabel('Öğrenci Sayısı (Frekans)') # Y ekseni: O aralığa düşen kişi sayısı

# Izgara çizgileri ekleyerek okunabilirliği artıralım (Sayfa 22'deki gibi)
plt.grid(axis='y', alpha=0.5, linestyle='--')

# Grafiği göster
plt.show()