n,m=input().split()
n=int(n)
m=int(m)
a=[[ i for i in input()] for j in range(n) ]

try:
    for k in range(n):
        for i in range(n):
            if ((a[i][k]>='a' and a[i][k]<='z') or (a[i][k]>='A' and a[i][k]<='Z')):
                print(a[i][k],end='')
            elif(((a[i][k-1]>'a' and a[i][k-1]<='z') or (a[i][k-1]>'A' and a[i][k-1]<='Z')) or ((a[i][k+1]>'a' and a[i][k+1]<='z') or (a[i][k+1]>'A' and a[i][k+1]<='Z'))):
                 if a[i][k].isalpha():
                     pass
                 else:
                    print(' ',end='')
   
                

except:
    print('#  %!',end='')


        













'''
if __name__=="__main__":
    a=[int(i) for i in input().split(' ')]
    s=int(input())
    n=[[int(i) for i in input().split(' ') ] for j in range(s) ]


f=True
for i in n:
    for j in i:
        if j in a:
            f=True
        else:
            f=False
            break
            
    if f==False:
        break

print(f)'''
