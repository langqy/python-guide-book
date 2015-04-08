
def tostr(item):
    return str(item)

list001 = ['a','ab','A',123,124,5]

list001.sort(key=tostr)

print(list001)

