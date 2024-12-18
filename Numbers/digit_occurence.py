n=1533
n=str(n)

k=3
dic={}
for i in range(len(n)):
    if n[i] not in dic:
        dic[n[i]]=1
    else:
        dic[n[i]] +=1

print(dic[str(k)])