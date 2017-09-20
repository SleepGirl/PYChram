# coding = utf-8
from selenium import webdriver
import codecs
'''vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
a = [x*y for x in vec1 for y in vec2]
print(a)
b = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(b)
'''
# 将3X4的矩阵转换成4X3 的矩阵
dr = webdriver.Chrome()
dr.implicitly_wait(5)

def transfer_matrix():
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
    a = [[row[i] for row in matrix] for i in range(4)]
    print(a)
    transposed = []
    for i in range(4):
        transposed.append([row[i] for row in matrix])
        print(transposed)

# def main():
#     pageNum = 10
#     i = 1
#     article_file = codecs.open("articles.txt",'a','utf-8')
#     while(i <= pageNum):
#         dr.get("")


