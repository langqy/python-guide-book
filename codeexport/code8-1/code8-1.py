
x1 = ['a','b','c','e']
x2 = [1,2,3,4]
y = dict(zip(x1,x2))
print('列表到字典：',y)
new_x1,new_x2 = zip(*y.items())
print(new_x1,new_x2)

