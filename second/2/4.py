# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ixSfqcocca7JwLShWBFNnt1hF0P9nktD
"""

import numpy as np

matritsa = np.tile(np.arange(1, 11), (10, 1))

sums = np.sum(matritsa, axis=0)
print(sums)