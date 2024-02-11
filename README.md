# Zaman Karmaşıklığı
  Bir algoritmanın zaman karmaşıklığı, genellikle algoritmanın çalışma süresinin, girdi boyutunun değişimine 
  göre nasıl değiştiğini hesaplayan bir yaklaşım olarak tanımlanır.
![alternatif metin](https://miro.medium.com/v2/resize:fit:1400/1*5ZLci3SuR0zM_QlZOADv8Q.jpeg)

## Big O Notasyonu 
 
  Big O notasyonu, bir algoritmanın zaman karmaşıklığını matematiksel olarak ifade ederek, algoritmanın 
  en kötü durumda nasıl davranacağını ve girdi boyutuna göre ne kadar sürede çalışabileceğini belirlemeye 
  yönelik bir araçtır.  Zaman karmaşıklığı hesaplanırken girdi boyutu genelde n olarak verilirken Big O Notasyonu hesaplanırken verilen girdi boyutuna göre üst limit hesaplanır.

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

###

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

###

### Faktoriyelli İfadelerin Big O Tahmini

```python
  def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)
```

Yukarıdaki kod parçasında girdinin n olduğu durumda faktoriyelli işlem yapılabilinmesi için rekürsif yaklaşım tercih edildi. Bu yaklaşımda fonksiyonun her bir çağrısı için yapılan işlem sayısının analiz edilmesi gerekir. 