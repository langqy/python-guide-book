
import os,sys
sys.path.append(os.environ['HOME']+'/pymf')
from pyconfig import *

print([fib(n) for n in range(10)])

