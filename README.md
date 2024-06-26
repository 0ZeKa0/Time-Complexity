# Zaman Karmaşıklığı
  Bir algoritmanın zaman karmaşıklığı, genellikle algoritmanın çalışma süresinin, girdi boyutunun değişimine 
  göre nasıl değiştiğini hesaplayan bir yaklaşım olarak tanımlanır.

## Big O Notasyonu 
 
  Big O notasyonu, bir algoritmanın en kötü durumda ne kadar sürede çalışabileceğini belirlemek için kullanılan bir matematiksel ifadedir. Bu notasyon, algoritmanın zaman karmaşıklığını ifade ederek, girdi boyutuna bağlı olarak işlem süresinin nasıl değişeceğini tahmin eder. Zaman karmaşıklığı hesaplanırken genellikle girdi boyutu n olarak belirlenir ve Big O notasyonu, bu girdi boyutuna göre algoritmanın en kötü durumda ne kadar sürede çalışabileceğini belirler. Büyük O karmaşıklık tablosu, farklı algoritmaların karmaşıklıklarını karşılaştırmak ve görselleştirmek için kullanılır. Bu tablo, algoritmaların performanslarını hızlı bir şekilde karşılaştırmak ve en etkili olanı seçmek için önemlidir.

  ![alternatif metin](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

1 < logn < n < nlogn <... < n!

## Theta Notasyonu 

  Theta notasyonu, bir algoritmanın en iyi ve en kötü senaryo çalışma zamanlarını sınırlar. 
  
## Theta Notasyonu Matematiksel Tanımı
 **f(x)** ve **g(x)** adındaki iki fonksiyonun **c1.|g(x)|<=|f(x)|<=c2.|g(x)|**   için birer **c1**, **c2** ve **k** değerleri bulabilirsek 
  **f(x)=Θ(g(x))** yani **g(x)**, **f(x)**'in Thetasıdır.

## Omega Notasyonu 
  
  Bir algoritmanın en iyi senaryodaki çalışma zamanının alt sınırını ifade eder. Bu notasyon bir algoritmanın çalışma zamanının en iyi durumda ne kadar hızlı olabileceğini ifade eder.

## Omega Notasyonu Matematiksel Tanımı
 **f(x)** ve **g(x)** adındaki iki fonksiyonun **|f(x)|>=c.|g(x)|** her **x>=k** için birer **k** ve **c** değerleri bulabilirsek 
  **f(x)= Ω(g(x))** yani **g(x)**, **f(x)**'in Omegasıdır.

## Big O Notasyonunun Matematiksel Tanımı

  **f(x)** ve **g(x)** adındaki iki fonksiyonun **|f(x)|<=c.|g(x)|** her **x>=k** için birer **k1** ve **k2** ve **c** değerleri bulabilirsek 
  **f(x)=O(g(x))** yani **g(x)**, **f(x)**'in Big O'sudur.

### Örneğin

$$
  6x^3 = O(x^4) 
$$

 yukarıdaki ifade için 

$$
 x>= 6
$$

 denir.

 $$
 x^4 >= 6x^3  
 $$

 yukarıdaki ifade için  
 
 $$
 c=1, k=6
 $$

c ve k reel sayıları bulunur. Bu sebeple ifadenin doğruluğu ispatlanmış olur.

### İlk n Pozitif Tam Sayının Toplamınn Örneklendirilmesi ve Fonksiyon Karmaşıklık Hesabı

```python
  def gauss_toplam(n):
    return (n * (n + 1)) // 2

```
Verilen kod parçasında işlem doğrudan formül kullanılarak yapıldığı için zaman karmaşıklığı **O(1)** olur. Aynı işlemin formülsüz yapılması 

```python
    def toplam(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    return toplam

```
yukardaki gibi for döngüsü kullanılmasına sebep olur. Döngü içindeki işlemin girdi boyutu kadar çalıştırılması sebebiyle bu kod parçasının karmaşıklığı **O(n)** olur.

### İlk n Pozitif Tam Sayının Toplamın Örneklendirilmesi ve Asimptotik Gösterimi

$$
Toplam=n(n+1)/2
$$

n adet pozitif tam sayının girdi olarak kullanıldığı ve bu girdinin toplamının istendiği bir fonksiyonda Big O notasyonu hesaplanırken en büyük etkiyi yapan terim dikkate alınır. 

$$
f(n)=1+2+3+...+n
$$
$$
O(g(n))=f(n)
$$

$$
1+2+3+...+n<=n+n+n+..+n
$$

yukarıdaki eşitsizlikten anlaşılacağı üzere 

$$
f(n)<=n.n
$$

$$
f(n)<=n^2
$$

Big O notasyonunu bulabilmek için bir c,k ikilisi seçilmelidir.

$$
n>=1
$$

$$
c=1,k=1
$$


$$
f(n)=O(n^2)
$$


### İlk n Pozitif Tam Sayının Çarpımının Örneklendirilmesi ve Fonksiyon Karmaşıklık Hesabı

```python
  def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)
```

Yukarıdaki kod parçasında girdinin n olduğu durumda faktoriyel işlemi yapılabilmesi için rekürsif yaklaşım tercih edildi. Bu yaklaşımda fonksiyonun her bir çağrısı için yapılan işlem sayısı sabit olduğu için ve fonksiyon kendini girdi boyutu kadar çağıracağı için karmaşıklık **O(n)** olur.

### İlk n Pozitif Tam Sayının Çarpımının Örneklendirilmesi ve Asimptotik Gösterimi 

n adet pozitif tam sayının girdi olarak kullanıldığı ve bu girdinin çarpımının istendiği bir fonksiyonda Big O notasyonunu hesaplanırken en büyük etkiyi yapan terim dikkate alınır.  

$$
f(n)=1.2.3.4.5...n
$$

$$
n!=1.2.3...n
$$

$$
1.2.3...n<= n.n.n...n
$$

$$
f(n)<=n^n, n>=1
$$

n'nin 1'den büyük olduğu durumlar için c,k ikilisi seçeriz.

$$
g(n)=n^n, c=1, k=1
$$

$$
n!<= 1.n^n, n>=1 
$$

$$
c=1, k=1
$$

$$
n!=O(n^n)
$$
