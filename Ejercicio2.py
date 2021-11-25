a = int(input("Ingresa el primer numero "))
b = int(input("Ingresa el segundo numero "))
c = int(input("Ingresa el tercer numero "))
def mayor(a,b,c):
    if((a > b) and (a > c)):
        return a
    if((b > a) and (b > c)):
        return b
    if((c > a) and (c > b)):
        return c
print(mayor(a,b,c))