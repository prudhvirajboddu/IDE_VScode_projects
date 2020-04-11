import time
t0=time.time()

for a in range(1,300):
    for b in range(1,600):
        for c in range(1,1000):
            if (a**2+b**2==c**2):
                if (a+b+c == 1000):
                    print(a*b*c)
                    print(a)
                    print(b)
                    print(c)
                    print(time.time() - t0)
                    exit(0)


print(time.time()-t0)