from setuptools import setup ,Extension

setup(
    name = 'example',
    version = '0.01',
    ext_modules = [Extension('_example', ['example.i','example.c'],swig_opts=['-modern', '-I../include'])],
    py_modules = ['example']
)



