#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *
from time import sleep

result = True
caseid = '45676'
casename = "all-2136:中文和英文搜索"

class LauncherMutiSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = 'wps表格'
        cls.appName = 'WPS 表格'

    @classmethod
    def tearDownClass(cls):
        pass

    def testMutiSearch(self):
        launcher.searchApp(self.text)
        sleep(2)
        apps = launcher.getLauncherAllApps()
        apps = ''.join(apps)
        sleep(2)
        launcher.exitLauncher()
        self.assertEqual(self.appName, apps)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherMutiSearch('testMutiSearch'))
        return suite


if __name__ == "__main__":
    runTest(LauncherMutiSearch.suite())
