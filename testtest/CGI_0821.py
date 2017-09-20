# coding = utf-8

# suma = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i!=j) and (j!=k) and (i!=k):
#                 print(i, j, k)
#                 suma +=1
# print(suma)

# 根据收益计算奖金
# num = float(input("请输入计算金额（万元）："))
# bons = 0
# if num <= 10:
#     bons = num * 0.01
# elif 10< num <= 20:
#     bons = 10 * 0.1 + (num - 10) * 0.075
# elif 20< num <= 40:
#     bons = 10 * 0.1 + 10 * 0.075 + (num - 20) * 0.05
# elif 40< num <= 60:
#     bons = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (num - 40) * 0.03
# elif 60< num <= 100:
#     bons = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (num - 60) * 0.015
# else:
#     bons = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (num - 100)*0.01
#
# print(bons)

# i = int(input("请输入纯利润："))
# r = 0
# arr = [100, 60, 40, 20, 10, 0]
# rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
# r = 0
# for idx in range(0, 6):
#     if i > arr[idx]:
#         r += (i - arr[idx]) * rat[idx]
#         i = arr[idx]
# print(r)

# 一个整数加上100后是一个完全平方数数，再加上168 还是一个完全平方数，求满足条件的这个整数
# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168//i
#         if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
#             m = (i+j)//2
#             n = (i-j)//2
#             x = n*n - 100
#             print(i,j,n,m,x)
# for m in range(168):
#     for n in range(m):
#         if (m+n)*(m-n) == 168:
#             x = n**2-100
#             print(x)


# 输入一个日期，计算出这是当年的第几天
# year = int(input('year:'))
# month = int(input('month:'))
# day = int(input('day:'))
# months = [0,31,59,90,120,151,181,212,243,273,304,334]
# if 0< month <=12:
#     days = months[month-1]
# else:
#     print('data error')
# days += day
# leap = 0
# if year%400==0 or year%4==0 and year%100 !=0:
#     leap = 1
# if leap ==1 and month>2:
#     days += 1
# print('这是今年的第%d天'%days)
# print('这是今年的第'+ str(days) + '天')

# 排序
# l = []
# for i in range(0,3):
#     x = int(input('输入数字：'))
#     l.append(x)
# l.sort()
# print(l)

a = [1,2,3,4]
# b = a.copy()
# b = a[:]
b = []
for i in range(len(a)):
    b.append(a[i])
print(b)