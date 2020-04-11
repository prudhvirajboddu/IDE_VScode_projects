str = input("Enter a str:")
res = ""

for i in range(len(str)):
    if(str[i].isdigit() == True):
        res = res+str[i]
if '-' in str and str[0]=='-':
    res = "-"+res

print(res)
