s ="babad"
n = len(s)
longest= ""
for i in range(n):
    for j in range(i,n):
        sub_string = s[i:j+1] # substring extraction
        if sub_string == sub_string[::-1]:
            if len(sub_string) > len(longest):
                longest = sub_string
print(longest)                