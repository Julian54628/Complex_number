import unittest
from complex_number import
class TestComplexFunctions(unittest.TestCase):
    def test_complex_sum(self):
        self.assertEqual(complex_sum((4,2),(7,9),(11,11))
        self.assertEqual(complex_sum((11,6),(10,9),(21,15))
                         
    def test_complex_rest(self):
        self.assertEqual(complex_rest((4,2),(7,9),(-3,-7))
        self.assertEqual(complex_rest((11,6),(10,9),(1,-3))
                         
    def test_complex_multiplication(self):
        self.assertEqual(complex_multiplication((7,9),(10,26),(-164,272))
        self.assertEqual(complex_multiplication((9,0),(3,20),(27,180))
                         
    def test_complex_division(self):
        self.assertEqual(complex_division((4,2),(7,9),((46/3969),-(22/3969)))
        self.assertEqual(complex_division((11,6),(10,9),((41/2025),-(13/2700)))
                         
    def test_complex_module(self):
        self.assertEqual(complex_module((7,9),math.sqrt(130))
        self.assertEqual(complex_module((10,9),math.sqrt(181))
                         
    def test_complex_conjugated(self):
        self.assertEqual(complex_conjugated((4,2),(4,-2))
        self.assertEqual(complex_conjugated((11,6),(11,-6))
                         
    def test_Cartesian_to_polar(self):
        self.assertEqual(Cartesian_to_polar((1,1),(math.sqrt(2),math.pi/4))
        self.assertEqual(Cartesian_to_polar((1,0),(1,0))
                         
    def test_polar_to_Cartesian(self):
        self.assertEqual(polar_to_Cartesian((math.sqrt(3),math.pi/4),((math.sqrt(6)/2),(math.sqrt(6)/2)))
        self.assertEqual(polar_to_Cartesian((1,math.pi/2),(0,1))
                         
                         
