s = str(input("Enter th String: "))

# eg:
# s="hello world"
# op: "world hello"

# without using reverse function

s = s.split()
ans = ""
print(s)
for i in range(len(s)-1,-1,-1):
    if i == len(s)-1:
            ans = ans + s[i]
    else:        
          ans = ans + " " + s[i]

print(ans)
