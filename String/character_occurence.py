s = str(input("Enter the string: "))
count = "a"
dic ={}
for char in s:
    if char in dic:
        dic[char] += 1
    else:
        dic[char] = 1    
print(dic) 
print(f"No of times {count} occured" , dic[count] )    
