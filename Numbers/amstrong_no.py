n=153
n=str(n)
sum=0
for i in range(len(n)):
    sum +=int(n[i])**3
if int(n)==sum:
    print("It is a amstrong number")
else:
    print("It is not a amstrong number")