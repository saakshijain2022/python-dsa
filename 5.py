def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
n1=int(input("enter1 nos"))
n2=int(input("enter2 nos"))
n3=int(input("enter3 nos"))
print(greatest(n1,n2,n3))       
#rest = greatest(n1,n2,n3)
#print("greatest nos is",rest)