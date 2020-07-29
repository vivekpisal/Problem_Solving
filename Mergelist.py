a=[1,3,5,7,9]
b=[2,4,6,8,10]
c=[]
i=0
j=0
while i<=len(a)-1:
	while j<=len(b)-1:
		try:
			if a[i]>b[j]:
				c.append(b[j])
				j+=1
			elif a[i]<b[j]:
				c.append(a[i])
				i+=1
		except IndexError:
			print(c)
			break
