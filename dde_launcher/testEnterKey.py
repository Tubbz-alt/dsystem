#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from lib import executeTestCase
import time
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33906'
casename = "all-533:launcher打开时对enter键的响应"

class LauncherEnterKey(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.appName = 'Google Chrome'
        cls.googleTitleName = '新标签页 - Google Chrome'
        cls.oldWindows = getAllWindows()

    @classmethod
    def tearDownClass(cls):
        cls.newWindows = getAllWindows()
        if len(cls.newWindows) > len(cls.oldWindows):
            for win in cls.newWindows[len(cls.oldWindows):]:
                win.close(1)

    def testEnterKey(self):
        launcher.searchApp(self.appName)
        launcher.launcherObj.child(self.appName).point()
        pyautogui.press('enter')
        win = getWindowName()
        self.assertEqual(self.googleTitleName, win)


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherEnterKey('testEnterKey'))
        return suite


if __name__ == "__main__":
    runTest(LauncherEnterKey.suite())
