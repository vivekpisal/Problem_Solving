nums=[0,1,3,50,75]
lower=0
upper=99
c=[]
for i in range(len(nums)-1):
	c.append([nums[i]+1,nums[i+1]-1])


c.append([nums[-1]+1,upper])
c.pop(0)
ans=[]
for i in range(len(c)):
	if c[i][0]!=c[i][1]:
		ans.append(f'{c[i][0]}->{c[i][1]}')
	else:
		ans.append(f'{c[i][0]}')


print(ans)