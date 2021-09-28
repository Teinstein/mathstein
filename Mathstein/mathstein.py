#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math,cmath
import numpy as np
import matplotlib.pyplot as plt


def f(function,x):
    y=eval(function)
    return y

def areadisplay(function,limits):
    x=np.linspace(-10,10,1000)
    plt.plot(x,f(function,x))
    plt.axhline(color="black")
    plt.fill_between(x,f(function,x),where=[(x>limits[0]) and (x<limits[1]) for x in x])
    
def areacalculator(function,limits):
    x1=limits[0]
    x2=limits[1]
    N=1000
    dx=(x2-x1)/N
    A=0
    x=x1
    while x<=x2:
        dA=f(function,x)*dx
        A=A+dA
        x=x+dx
    return A

def graphgen(coeff):
    x = np.linspace(-10, 10, 1000)
    y=0
    degree=len(coeff)-1
    #graph of a quadratic polynomial
    if degree==3:
        a,b,c,d=coeff
        c=c-d
        y=a*(x**2)+b*x+c
        fig, ax = plt.subplots()
        ax.plot(x, y)
        return
    #graph of a cubic polynomial
    elif degree==4:
        a,b,c,d,e=coeff
        d=d-e
        y=a*(x**3)+b*(x**2)+c*x+d
        fig, ax = plt.subplots()
        ax.plot(x, y)
        return
    #graph of a biquadratic polynomial
    else:
        a,b,c,d,e,f=coeff
        e=e-f
        y=a*(x**4)+b*(x**3)+c*(x**2)+d*x+e
        fig, ax = plt.subplots()
        ax.plot(x, y)
        return   
      
def quadraticsolver(coeff):
    a,b,c,d=coeff
    c=c-d
    if a==0:
        return "Invalid equation"
    dis=b*b-4*a*c
    discrimi=math.sqrt(abs(dis))#FInding the discriminant
    #based on the discriminant checking if solution exist or not
    if dis > 0:
        r1=(-b + discrimi)/(2 * a)
        r2=(-b - discrimi)/(2 * a)
        return r1,r2
    elif dis == 0:
        return -b / (2*a)
    else:  
        return "No real root possible"
    
def accessory_cubic(A, B, C, D, x) :
 
    ans = 0
 
    # Find the value equation at x
    ans = (A * x * x * x +
           B * x * x + C * x + D)
 
    # Return the value of ans
    return ans
 

def cubicsolver(coeff) :
    # Initialise start and end
    A, B, C, D, E=coeff
    start = 0 
    end = 100000
 
    mid = 0
    ans = 0
 
    # Implement Binary Search
    while (start <= end) :
 
        # Find mid
        mid = start + (end - start) // 2
 
        # Find the value of f(x) using
        # current mid
        ans = accessory_cubic(A, B, C, D, mid)
 
        # Check if current mid satisfy
        # the equation
        if (ans == E) :
 
            # Print mid and return
            return mid
 
        if (ans < E) :
            start = mid + 1
        else :
            end = mid - 1
 
    # Print "No real root possible" if not found
    # any integral solution
    return "No real root possible"

def accesory_biquadratic1(a0, b0, c0):
    a, b = b0 / a0, c0 / a0

    # Some repating variables
    a0 = -0.5*a
    delta = a0*a0 - b
    sqrt_delta = cmath.sqrt(delta)

    # Roots
    r1 = a0 - sqrt_delta
    r2 = a0 + sqrt_delta

    return r1, r2


def accesory_biquadratic2(a0, b0, c0, d0):
    a, b, c = b0 / a0, c0 / a0, d0 / a0

    # Some repeating constants and variables
    third = 1./3.
    a13 = a*third
    a2 = a13*a13

    # Additional intermediate variables
    f = third*b - a2
    g = a13 * (2*a2 - b) + c
    h = 0.25*g*g + f*f*f

    def cubic_root(x):
        if x.real >= 0:
            return x**third
        else:
            return -(-x)**third

    if f == g == h == 0:
        return -cubic_root(c)

    elif h <= 0:
        j = math.sqrt(-f)
        k = math.acos(-0.5*g / (j*j*j))
        m = math.cos(third*k)
        return 2*j*m - a13

    else:
        sqrt_h = cmath.sqrt(h)
        S = cubic_root(-0.5*g + sqrt_h)
        U = cubic_root(-0.5*g - sqrt_h)
        S_plus_U = S + U
        return S_plus_U - a13
    
def biquadraticsolver(coeff):
    a0,b0,c0,d0,e0,f0=coeff
    e0=e0-f0
    a, b, c, d = b0/a0, c0/a0, d0/a0, e0/a0

    # Some repeating variables
    a0 = 0.25*a
    a02 = a0*a0

    # Coefficients of subsidiary cubic euqtion
    p = 3*a02 - 0.5*b
    q = a*a02 - b*a0 + 0.5*c
    r = 3*a02*a02 - b*a02 + c*a0 - d

    # One root of the cubic equation
    z0 = accesory_biquadratic2(1, p, r, p*r - 0.5*q*q)

    # Additional variables
    s = cmath.sqrt(2*p + 2*z0.real + 0j)
    if s == 0:
        t = z0*z0 + r
    else:
        t = -q / s

    # Compute roots by quadratic equations
    r0, r1 = accesory_biquadratic1(1, s, z0 + t)
    r2, r3 = accesory_biquadratic1(1, -s, z0 - t)

    lst=[r0 - a0, r1 - a0, r2 - a0, r3 - a0]
    arr=np.iscomplex(lst)
    ans=[]
    for i in range(len(arr)):
        if arr[i]==False:
            ans.append(lst[i].real)
    if len(ans)==0:
        return "No real root possible"
    else:
        return ans

def OneVarSolver(lin_equation) :
  
    len_of_eqn = len(lin_equation)  
    sign = 1
    coeff = 0
    total = 0
    i = 0  
    # Traverse the equation
    for j in range(0, len_of_eqn) :
      
        if (lin_equation[j] == '+' or lin_equation[j] == '-') :
            if (j > i) :
                total = (total + sign * int(lin_equation[i:j]))
            i = j
          
        # For cases such 
        # as: x, -x, +x
        elif (lin_equation[j] == 'x') :
          
            if ((i == j) or lin_equation[j - 1] == '+') :
                coeff += sign
            elif (lin_equation[j - 1] == '-') :
                coeff = coeff - sign
            else :
                coeff = (coeff + sign * int(lin_equation[i: j]))
            i = j + 1
          
        # Flip sign once 
        # '=' is seen
        elif (lin_equation[j] == '=') :
            if (j > i) :
                total = (total + int(lin_equation[i: j]))
            sign = -1
            i = j + 1
          
    # There may be a number
    # left in the end
    if (i < len_of_eqn) :
        total = (total + sign * int(lin_equation[i: len(lin_equation)]))
  
    # For infinite solutions
    if (coeff == 0 and total == 0) :
        return "Infinite solutions"
  
    # For no solution
    if (coeff == 0 and total) :
        return "No solution"
  
    # x = total sum / coeff of x
    # '-' sign indicates moving
    # numeric value to right hand side
    ans = -total / coeff
    return int(ans)

def get_index(d, c):
    if c in d.keys():
        return d[c] 
    else:
        return -1
    
def coeffgen(eqn,degree):
    s=1 #sign
    n_fg = 0 #number exist
    eq_fg = 0 #equal flag
    s_fg = 0 #sign flag
    letter = '' # store current letter (variable)
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
        k = 0 # position in line str

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

