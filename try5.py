# coding = utf-8
# def sortPop(data):
#     length = len(data)
#     for i in range(length-1):
#         for j in range(i):
#             if data[j] > data[j+1]:
#                 temp = data[j]
#                 data[j] = data[j+1]
#                 data[j+1] = temp
#                 # data[j], data[j+1] = data[j+1], data[j]
#     return data
#
# a = input("请输入：")
# print(a)
# list1 = a.split(",")
# results = sortPop(list1)
# print(results)


def bubbleSort(nums):
    for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [5,2,45,6,8,2,1]
# 5,2,45,6,8,2,1
print(bubbleSort(nums))