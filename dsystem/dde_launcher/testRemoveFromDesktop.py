#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib.launcher import *
from lib.dde_dock import *

result = True
casename = 'all-519:从桌面上移除'

class LauncherRemoveFromDesktop(unittest.TestCase):
    caseid = '33843'
    @classmethod
    def setUpClass(cls):
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        cls.QQName = 'QQ'

    @classmethod
    def tearDownClass(cls):
        launcher.exitLauncher()

    def testMenuRemoveFromDesktop(self):
        launcher.menuDesktop(self.QQName)
        desktopFiles = getDesktopFiles()
        QQdesktopFile = 'apps.com.qq.im.desktop'
        self.assertNotIn(QQdesktopFile,desktopFiles)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherRemoveFromDesktop('testMenuRemoveFromDesktop'))
        return suite


if __name__ == "__main__":
    executeTestCase.runTest(LauncherRemoveFromDesktop)
