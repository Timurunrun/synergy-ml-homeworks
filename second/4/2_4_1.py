# -*- coding: utf-8 -*-
"""2_4_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18wm3P0028DPKqNglwQfIFNk-i2TMWssc
"""

import pandas as pd

customers = pd.read_csv("Customers.csv", sep=';')

select_f = customers[(customers['Age'] > 30) & (customers['Income'] < 30000)]

select_s = customers[(customers['Profession'] == 'Lawyer') & (customers['Work Experience'] > 5)]

print(select_f)
print(select_s)