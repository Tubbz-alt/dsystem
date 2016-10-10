#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True

class Apt_cache(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.caseid = '69087'
        cls.casename = 'all-2614:apt-cache命令'

    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(cls.caseid, result)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApt_cache(self):
        (status, output) = rt('apt-cache policy dde')
        self.assertTrue(0 == status, "Error: %s" % output)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Apt_cache('testApt_cache'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(Apt_cache.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(Apt_cache.MyTestResult, self).addError(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=Apt_cache.MyTestResult).run(Apt_cache.suite())
