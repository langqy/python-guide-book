
lst = [[1,2,[3]],[4,[5,[[[[10],11]]]],(1,2,3)],[{'a','b','c'},8,9]]

def is_list(thing):
    return isinstance(thing, list)

def flatten(iter):
    templst = []
    for x in iter:
        if not is_list(x):
            templst.append(x)
        else:
            templst += flatten(x)
    return templst

print(flatten(lst))

