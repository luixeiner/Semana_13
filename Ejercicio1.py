a = int(input("Ingresa el primer numero "))
b = int(input("Ingresa el segundo numero "))
def mayor(a,b):
    if(a > b):
        return a
    if(b > a):
        return b
print(mayor(a,b))
