#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import mathstein


class TestMathstein(unittest.TestCase):
    
    def test_quadraticsolver(self):
        result1=mathstein.quadraticsolver((1,0,-4,0))
        self.assertEqual(result1,(2.0,-2.0))
        result2=mathstein.quadraticsolver((1,0,4,0))
        self.assertEqual(result2,"No real root possible")
    def test_cubicsolver(self):
        result1=mathstein.cubicsolver((1,0,0,-27,0))
        self.assertEqual(result1,3)
        result2=mathstein.cubicsolver((1,0,0,27,0))
        self.assertEqual(result2,"No real root possible")
    def test_biquadraticsolver(self):
        result1=mathstein.biquadraticsolver((1,0,0,0,0,16))
        self.assertEqual(result1,[-4.0, 4.0])
        result2=mathstein.biquadraticsolver((1,0,0,0,0,-16))
        self.assertEqual(result2,"No real root possible")
        

if __name__=='__main__':
    unittest.main()

