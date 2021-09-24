import unittest
import mathstein


class TestMathstein(unittest.TestCase):
    
    def test_OneVarSolver(self):
        result1=mathstein.OneVarSolver("x+5-3+x=6+x-2")
        self.assertEqual(result1,2)
        result2=mathstein.OneVarSolver("x=x")
        self.assertEqual(result2,"Infinite solutions")
        result3=mathstein.OneVarSolver("x=x+2")
        self.assertEqual(result3,"No solution")
    def test_MultiVarSolver(self):
        result1=mathstein.MultiVarSolver(['- 3x + y = -1','4x + y = -8'],2)
        self.assertEqual(result1,[-1.0,-4.0])
        result2=mathstein.MultiVarSolver(['2x + y = 2','4x + 2y = -8'],2)
        self.assertEqual(result2,"No solution possible")
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
