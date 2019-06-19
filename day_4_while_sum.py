x = 0
sum = 0
while x <= 100:

    if x % 2 != 0:
        print(x)
        sum += x
    x += 1
print("从1加到100的偶数和是%d" % sum)
