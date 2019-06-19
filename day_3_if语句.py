today_money = float(input("请输入今日工资金额： "))

if not 5000 > today_money:
    today_cords = float(input("明天还贷款： "))
    money = today_money - today_cords
    print("今天可以还款了%.2f,这个月可支出的钱是%.2f" %(today_cords,money)  )
else:
    print("穷鬼你的信用卡都还不上了")
print(20 * "_"  +"\n离好日子还远着呢")

# if today_money != 5000 :
#     print("只能混日子了")

