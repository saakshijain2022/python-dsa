def f(n):
    if n==0:
        return "n=0"
    print(n**2)
    output =f(n-1)
    print(output)
    return "f has ended and n = ",n



fincal_output= f(5)
print("Final Ouput: ",fincal_output)