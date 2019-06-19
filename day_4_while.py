catic = True
while catic:
    enter = input("请输入一个数字，输入quit退出计算： ")
    enter1 = input("请再输入一个数字，输入quit退出计算： ")
    # while enter or enter1 != "quit" :
    sum = int(enter) + int(enter1)
    #   print("这两个数字的和是： %d" %sum)
    report = input("是否继续参与计算，如果是输入Yes，否则输入No :")
    if report == "No":
        catic = False
    print("这两个数字的和是： %s + %s =%s " % (enter, enter1, sum))
