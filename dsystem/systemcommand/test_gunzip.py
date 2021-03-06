#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from lib import executeTestCase
from subprocess import getstatusoutput as rt
from subprocess import getoutput
from lib import runner
from lib import utils

result = True
casename = 'all-1456:备份、压缩和解压缩操作命令--验证对gunzip命令的支持'

class Gunzip(unittest.TestCase):
    caseid = '39052'
    @classmethod
    def setUpClass(cls):
        cls.testfile    = "testfile"
        cls.gzipfile    = "testfile.gz"

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.testfile):
            os.remove(cls.testfile)

        if os.path.exists(cls.gzipfile):
            os.remove(cls.gzipfile)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGunzipOne(self):
        os.system("touch %s" % self.testfile)
        self.assertTrue(os.path.exists(self.testfile))

        os.system("gzip %s" % self.testfile)
        self.assertFalse(os.path.exists(self.testfile))
        self.assertTrue(os.path.exists(self.gzipfile))

    def testGunzipTwo(self):
        os.system("gzip -d %s" % self.gzipfile)
        self.assertTrue(os.path.exists(self.testfile))
        self.assertFalse(os.path.exists(self.gzipfile))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Gunzip('testGunzipOne'))
        suite.addTest(Gunzip('testGunzipTwo'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(Gunzip)
