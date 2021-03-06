#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import gettext
from lib import executeTestCase
from lib import dde_control_center

casename = "all-3767:添加账户-取消"

class Accounts_AddUserCancel(unittest.TestCase):
    caseid ='103183'
    @classmethod
    def setUpClass(cls):
        cls.dcc = dde_control_center.Dde_control_center()
        cls.dbus_account = dde_control_center.Accounts()
        cls.newusername = 'test1234'
        cls.newuserpw = 'test1234'

    @classmethod
    def tearDownClass(cls):
        cls.dcc.backToIndex()
        cls.dcc.exit()

    def testAccountsAddUserCancel(self):
        ret = self.dcc.showModule("accounts")
        self.assertTrue(ret)
        self.dcc.page_deep += 1
        deepinAllUserName = self.dbus_account.getDeepinAllUserName()

        for username in deepinAllUserName:
            username_widget = self.dcc.dccObj.child(username)
            self.assertTrue(username_widget)

        createaccount = self.dcc.dccObj.child(self.dcc.string_Create_Account)
        self.assertTrue(createaccount)
        createaccount.click()
        self.dcc.page_deep += 1
        self.dcc.addUser(self.newusername, self.newuserpw,
                         self.dcc.string_NewAccount_Cancel)

        newAllUserName = self.dbus_account.getDeepinAllUserName()
        self.assertFalse(self.newusername in newAllUserName)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Accounts_AddUserCancel('testAccountsAddUserCancel'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Accounts_AddUserCancel)
