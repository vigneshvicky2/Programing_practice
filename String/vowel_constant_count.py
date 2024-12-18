s="banana"
vow=['a','e','i','o','u','A','E','I','O','U']
vow_count=0
const_count=0
for char in s:
    if char.isalpha():
        if char in vow:
            vow_count +=1
        else:
            const_count +=1
print(f"vowel count is: {vow_count}" ,f"constant count is: {const_count}")            
