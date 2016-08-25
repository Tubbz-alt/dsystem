#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '33803'
casename = "all-510:英文字符串搜索"

class MyTestResult(runner.MyTextTestResult):
    def addError(self, test, err):
        super(MyTestResult, self).addError(test, err)
        global result
        result = result and False

    def addFailure(self, test, err):
        super(MyTestResult, self).addFailure(test, err)
        global result
        result = result and False

class LauncherEnglishSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.appName = '图像查看器'
        cls.text1 = 'image viewer'
        cls.text2 = 'iv'
        cls.text3 = 'image'


    @classmethod
    def tearDownClass(cls):
        global result
        utils.commitresult(caseid, result)
        
        
    
    def testEnglishSearch1(self):
        launcher.searchApp(self.text1)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)


    def testEnglishSearch2(self):
        launcher.searchApp(self.text2)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        sleep(2)
        launcher.exitLauncher()
        self.assertIn(self.appName, apps)


    def testEnglishSearch3(self):
        launcher.searchApp(self.text3)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)



def suite():
    suite = unittest.TestSuite()
    suite.addTest(LauncherEnglishSearch('testEnglishSearch1'))
    suite.addTest(LauncherEnglishSearch('testEnglishSearch2'))
    suite.addTest(LauncherEnglishSearch('testEnglishSearch3'))
    return suite

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=MyTestResult).run(suite())