num = 10
flag = False
if num > 1:
    for n in range(2, num):
        if (num % n) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
