#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import runner,utils
from lib.launcher import *

result = True
caseid = '33849'
casename = "all-521:鼠标右键卸载"

class LauncherUninstall(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.startTime = time.time()
        cls.menuObj = root.application(appName='deepin-menu', description='/usr/lib/deepin-menu')
        apps = launcher.getLauncherAllApps()
        cls.launchername = '深度音乐'
        cls.appName = 'deepin-music'


    @classmethod
    def tearDownClass(cls):
        seconds = "%.3f" % (time.time() - cls.startTime)
        minutes = utils.convertToMinutes(float(seconds))
        global result
        utils.commitresult(caseid, result, minutes)
        if cls.launchername not in launcher.getLauncherAllApps():
            subprocess.check_call('sudo apt-get install -y deepin-music', shell=True)
        launcher.exitLauncher()

    def testNotUninstall(self):
        launcher.searchApp(self.launchername)
        sleep(2)
        launcher.launcherObj.child(self.launchername).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('取消').click()
        apps = launcher.getLauncherAllApps()
        self.assertIn(self.launchername, apps)


    def testUninstall(self):
        launcher.launcherObj.child(self.launchername).click(3)
        if self.menuObj.children[0].name == 'DesktopMenu':
            for i in range(5):
                pyautogui.press('down')
                sleep(0.1)
            pyautogui.press('enter')
        else:
            raise Exception("Menu did not opened!")
        launcher.launcherObj.child('确定').click()
        sleep(2)
        apps = launcher.getLauncherAllApps()
        self.assertNotIn(self.launchername, apps)
        print ('Uninstall %s successeful' % self.launchername)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(LauncherUninstall('testNotUninstall'))
        suite.addTest(LauncherUninstall('testUninstall'))
        return suite

    class MyTestResult(runner.MyTextTestResult):
        def addError(self, test, err):
            super(LauncherUninstall.MyTestResult, self).addError(test, err)
            global result
            result = result and False

        def addFailure(self, test, err):
            super(LauncherUninstall.MyTestResult, self).addFailure(test, err)
            global result
            result = result and False

if __name__ == "__main__":
    unittest.TextTestRunner(resultclass=LauncherUninstall.MyTestResult).run(LauncherUninstall.suite())
