sum=pow(2,1000)
digits=[int(x) for x in str(sum)]
S=0
for x in digits:
    S=S+x
print(S)