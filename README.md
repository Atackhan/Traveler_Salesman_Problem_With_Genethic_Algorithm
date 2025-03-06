
---

# Şehirler Arası Rota Optimizasyonu (Genetik Algoritma Yaklaşımı)

Bu proje, şehirler arasındaki mesafeleri kullanarak **Genetik Algoritma** yöntemi ile en kısa rotayı belirlemeye çalışan bir Python programıdır. Program, rastgele oluşturulan veya kullanıcı tarafından girilen rotaları çaprazlama (crossover) ve mutasyon işlemleriyle optimize etmeye çalışır.

## 🚀 Nasıl Çalışır?

1. **Mesafe Matrisi:**  
   Program, belirli şehirler arasındaki mesafeleri içeren bir matris kullanır.
   
2. **Rota Oluşturma:**  
   - Kullanıcıdan iki adet başlangıç rotası girmesi istenir.  
   - Ek olarak, rastgele iki adet rota daha oluşturulur.  
   
3. **Rota Değerlendirme:**  
   - Tüm rotalar hesaplanarak toplam mesafeleri karşılaştırılır.  
   - En kısa mesafeye sahip olan iki rota seçilir.

4. **Çaprazlama (Crossover):**  
   - En iyi iki rota arasında **tek noktalı çaprazlama** uygulanarak yeni rotalar oluşturulur.  
   - Bu süreç iki defa tekrarlanır, böylece farklı kombinasyonlar denenir.

5. **Mutasyon:**  
   - En iyi bulunan rota üzerinde **rastgele iki nokta değiştirilerek** mutasyon uygulanır.  
   - Mutasyon işlemi, yerel minimuma sıkışmayı önlemek için yapılır.

6. **Sonuç:**  
   - En iyi bulunan rota ve mesafesi ekrana yazdırılır.  

---

## 📌 Kullanılan Fonksiyonlar

### 1. `create_random_route()`
- Tüm şehirleri içeren rastgele bir rota oluşturur ve karıştırır.

### 2. `calculate_distance(route)`
- Verilen rotanın toplam mesafesini hesaplar.

### 3. `single_point_crossover(route1, route2)`
- İki rota arasında tek noktalı çaprazlama işlemi yaparak yeni rotalar oluşturur.

### 4. `validate_route(route)`
- Rotanın geçerli olup olmadığını kontrol eder. Her şehrin bir kez ziyaret edilip edilmediğini ve başlangıç şehrine dönülüp dönülmediğini kontrol eder.

### 5. `get_user_routes()`
- Kullanıcıdan iki rota girişi alır ve doğrular.

---

## 🔧 Kullanım

Python yüklü değilse, [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirip yükleyebilirsiniz.

### **Projeyi Çalıştırmak için:**
1. Proje dosyasını indirin veya klonlayın:

   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi
   ```

2. Python dosyasını çalıştırın:

   ```bash
   python main.py
   ```

3. Terminalde iki farklı rota girerek veya rastgele oluşturulan rotalar ile en iyi rotanın bulunmasını sağlayabilirsiniz.

---

## 🎯 Örnek Çıktı

```bash
Lütfen ilk rotayı girin (0'dan başlayarak): 0 2 4 1 3 5 6 7 8 9 0
Lütfen ikinci rotayı girin (0'dan başlayarak): 0 3 1 6 5 7 2 8 4 9 0

Seçilen En İyi Rota: [0, 3, 1, 6, 5, 7, 2, 8, 4, 9, 0] Mesafe: 2500
Mutasyonsuz Rota: [0, 3, 1, 6, 5, 7, 4, 8, 2, 9, 0] Mesafe: 2450
```

---

