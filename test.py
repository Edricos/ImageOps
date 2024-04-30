#输入三角形的三边长
a,b,c = (input("请输入三角形三边的长：").split())
a= int(a)
b= int(b)
c= int(c)

#计算三角形的半周长p
p=(a+b+c)/2

#计算三角形的面积s
s=(p*(p-a)*(p-b)*(p-c))**0.5

#输出三角形的面积
print("三角形面积为：",format(s,'.2f'))