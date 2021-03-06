#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import getpass
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput

casename = 'all-5410:其他命令--验证对who命令的支持'

class Command_who(unittest.TestCase):
    caseid = '192250'
    @classmethod
    def setUpClass(cls):
        cls.loginuser = getpass.getuser()

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWho(self):
        (status, output) = rt('who')
        self.assertTrue(0 == status)

        for line in output.split('\n'):
            linelist = line.split()
            self.assertTrue(self.loginuser == linelist[0])
            self.assertTrue('tty1' == linelist[1])
            break

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Command_who('testWho'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    executeTestCase.runTest(Command_who)
