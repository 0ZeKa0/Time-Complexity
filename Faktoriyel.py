def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)

sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

if sayi < 0:
    print("Negatif bir sayının faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0'ın faktöriyeli 1'dir.")
else:
    print(f"{sayi}'in faktöriyeli: {faktoriyel(sayi)}")
