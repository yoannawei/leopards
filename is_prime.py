def is_prime(x):
    if x == 0:
        return False
    elif x==1:
        return False
    elif x==2:
        return True
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        else:
            return True

num = input("Enter a number: ")
if is_prime(int(num)) == True:
    print(num, " is prime")
else:
    print(num, " is not prime")


