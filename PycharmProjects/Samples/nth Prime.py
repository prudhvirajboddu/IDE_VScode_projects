import time,math
t0=time.time()
Str=str(math.factorial(100))
digits=[int(x) for x in Str]
S=0
for x in digits:
    S=S+x
print(S)
print(time.time()-t0)

