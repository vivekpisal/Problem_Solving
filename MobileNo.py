if __name__=="__main__":
    n=int(input())
    no=[input() for i in range(n)]


f=False
for i in range(len(no)):
    for j in range(len(no[i])):
        if no[i][0]>='7' and no[i][0]<='9' and len(no[i])==10:
            f=True
            break
        else:
            f=False
    if f==True:
        print("YES")
    else:
        print("NO")
