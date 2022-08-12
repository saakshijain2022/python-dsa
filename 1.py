
if __name__ == '__main__':
    st = "AEIOUkcdcxwjfrhflsnqiebxzau"
    s={"a","e","i","o","u"}
    sum = 0
    i=0
    for i in range(0,len(st)):
        if st[i].lower() not in s:
            print("ji")
        else:
            print("vowels" , st[i])
            sum = sum+1
    
    print(sum)