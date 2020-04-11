def fib(n):
    arr=[]
    a,b=1,2
    while a<n:
        arr.append(a)
        a,b=b,a+b

    return  arr

fibo=fib(4000000)

even=[x  for x in fibo if x%2==0]

print(sum(even))