# Zaman Karmaşıklığı
  Bir algoritmanın zaman karmaşıklığı, genellikle algoritmanın çalışma süresinin, girdi boyutunun değişimine 
  göre nasıl değiştiğini hesaplayan bir yaklaşım olarak tanımlanır.

## Big O Notasyonu 
 
  Big O notasyonu, bir algoritmanın zaman karmaşıklığını matematiksel olarak ifade ederek, algoritmanın 
  en kötü durumda nasıl davranacağını ve girdi boyutuna göre ne kadar sürede çalışabileceğini belirlemeye 
  yönelik bir araçtır.  Zaman karmaşıklığı hesaplanırken girdi boyutu genelde n olarak verilirken Big O Notasyonu hesaplanırken verilen girdi boyutuna göre üst limit hesaplanır. Farklı algoritma karmaşıklıklarını karşılaştırmak ve görselleştirmek için büyük o karmaşıklık tablosu kullanılır ve algoritma performanslarının hızlı bir şekilde karşılaştırılması için önemlidir.

  ![alternatif metin](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

## Theta Notasyonu 

  Theta notasyonu, bir algoritmanın en iyi ve en kötü senaryo çalışma zamanlarını sınırlar. 

## Omega Notasyonu 
  
  Bir algoritmanın en iyi senaryodaki çalışma zamanının alt sınırını ifade eder. Bu notasyon bir algoritmanın çalışma zamanının en iyi durumda ne kadar hızlı olabileceğini ifade eder.



## Big O Notasyonunun Matematiksel Tanımı

  **f(x)** ve **g(x)** adındaki iki fonksiyonun **|f(x)|<=c.|g(x)|** her **x>=k** için birer **k** ve **c** değerleri bulabilirsek 
  **f(x)=O(g(x))** yani **f(x)**, **g(x)**'in Big O'sudur.

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

### İlk n Pozitif Tam Sayının Toplamınn Örneklendirilmesi ve Fonksiyon Karmaşıklığı Hesabı

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

### İlk n Pozitif Tam Sayının Toplamınn Örneklendirilmesi ve Büyük O Tahmini

$$
Toplam=n(n+1)/2
$$

n adet pozitif tam sayının girdi olarak kullanıldığı bir fonksiyonun Big O notasyonunu hesaplanırken en büyük etkiyi yapan terim dikkate alınır. 

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


### İlk n Pozitif Tam Sayının Çarpımının Örneklendirilmesi ve Fonksiyon Karmaşıklığı Hesabı

```python
  def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)
```

Yukarıdaki kod parçasında girdinin n olduğu durumda faktoriyel işlemi yapılabilmesi için rekürsif yaklaşım tercih edildi. Bu yaklaşımda fonksiyonun her bir çağrısı için yapılan işlem sayısı sabit olduğu için ve fonksiyon kendini girdi boyutu kadar çağıracağı için karmaşıklık **O(n)** olur.

### İlk n Pozitif Tam Sayının Çarpımının Örneklendirilmesi ve Büyük O Tahmini

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