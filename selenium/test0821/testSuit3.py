import unittest
from test0821 import testbaidu1
from test0821 import testbaidu2

def createsuite():
    # TestLoader
    suite1 = unittest.TestLoader.loadTestsFromTestCase(testbaidu1.Baidu1)
    suite2 = unittest.TestLoader.loadTestsFromTestCase(testbaidu2.Baidu2)
    suite = unittest.TestSuite([suite1, suite2])
    return suite

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity = 0,1,2
    runner.run(suite)