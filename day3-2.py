# Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license()" for more information.
# i = "A"
# while(i<="Z"):
#     print(i)
#     i+=1
#
#
# A
# Traceback (most recent call last):
#   File "<pyshell#4>", line 3, in <module>
#     i+=1
# TypeError: can only concatenate str (not "int") to str
# i = "A"
# while(i<="Z"):
#     print(i)
#     i = chr(ord(letter)+1)
#
#
# A
# Traceback (most recent call last):
#   File "<pyshell#7>", line 3, in <module>
#     i = chr(ord(letter)+1)
# NameError: name 'letter' is not defined
# i = "A"
# while(i<="Z"):
#     print(i)
#     i = chr(ord(i)+1)
#
#
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J
# K
# L
# M
# N
# O
# P
# Q
# R
# S
# T
# U
# V
# W
# X
# Y
# Z
# str = "The quick brown fox jumps over the lazy dog"
# str = str.split("")
# Traceback (most recent call last):
#   File "<pyshell#12>", line 1, in <module>
#     str = str.split("")
# ValueError: empty separator
# str = "The quick brown fox jumps over the lazy dog"
# str = str.split(" ")
# str
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# " ".join(str)
# 'The quick brown fox jumps over the lazy dog'
# str = " ".join(str)
# for i in str:
#     if i is not " ":
#
# KeyboardInterrupt
# str
# 'The quick brown fox jumps over the lazy dog'
# str_list = []
#
#
# for i in str:
#     if i not in str_list:
#         str_list.append(i)
#
#
# str_list()
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     str_list()
# TypeError: 'list' object is not callable
# str_list
# ['T', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g']
# str_list.sort()
# str_list()
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     str_list()
# TypeError: 'list' object is not callable
# str_list
# [' ', 'T', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# str_list = []
# for i in str:
#     if i not in str_list and i is not " ":
#         str_list.append(i.lower())
#
#
# str_list
# ['t', 'h', 'e', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x', 'j', 'm', 'p', 's', 'v', 'l', 'a', 'z', 'y', 'd', 'g']
# str_list.sort()
# str_list
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# i = 'a'
# alpha_list = []
# while(i<='z'):
#     alpha_list.append(i)
#     i = chr(ord(i)+1)
#
#
# alpha_list
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# alpha_list == str_list
# True
#
#
# str1 =  'naman'
# str2 = 'aman'
# str2 = 'manan'
# for i in str1:
#     str1.split()
#
#
# ['naman']
# ['naman']
# ['naman']
# ['naman']
# ['naman']
#
# str1.sort() == str2.sort()
# Traceback (most recent call last):
#   File "<pyshell#56>", line 1, in <module>
#     str1.sort() == str2.sort()
# AttributeError: 'str' object has no attribute 'sort'
# str1_list = []
# str2_list = []
# for i in str:
#     if i not in str_list and i is not " ":
#         str_list.append(i.lower())
#
#
# str1.sort() == str2.sort()
# Traceback (most recent call last):
#   File "<pyshell#61>", line 1, in <module>
#     str1.sort() == str2.sort()
# AttributeError: 'str' object has no attribute 'sort'
#
# str1
# 'naman'
# str1_list
# []
# for i in str:
#     if i not in str1_list and i is not " ":
#         str_list.append(i.lower())
#
#
# for i in str1:
#     if i not in str1_list and i is not " ":
#         str_list.append(i.lower())
#
#
# for i in str2:
#     if i not in str2_list and i is not " ":
#         str_list.append(i.lower())
#
#
# str1_list
# []
# for i in str1:
#     if i not in str1_list and i is not " ":
#         str1_list.append(i.lower())
#
#
# for i in str2:
#     if i not in str2_list and i is not " ":
#         str2_list.append(i.lower())
#
#
# str1_list
# ['n', 'a', 'm']
#
# str2_list
# ['m', 'a', 'n']
#
# str1_list.sort() == str2_list.sort()
# True
#
# snake = the_new_class
# Traceback (most recent call last):
#   File "<pyshell#82>", line 1, in <module>
#     snake = the_new_class
# NameError: name 'the_new_class' is not defined
# snake = "the_new_class"
# >>> camel = "TheNewClass"
# >>> camel = "TheNewClass"
# >>> KeyboardInterrupt
# >>> snake
# 'the_new_class'
# >>> camel_case
# Traceback (most recent call last):
#   File "<pyshell#87>", line 1, in <module>
#     camel_case
# NameError: name 'camel_case' is not defined
# >>> sanke = snake.split("_")
# >>> snake
# 'the_new_class'
# >>> sanke
# ['the', 'new', 'class']
# >>> camel_list = []
# >>> for i in camel_case:
# ...
# KeyboardInterrupt
# >>> for i in sanke:
# ...     camel_list.append(replace_at_index(i, 0, i[0].upper()))
# ...
# ...
# Traceback (most recent call last):
#   File "<pyshell#95>", line 2, in <module>
#     camel_list.append(replace_at_index(i, 0, i[0].upper()))
# NameError: name 'replace_at_index' is not defined
# >>> for i in sanke:
# ...     camel_list.append(i[0]+i[1:])
# ...
# ...
# >>> sanke
# ['the', 'new', 'class']
# >>> camel_list
# ['the', 'new', 'class']
# >>> for i in sanke:
# ...     camel_list.append(i[0].upper()+i[1:])
# ...
# ...
# >>> camel_case
# Traceback (most recent call last):
#   File "<pyshell#105>", line 1, in <module>
#     camel_case
# NameError: name 'camel_case' is not defined. Did you mean: 'camel_list'?
# >>> camel_list
# ['the', 'new', 'class', 'The', 'New', 'Class']
# >>> camel_list = []
# >>> for i in sanke:
# ...     camel_list.append(i[0].upper()+i[1:])
# ...
# ...
# >>> camel_list
# ['The', 'New', 'Class']
# >>> "".join(camel_list)
# 'TheNewClass'
# >>>
# >>>
# >>> weekdays = ["M", "T", "W", "T", "F", "S", "S"]
# >>>
# >>> days = 31
# >>>
# >>> startDay = 4
# >>>
