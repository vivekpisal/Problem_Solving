a=[1,12,13,14,23]
fir=0
ser=13
las=len(a)-1
mid=(fir+las)//2
while fir<=las:
	if a[mid]==ser:
		print('element is found')
		f=True
		break
	elif a[mid]>ser:
		fir=mid+1
		mid=(fir+las)//2
		f=False
	elif a[mid]<ser:
		las=mid-1
		mid=(fir+las)//2
		f=False
if f==False:
	print('element is not found')