import unittest

class TestAtLeastSomething(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('sun'.upper(), 'SUN')
        
    def test_purum(self):
        self.assertGreater(5, 3, "no")
        
    def test_burum(self):
        a_dict={'location':'SPb','place':'restaurant'}
        b_dict={'place':'restaurant'}
        self.assertDictContainsSubset (b_dict, a_dict)
        
    def test_float(self):
        a=5
        b='{0:.3f}'.format(a)
        c='{0:.4f}'.format(a)
        b_float=float(b)
        c_float=float(c)
        d=5.0005
        self.assertAlmostEqual(b_float,d,3)
        self.assertAlmostEqual(b_float,c_float,4)
            
if __name__ == '__main__':
    unittest.main()