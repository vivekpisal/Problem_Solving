words=["This","is","an","example","of","text","justification."]
maxwidth=16
ans=[]
for i in range(len(words)):
	if len(words[i])==maxwidth:
		temp=[]
		temp.append(words[i])
		ans.append(temp)
		break
	else:
		temp=[""]
		for j in range(i,len(words)):
			if len(temp[0]+words[j])<maxwidth:
				temp[0]=temp[0]+words[j]

		ans.append(temp)
		temp=[""]



print(ans)