# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AvEv2h55z2QAGcnocBMbC_tgMeaU70Al
"""

numbers = list(map(int, input().split()))
n = numbers.pop(-1)

result = [num ** n for num in numbers]

print(result)