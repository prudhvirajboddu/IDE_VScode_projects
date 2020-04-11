def fib():
    strli=""
    li=[]
    a,b=0,1
    while len(strli)!=1000:
        a,b=a,a+b
        li.append(a)
        for i in li:
            strli=str(li[i])    
    return strli,li.index

stli,lis=fib()

print(stli)
print(lis)