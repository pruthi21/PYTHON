Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x='hello'
>>> y='world'
>>> print(*2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(*2)
TypeError: print() argument after * must be an iterable, not int
>>> print(x,y)
hello world
>>> x='pruthi'
>>> print(x(1))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(x(1))
TypeError: 'str' object is not callable
>>> my_string = 'hello world'
>>> length= len(my_string)
>>> print(length)
11
>>> a= 'pruthika'
>>> length= len(a)
>>> print(length)
8
>>> b='shivam'
>>> length= len(b)
>>> print(length)
6
>>> d= 'shivam'
>>> e= 'jaiswal'
>>> print(d,e)
shivam jaiswal
