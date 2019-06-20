info = {"name": "zhangsan", "age": 18, "redan": "True", "adreess": "AnhuiHefei", "phone": "1595531392"}

# print(info)
# print(info["age"])
info["move"] = 22
info["name"] = "张三"
# print(info)
print(len(info))
for k in info:
    # print(k, end = '')

    if k == "name":
        print(k, (info[k]))
    print("%s:%s" % (k, (info[k])))
