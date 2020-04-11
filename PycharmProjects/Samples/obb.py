n=int(input("Enter"))

def reverse(num):
    temp=num
    rev=0
    while temp>0:
        rev=rev*10+temp%10
        temp//=10

    return rev

def isPalin(num):
    temp=reverse(num)
    if temp==num:
        return True
    else:
        return False

num=n
while True:
    if isPalin(num):
        print("palindrome Found which is {}".format(num))
        break
    else:
        num=num+reverse(num)
        print("Addition is {}".format(num))