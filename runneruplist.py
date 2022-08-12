n= int (input())
arr= int( input())
count=0
a=max(arr)
for i in range (len(arr)): #c=arr.count(a)
       if a == arr[i] :
        count+=1
        
for i in range (count):
        arr.remove(a)
        
print(max(arr))

#Input (stdin)
 #   5
 #  2 3 6 6 5
#Your Output (stdout)
#  5
         
        
        