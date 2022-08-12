s = "heello stududent of devsnest"
d = {}
for c in s:
    if c in d:
        d[c]+= 1
    else:
        d[c]=1
print(d)
mk=mv=0
for key in d:
    val = d[key]
    print(key,val)
    if val>mv:
        mv=val
        mk=key
print( "ans=",mk,mv)