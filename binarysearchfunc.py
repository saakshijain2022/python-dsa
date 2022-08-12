def binarysearch(data,low,high,item):
    if low <=high:
        middle=(low+high)//2

        if data[middle]==item:
             return middle
        elif item < data[middle]:
            return binarysearch (data,low,middle-1,item)
        else:
            return binarysearch (data,middle+1,high,item)
    
    else:
        return -1

nums=[3,4,5,6,87,3,2,5,99,110,21]
print(binarysearch (nums,0,len(nums)-1,110))