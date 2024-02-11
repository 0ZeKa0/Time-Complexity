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

```python
  a=5
```

  