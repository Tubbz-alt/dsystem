#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner
import pexpect

result = True
casename = 'all-1438:用户管理命令--验证对passwd命令的支持'

class Passwd(unittest.TestCase):
    caseid = '38933'
    @classmethod
    def setUpClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

    @classmethod
    def tearDownClass(cls):
        if os.path.exists('/home/test'):
            (status, output) = rt('sudo deluser --remove-home test')

        if os.path.exists('/home/test'):
            os.system('sudo rm -rf /home/test')

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def addUser(self):
        self.assertFalse(os.path.exists('/home/test'))
        (status, output) = rt('sudo useradd -m test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def passwd(self):
        childerr = pexpect.spawn('su - test')
        childerr.expect("密码：")
        childerr.sendline("deepin")
        outputerr = getoutput('echo $?')
        self.assertFalse(int(outputerr) == 1)

        child = pexpect.spawn('sudo passwd test')
        child.expect("UNIX 密码：")
        child.sendline("deepin")
        child.expect("UNIX 密码：")
        child.sendline("deepin")

        childok = pexpect.spawn('su - test')
        childok.expect("密码：")
        childok.sendline("deepin")
        outputok = getoutput('echo $?')
        self.assertTrue(int(outputok) == 0)

    def delUser(self):
        (status, output) = rt('sudo userdel test')
        self.assertTrue(0 == status)
        self.assertTrue(os.path.exists('/home/test'))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Passwd('addUser'))
        suite.addTest(Passwd('passwd'))
        suite.addTest(Passwd('delUser'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Passwd)
