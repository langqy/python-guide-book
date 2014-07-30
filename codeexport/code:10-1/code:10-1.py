
import os,sys
sys.path.append(os.environ['HOME']+'/pymf')
from pyconfig import *

import mymodule.mymod

mymodule.mymod.myfun()

