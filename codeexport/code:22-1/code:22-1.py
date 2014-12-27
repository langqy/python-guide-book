
from collections import namedtuple

Point3d=namedtuple('Point3d',['x','y','z'])
p1=Point3d(0,1,2)
print(p1)
print(p1[0],p1.z)

