def bs(arr,x):
    l,h=0,len(arr)-1
    if l<=h:
        m=(l+h)//2
        if arr[m]==x:
            return m
        elif x> arr[m]:
           return l=m+1
        elif x <arr[m]:
           return h=m-1
    else:
      return -1
arr=[2,3,4,5,6,7,89,10,11,13,14,15,16,1]
print(bs(arr,10))