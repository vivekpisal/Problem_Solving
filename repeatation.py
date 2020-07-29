'''
First Approach:
a=[10,4,12,34,134,1,10]
a=sorted(a)
for i in range(len(a)-1):
	if a[i]==a[i+1]:
		print(a[i])
		break

'''

'''
Second Approach
a=[10,4,12,34,134,1,10]
dic=dict()
for i in range(len(a)):
	try:
		if dic[a[i]]:
			dic[a[i]]=dic[a[i]]+1
	except:
		dic[a[i]]=1
print(dic)

'''