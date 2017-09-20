# coding = utf-8

# 九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}x{}={}\t'.format(i, j, i * j), end='')
#     print()
# 斐波那契数列
# num = float(input("输入一个大于0的整数："))
# n1, n2 = 0, 1
# count = 2
# print(n1, n2, end=",")
# while count <= num:
#     jia = n1 + n2
#     print(jia, end=",")
#     n1 = n2
#     n2 = jia
#     count += 1


num = int(input("请输入要检测的数字:"))
sum = 0
n = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if num == sum:
    print("是阿姆斯特朗数")
else:
    print("不是阿姆斯特朗数")

