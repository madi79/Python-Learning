a = input("请输入英文：")
while a.isalpha()!=True:
    print("输入错误，请重新输入")
    a = input("请输入英文")
else:
    print("输出结果为："+a[1:len(a)]+str("-")+str(a[0]))