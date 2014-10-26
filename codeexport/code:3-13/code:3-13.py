
def subst(list001,element001,element002):
    try:
        list001.index(element001)
    except ValueError:
        return list001
    else:
        n=list001.index(element001)
        del list001[n]
        list001[n:n]=[element002]
        return subst(list001,element001,element002)

print(subst([1,'a',3,[4,5]],[4,5],'b'))
print(subst([1,1,5,4,1,6],1,'replaced'))

