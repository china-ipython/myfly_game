message = "  helloWorld"
message1 = " "
# for c in message :
#     print(c)
print(len(message))
print(sorted(message))
print("第三个字条是" + message[2])
me = message.count("l")
if me == 0:
    print("所查询的字符串为空")
else:
    print("你查询的字符串的次数是%d次" % me)
print(message.index("l"))
if message.isalpha():
    print("只包括字符串")
print(message.title())
print(message.upper())
print(message.lower())

print(message1.isspace())
