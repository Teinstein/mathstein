#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math,cmath
import numpy as np
import matplotlib.pyplot as plt


def OneVarSolver(lin_equation) :
    """
    Solves single variable linear equation
        :param lin_equation: linear equation with single variable in the form of a string
        :return: Solution of the equation
    """
    len_of_eqn = len(lin_equation)  
    sign = 1
    coeff = 0
    total = 0
    i = 0  
    for j in range(0, len_of_eqn) :
      
        if (lin_equation[j] == '+' or lin_equation[j] == '-') :
            if (j > i) :
                total = (total + sign * int(lin_equation[i:j]))
            i = j
          
        
        elif (lin_equation[j] == 'x') :
          
            if ((i == j) or lin_equation[j - 1] == '+') :
                coeff += sign
            elif (lin_equation[j - 1] == '-') :
                coeff = coeff - sign
            else :
                coeff = (coeff + sign * int(lin_equation[i: j]))
            i = j + 1
          
        elif (lin_equation[j] == '=') :
            if (j > i) :
                total = (total + int(lin_equation[i: j]))
            sign = -1
            i = j + 1
          
    if (i < len_of_eqn) :
        total = (total + sign * int(lin_equation[i: len(lin_equation)]))
  
    
    if (coeff == 0 and total == 0) :
        return "Infinite solutions"
  
    
    if (coeff == 0 and total) :
        return "No solution"
  
    ans = -total / coeff
    return int(ans)

def get_index(d, c):
    if c in d.keys():
        return d[c] 
    else:
        return -1
    
def coeffgen(eqn,degree):
    s=1 
    n_fg = 0 
    eq_fg = 0 
    s_fg = 0 
    letter = '' 
    coef =''
    curr_idx = 0
    N = degree

    letter_idx = {}

    mat = [[0 for i in range(N+1)] for i in range(N)]

    for i in range(N):
        l=eqn[i]
        coef = ''
        eq_fg = 0
        s_fg = 0
        s = 1
        ls = len(l)
        k = 0 

        for c in l:

            if c == '-':
                s_fg = 1
                s=-1
            elif c == '+':
                s_fg = 1
                s = 1
            elif c.isalpha():
                if n_fg == 0:
                    coef = 1
                letter = c
            elif c.isdigit():
                n_fg = 1
                coef += c

                if k == ls-1:
                    if coef is '':
                        coef = 1
                    coef = s*int(coef)
                    if eq_fg == 0:
                        j = get_index(letter_idx,letter)
                        if j == -1:
                            j = curr_idx
                            letter_idx[letter] = j
                            curr_idx+=1
                    else:
                        j = N
                    mat[i][j] = coef

            elif (c == ' ' and s_fg != 1) :
                if coef is '':
                    coef = 1
                coef = s*int(coef)
                if eq_fg == 0:
                    j = get_index(letter_idx,letter)
                    if j == -1:
                        j = curr_idx
                        letter_idx[letter] = j
                        curr_idx+=1
                else:
                    j = N
                mat[i][j] = coef
                coef = ''
                n_fg = 0
            elif c == ' ' and s_fg == 1:
                s_fg = 0
            elif c == '=':
                eq_fg = 1
                s_fg = 1
                s = 1
            k+=1
    print(mat)
    return mat
            
def MultiVarSolver(equations,n):
    """
    Solves multiple linear equation with n variables
        :param equations: list of multiple linear equations
        :param n: Number of equations/ Number of unknowns
        :return: Solution of these equations
    """
    resultant= coeffgen(equations,n)
    A=[]
    B=[]
    for i in resultant:
        lst_len=len(i)
        A.append(i[:lst_len-1])
        B.append(i[lst_len-1])
    a=np.array(A)
    b=np.array(B)
    det = int(np.linalg.det(A))
    if(det==0):
        return "No solution possible"
    inver_arr=np. linalg. inv(a)
    ans= np.dot(inver_arr,b)
    return list(ans)


# In[ ]:





# In[ ]:




