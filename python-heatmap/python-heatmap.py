import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Veri yükleme ve ön işleme (buraya eklemeler yapabilirsiniz)
veri_seti = pd.read_csv("airquality.csv")

# Korelasyon matrisi
korelasyon_matrisi = veri_seti.corr()
sb.heatmap(korelasyon_matrisi, annot=True)
plt.title("Korelasyon Matrisi")
plt.show()

# Gruplama ve toplama
gruplanmis_veriler = veri_seti.groupby('kategori')['değer'].mean()
print(gruplanmis_veriler)

# Grafik çizimi (örneğin, çubuk grafik)
gruplanmis_veriler.plot(kind='bar')
plt.title("Kategoriye Göre Değerlerin Ortalamasi")
plt.xlabel("Kategori")
plt.ylabel("Değer Ortalamasi")
