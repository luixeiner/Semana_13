a=[1,2,3,4]  
def suma(a):
    total = 0
    for i in range(len(a)):
        total += a[i] 
    return total
print(sum(a))
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
    return total
print(mult(a))