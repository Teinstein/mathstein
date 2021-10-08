#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import numpy as np

def f(function,x):
    y=eval(function)
    return y

def areadisplay(function,limits):
    """
    Shows a visual representation of area under a line or a curve
        :param function: string which denotes the equation of the line or curve
        :param limits: limits between which the area needs to be calculated
        :return: Graphical object denoting area under a line or a curve
    """
    x=np.linspace(-10,10,1000)
    plt.plot(x,f(function,x))
    plt.axhline(color="black")
    plt.fill_between(x,f(function,x),where=[(x>limits[0]) and (x<limits[1]) for x in x])
    
def areacalculator(function,limits):
    """
    Calculates area covered by a line or a curve
        :param function: string which denotes the equation of the line or curve
        :param limits: limits between which the area needs to be calculated
        :return: Area under line or curve
    """
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



