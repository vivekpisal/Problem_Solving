import numpy
def negno(a):
    count=0
    for i in a:
        for j in i:
            if j<0:
                count+=1
            else:
                pass

    return count




a=[[-1,-2,3],[-2,-3,4],[-4,5,8]]
count=negno(a)
print(count)
