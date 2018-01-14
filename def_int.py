def is_int(x):
    if x > 0:
        while x>0:
            x -= 1
        if x == 0:
            print(x)
            return True
        else:
            print(x)
            return False
    elif x < 0:
        while x < 0:
            x += 1
        if x == 0:
            print(x)
            return True
        else:
            print(x)
            return False
    elif x==0:
        return True

def digit_sum(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

def factorial(x):
    if x == 1:
        return 1
    elif x == 0:
        return 1
    else:
        return x * factorial(x - 1)


n = input('Input a number: ')
print("Factorial of ", n, " is ", factorial(int(n)))
print(digit_sum(234))

is_int(-2)