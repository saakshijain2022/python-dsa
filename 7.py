def f(n):
    if n==0:
        return "n=0"
    print(n**2)
    print(f(n-1))
    return "f has ended and n = ",n



fincal_output= f(5)
print("Final Ouput: ",fincal_output)