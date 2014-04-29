
from random import *
def random_list_max(n):
    y=[randint(1,n) for x in range(10000)]
    list_count=[y.count(x) for x in range(1,n+1)]
    return list_count.index(max(list_count))+1

print(random_list_max(40))

