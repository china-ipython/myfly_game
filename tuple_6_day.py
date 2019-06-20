tuple_1 = ("zhanghai", 18, 25.3, "zhanghaiping")
for tup in tuple_1:
    print("这是打印的什么东西" + str(tup))
print(tuple_1.count("zhanghai"))
print("%s年龄是%d\n体重是%.2f\n别名是%s" % tuple_1)
