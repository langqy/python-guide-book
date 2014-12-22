swig -python example.i

gcc -fpic -c example.c example_wrap.c -I/usr/include/python3.4m

gcc -shared example.o example_wrap.o -o _example.so

