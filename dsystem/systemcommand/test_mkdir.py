#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import utils
from lib import runner

result = True
casename = 'all-1441:文件/文件夹操作命令--验证对mkdir命令的支持'

class Mkdir(unittest.TestCase):
    caseid = '38951'
    @classmethod
    def setUpClass(cls):
        cls.loginuser = getoutput("whoami")
        cls.homedir = "/home/%s" % cls.loginuser
        cls.curdir = getoutput("pwd")
        cls.testdir = "testdir"
        cls.deepdir = "testdir1/testsubdir"
        cls.testdir2 = "testdir2"
        cls.testdir3 = "testdir3"

    @classmethod
    def tearDownClass(cls):
        os.system("rm -rf %s*" % cls.testdir)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1CreateDir(self):
        fullpath = "%s/%s" % (self.curdir, self.testdir)
        self.assertFalse(os.path.exists(fullpath))
        os.system("mkdir %s" % self.testdir)
        self.assertTrue(os.path.exists(fullpath))
        self.assertTrue(os.path.isdir(fullpath))

    def test2CreateDir(self):
        (status, output) = rt("mkdir testdir")
        self.assertTrue(0 != status)

    def test3DeepDir(self):
        fullpath = "%s/%s" %(self.curdir, self.deepdir)
        os.system("mkdir -p %s" % self.deepdir)
        self.assertTrue(os.path.exists(fullpath))
        self.assertTrue(os.path.isdir(fullpath))

    def test4MutiCreateDir(self):
        os.system("mkdir %s %s" % (self.testdir2, self.testdir3))
        testdir2path = "%s/%s" % (self.curdir, self.testdir2)
        testdir3path = "%s/%s" % (self.curdir, self.testdir3)
        self.assertTrue(os.path.exists(testdir2path))
        self.assertTrue(os.path.exists(testdir3path))
        self.assertTrue(os.path.isdir(testdir2path))
        self.assertTrue(os.path.isdir(testdir3path))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Mkdir('test1CreateDir'))
        suite.addTest(Mkdir('test2CreateDir'))
        suite.addTest(Mkdir('test3DeepDir'))
        suite.addTest(Mkdir('test4MutiCreateDir'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Mkdir)
