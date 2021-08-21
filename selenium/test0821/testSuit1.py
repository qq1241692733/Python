import unittest
from test0821 import testbaidu1, testbaidu2


def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(testbaidu1.Baidu1("test_hao"))
    suite.addTest(testbaidu1.Baidu1("test_baidu"))
    suite.addTest(testbaidu2.Baidu2("test_hao"))
    suite.addTest(testbaidu2.Baidu2("test_baidu"))
    return suite

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity = 0,1,2
    runner.run(suite)
