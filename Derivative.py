# -*- coding: utf-8 -*-
"""derivative.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14RZNIZbEnG9ZP_VQiE9YlslWH9nlrNdJ
"""

import sympy

J, W =sympy.symbols('J, W')

J = W **2
J

dJ_dW = sympy.diff(J, W)
dJ_dW

dJ_dW.subs([(W, 2)])

J = W **3
J

dJ_dW = sympy.diff(J, W)
dJ_dW

dJ_dW.subs([(W, 2)])

J = 1/ W
J

dJ_dW = sympy.diff(J, W)
dJ_dW

dJ_dW.subs([(W, 2)])

