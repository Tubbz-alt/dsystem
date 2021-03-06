#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from lib import executeTestCase
from lib import runner,utils
from lib.launcher import *
from lib.dde_dock import *
from fnmatch import fnmatch
from glob import glob

result = True
casename = 'all-3353:启动与截图保存'
homePath = os.path.expanduser('~')

class DeepinScreenShot(unittest.TestCase):
    caseid = '83352'
    @classmethod
    def setUpClass(cls):
        cls.appName = 'deepin-screenshot'
        cls.cmd = "ps aux |grep /usr/bin/deepin-screenshot |grep -v grep |awk '{print $12}'"

    @classmethod
    def tearDownClass(cls):
        for pngfile in pngfiles:
            os.remove(pngfile)


    def testDeepinScreenShot1(self):
        subprocess.check_call(self.appName + ' &', shell=True)
        sleep(2)
        pyautogui.press('esc')

    def testDeepinScreenShot2(self):
        launcher.searchApp(self.appName)
        sleep(1)
        pyautogui.press('enter')

    def testSaveScreenShot(self):
        size = pyautogui.size()
        s = size[0]/2, size[1]/2
        d = size[0]/2+300, size[1]/2+200
        sleep(2)
        mouseDrag(s, d)
        pyautogui.press('enter')
        pngfiles = [name for name in os.listdir(homePath + '/Desktop') if fnmatch(name, '深度截图*.png')]
        self.assertGreater(len(pngfiles),0)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DeepinScreenShot('testDeepinScreenShot1'))
        suite.addTest(DeepinScreenShot('testDeepinScreenShot2'))
        suite.addTest(DeepinScreenShot('testSaveScreenShot'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DeepinScreenShot)
