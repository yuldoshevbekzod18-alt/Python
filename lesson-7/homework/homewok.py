#is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.
def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

is_prime(11)


#digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    yegindi=0
    while k>0:
        num=k%10
        yegindi+=num
        k//=10
    return yegindi
digit_sum(999)


#Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.
def berilgan(n):
    d = 1
    while d <= n:
        print(d)
        d *= 2

berilgan(10)
