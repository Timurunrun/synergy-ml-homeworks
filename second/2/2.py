# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixSfqcocca7JwLShWBFNnt1hF0P9nktD
"""

import numpy as np

res = []

for _ in range(1000):
    vec = np.random.randint(1, 11, size=100)
    a = np.mean(vec > 7) * 100
    res.append(a)

tw = np.sum(np.array(res) == 20) #вторая часть
print(f"Процент: {tw /1000:.2}")