if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    l=[]        #   l=list()
    for i in range  (x+1):
        for j in range (y+1):
            for k in range  (z+1):
                if i+j+k!= n:
                    l.append([i,j,k])
    print(l)

#one liner
#s=[[i,j,k]for i in range(x+1) for j in range(y+1)for k in range (z+1) if i+j+k!=n]
#print(s)


    # input (stdin)

    # 1

    # 1

    # 1

    # 2

# Your Output (stdout)

    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Expected Output

    # [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]