import time
t0=time.time()
num = int(input("Enter"))
def reverse(num):
    temp = num
    rev = 0
    while temp > 0:
        rev = rev*10+temp%10
        temp = temp//10

    return rev

def isPalin(num):
    temp = reverse(num)
    if temp == num:
        return True
    else:
        return False

while True:
    if isPalin(num) == True:
        print("Palindrome found {}".format(num))
        break
    else:
        num += reverse(num)
        print("Addition is {}".format(num))

print("Execution time is ",(time.time()-t0))

