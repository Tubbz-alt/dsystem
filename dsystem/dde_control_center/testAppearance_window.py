#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
from time import sleep
from lib import executeTestCase
from lib import dde_control_center

casename = 'all-3847:主题-窗口-默认'

class AppearanceWindowTheme(unittest.TestCase):
    caseid = '103580'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.defaultWindowTheme = dde_control_center.getAppearanceWindowTheme()

    @classmethod
    def tearDownClass(cls):
        if dde_control_center.getAppearanceWindowTheme() != cls.defaultWindowTheme:
            dde_control_center.setAppearanceWindowTheme('deepin')

        dde_control_center.Dde_control_center().hideDcc()

    def testWindowTheme(self):
        ret = self.dcc.showModule('Personalization')
        self.dcc.dccObj.child('Theme').click()
        windowTheme = dde_control_center.getAppearanceWindowTheme()
        self.assertEqual(windowTheme, 'deepin')

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(AppearanceWindowTheme('testWindowTheme'))
        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(AppearanceWindowTheme)
