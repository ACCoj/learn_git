# a. 计算圆的面积（输入半径，输出面积）。
from math import pi
#输入错误循环处理，直到输入有效半径跳出循环，再进行计算
while True:
    print("请输入圆的半径:")
    radius = float(input())
    if radius<=0 :
        print("请重新输入有效的半径")
        continue
    print(radius,type(radius))
    break
# 面积公式：π*r²
area = pi*radius**2
print("圆的面积约为：",area)

