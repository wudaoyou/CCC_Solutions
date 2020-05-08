import unittest
import os
from bin.util import *
from pathlib import Path
from foo.ccc2020.J1 import *


class simple_test(unittest.TestCase):
    def setUp(self):
        print('@@@ initialize @@@')
        self.a = dogTreat

    def test_one(self):
        n = 1
        print('first test case')
        test_paths = find_pattern('j1.01*.in', find_dir('test_2020'))
        result_paths = find_pattern('j1.01*.out', find_dir('test_2020'))
        for i in range(len(test_paths)):
            test_object = open(test_paths[i])
            result_object = open(result_paths[i])
            t = test_object.readlines()
            t = list(map(int, t))
            r = result_object.readlines()
            test_object.close()
            result_object.close()
            self.assertEqual(self.a(t[0], t[1], t[2]), r[0])
            print('test case %d OK' % n)
            n+=1


def suite():
    suite = unittest.TestSuite()
    suite.addTest([simple_test('test_one')])
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
