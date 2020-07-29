'''n=int(input())
s=""
c=[]
for _ in range(n):
    i=input().split(' ')
    d=int(i[0])
    if d==1:
        s=s+i[1]
        c.append(1)
    elif d==2:
        l=len(s)-int(i[1])
        f=s[l:]
        s=s[:-int(i[1])]
        c.append(2)
    elif d==3:
        print(s[int(i[1])-1])
    elif d==4:
        if c[-1]==2:
            s=s+f
        elif c[-1]==1:
            s=f'''


def arrayManipulation(n, queries,m):
    a=[0 for i in range(n)]
    for i in range(m):
        a[queries[i][0]-1]=a[queries[i][0]-1]+queries[i][2]
        a[queries[i][1]-1]=a[queries[i][1]-1]+queries[i][2]
    return max(a)


        

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries,m)
