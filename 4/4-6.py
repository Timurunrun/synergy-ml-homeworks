# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uMomGuaIo63VssMAeq6FEfzSLP44oI8Z
"""

input_string = input()
open_bracket_index = input_string.find("(")

while open_bracket_index != -1:
    close_bracket_index = input_string.find(")", open_bracket_index)
    content_inside_brackets = input_string[open_bracket_index + 1:close_bracket_index]
    print(content_inside_brackets)
    open_bracket_index = input_string.find("(", close_bracket_index)