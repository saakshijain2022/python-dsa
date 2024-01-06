def pat(n):
    s = []
    for i in range(1,n+1):
        t = []
        while i>0:
            t.append(i)
            i -= 1
        s.append(t)
    return s
