#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import mathstein


class TestMathstein(unittest.TestCase):
    
    def test_areacalculator(self):
        result1=mathstein.areacalculator("x**3",[1,2])
        self.assertEqual(result1,3.75450074999953)
        result2=mathstein.areacalculator("3*x**2+2",[1,2])
        self.assertEqual(result2,9.009500499999444)

if __name__=='__main__':
    unittest.main()

    
    


# In[ ]:




