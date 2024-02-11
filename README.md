# Zaman Karmaşıklığı
  Bir algoritmanın zaman karmaşıklığı, genellikle algoritmanın çalışma süresinin, girdi boyutunun değişimine 
  göre nasıl değiştiğini hesaplayan bir yaklaşım olarak tanımlanır.

## Big O Notasyonu Nedir?
 
  Big O notasyonu, bir algoritmanın zaman karmaşıklığını matematiksel olarak ifade ederek, algoritmanın 
  en kötü durumda nasıl davranacağını ve girdi boyutuna göre ne kadar sürede çalışabileceğini belirlemeye 
  yönelik bir araçtır.

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

### n Pozitif Tam Sayının Toplamınn Örneklendirilmesi ve Büyük O Tahmini

```python
  def toplam(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    return toplam
```
 Bu kod parçasında for döngüsü n defa çalışacaktır. Girdi boyutu yani n artıkça çalışma zamanı da artacaktır ve çalışma zamanının artma şekli doğrusaldır.

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

Big O notasyonunu bulabilmek için c ve k çiftine değer verilmesi gerekir.

$$
n>=1
$$

$$
c=1,k=1
$$

### Faktoriyelli İfadelerin Big O Tahmini

```python
  def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)
```

