def toplam(n):
    toplam = 0
    for i in range(1, n + 1):
        toplam += i
    return toplam

n = int(input("İlk kaç pozitif tam sayının toplamını hesaplamak istiyorsunuz? "))
print(f"{n} pozitif tam sayının toplamı: {toplam(n)}")

