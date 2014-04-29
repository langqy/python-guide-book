
def square(n):
    return n*n

print(map(square,[1,2,3,4,5]))
print([square(x) for x in [1,2,3,4,5]])

