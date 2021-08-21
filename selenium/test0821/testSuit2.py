import unittest
from test0821 import testbaidu1

def createsuite():
    # makeSuite  添加所有类里脚本
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(testbaidu1.Baidu1))
    return suite

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity = 0,1,2
    runner.run(suite)