
def removeduplicate(list):
    newlist = list.copy()
    for j in newlist:
        for index in range(newlist.index(j)+1,len(newlist)-1):
            if j == newlist[index]:
                del newlist[index]
                return removeduplicate(newlist)
    return newlist

list001=[1,2,3,1,2,4,4,5,5,5,7]
print(removeduplicate(list001))

