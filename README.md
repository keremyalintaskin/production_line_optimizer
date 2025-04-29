#  Üretim Hattı Zamanlayıcısı (Production Line Optimizer)

Bu proje, sıralı şekilde yapılması gereken `n` adet işin, `m` farklı makinede **en az toplam süre** ile tamamlanmasını sağlayan bir algoritmayı içerir. Her işin her makinedeki süresi farklıdır ve makineler arasında geçiş yapılırken bir **geçiş maliyeti** oluşur. Amaç, tüm işleri sırayla yaparken **toplam süreyi en aza indirmektir**.

---

##  Problem Tanımı

- `n` adet sıralı iş bulunmaktadır.
- Her iş, `m` farklı makineden birinde yapılabilir.
- Her makine, aynı işi farklı sürede tamamlar.
- İşten işe geçerken makine değiştirilirse **geçiş süresi/maliyeti** eklenir.
- Hedef: İşleri öyle bir sırayla ve makinelerde yapmak ki, **toplam süre** (iş süresi + geçiş süresi) minimum olsun.

---

##  Örnek Girdi

```python
completion_time = [
    [5, 6, 8],  # İş 0: Makine 0, 1, 2 üzerindeki süreleri
    [4, 7, 3],  # İş 1
    [6, 5, 4],  # İş 2
    [3, 6, 7],  # İş 3
]

transition_cost = [
    [0, 2, 4],  # Makine 0'dan diğerlerine geçiş
    [2, 0, 1],  # Makine 1'den diğerlerine geçiş
    [3, 2, 0],  # Makine 2'den diğerlerine geçiş
]
```

---

##  Algoritma Açıklaması

Bu problem, **Dinamik Programlama** kullanılarak çözülmüştür.

- `dp[i][j]` tablosu: `i`. işi `j`. makinede yaparsak, o ana kadar harcanan **minimum toplam süreyi** tutar.
- İlk iş için doğrudan süreler yazılır.
- Sonraki işler için, tüm önceki makinelerden geçişler kontrol edilir, **geçiş maliyeti + iş süresi** eklenerek minimum olan seçilir.

---

##  Kod

```python
def min_total_time(completion_time, transition_cost):
    n = len(completion_time)  # İş sayısı
    m = len(completion_time[0])  # Makine sayısı

    dp = [[float('inf')] * m for _ in range(n)]

    # İlk işin sürelerini yaz
    for j in range(m):
        dp[0][j] = completion_time[0][j]

    # Diğer işleri sırayla doldur
    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                cost = dp[i-1][k] + transition_cost[k][j] + completion_time[i][j]
                dp[i][j] = min(dp[i][j], cost)

    return min(dp[n-1])

# Test
print("Minimum toplam süre:", min_total_time(
    completion_time=[
        [5, 6, 8],
        [4, 7, 3],
        [6, 5, 4],
        [3, 6, 7]
    ],
    transition_cost=[
        [0, 2, 4],
        [2, 0, 1],
        [3, 2, 0]
    ]
))
```

---

##  Çıktı

```
Minimum toplam süre: 18
```

---

##  Zaman ve Bellek Karmaşıklığı

- **Zaman Karmaşıklığı:** O(n × m²)  
  (Her iş ve her makine için, tüm önceki makinelerle karşılaştırma yapılır.)

- **Bellek Karmaşıklığı:** O(n × m)  
  (Tüm durumlar `dp` tablosunda saklanır.)

---


---

##  Dosya Yapısı

```
.
├── production_line_optimizer.py
└── README.md
```

---

