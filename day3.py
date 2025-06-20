Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> str = "hello i am python beginnner. The first program is hello world"
>>> count_dict = {}
>>> for i in str:
...     if count_dict[i]:
...         count_dict[i] +=1
...     else:
...         count_dict[i] = 1
... 
...         
Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    if count_dict[i]:
KeyError: 'h'
>>> str = "hello i am python beginnner. The first program is hello world"
>>> count_dict = {}
>>> for i in str:
...     if i in count_dict:
...         count_dict[i] +=1
...     else:
...         count_dict[i] = 1
... 
...         
>>> count_dict
{'h': 4, 'e': 5, 'l': 5, 'o': 5, ' ': 10, 'i': 4, 'a': 2, 'm': 2, 'p': 2, 'y': 1, 't': 2, 'n': 4, 'b': 1, 'g': 2, 'r': 5, '.': 1, 'T': 1, 'f': 1, 's': 2, 'w': 1, 'd': 1}
>>> str = str.split(" ")
>>> str
['hello', 'i', 'am', 'python', 'beginnner.', 'The', 'first', 'program', 'is', 'hello', 'world']
>>> count_dict = {}
>>> for i in str:
...     if i in count_dict:
...         count_dict[i] +=1
...     else:
...         count_dict[i] = 1
... 
...         
>>> count_dict
{'hello': 2, 'i': 1, 'am': 1, 'python': 1, 'beginnner.': 1, 'The': 1, 'first': 1, 'program': 1, 'is': 1, 'world': 1}
