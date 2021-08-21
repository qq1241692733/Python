import unittest
import time

def createsuite():
    # discover
    discovers = unittest.defaultTestLoader.discover("../test0821", pattern="testbaidu*.py", top_level_dir=None)
    return discovers

if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity = 0,1,2
    runner.run(suite)