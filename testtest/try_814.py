# coding = utf-8
# import sys
# 异常处理
# # while True:
# #     try:
# #         x = int(input("please input a number: "))
# #         break
# #     except ValueError:
# #         print("Oops! This is not a valid number, try again")
# 文件读写
# fo = open("articles.txt","r+")
# print("文件名：", fo.name)
#
# str1 = '12'
# line = fo.write(str1)
# try:
#     f = open('articles.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Not a valid integer")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
# 类继承，方法重写等
# class Parent:  # 定义父类
#     def myMethod(self):
#         print('调用父类方法')
# class Child(Parent):  # 定义子类
#     def myMethod(self):
#         print('调用子类方法')
#
# c = Child()
# c.myMethod()

year = int(input("输入一个年份: "))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
        else:
            print("{0} 不是闰年".format(year))
    else:
        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
    print("{0} 不是闰年".format(year))