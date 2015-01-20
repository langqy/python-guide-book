from setuptools import setup ,Extension
from setuptools import  find_packages


PATH_example = 'example/example/'
SOURCES_example = [PATH_example + i for i in ['example.i','example.c']]

setup(
    name = 'example',
    version = '0.01',
    ext_modules = [Extension('example/example/_example', sources=SOURCES_example,swig_opts=['-modern', '-I../include'])],
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
)



