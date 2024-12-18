s = str(input("Enter the string: "))
ans = ""
dic ={}
for char in s:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1    

#sort dictionary
sorted_dic=sorted(dic.keys() , key=lambda x:dic[x] , reverse=True)
result = ''.join(char * dic[char] for char in sorted_dic)

print(result)    