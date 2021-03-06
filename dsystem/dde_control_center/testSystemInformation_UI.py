#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-4222:默认程序首页"

class SystemInformation_UI(unittest.TestCase):
    caseid ='999999'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_display = dde_control_center.Display()

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testSystemInformation_UI(self):
        ret = self.dcc.showModule("systeminfo")
        self.assertTrue(ret)
        self.dcc.page_deep += 1

        systeminfo_label = self.dcc.dccObj.child(self.dcc.string_System_Information)
        self.assertTrue(systeminfo_label)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(SystemInformation_UI('testSystemInformation_UI'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(SystemInformation_UI)
