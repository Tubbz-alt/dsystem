#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import gettext
import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import runner
from lib.launcher import launcher
from dogtail import rawinput
from lib.dde_dock import Dock

casename = "all-439:gedit"

class Gedit(unittest.TestCase):
    caseid = '33428'
    @classmethod
    def setUpClass(cls):
        cls.dock = Dock()
        cls.gediticonname = cls.dock.string_Text_Editor
        cls.ddedockobject = utils.getDdeDockObject()

        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    @classmethod
    def tearDownClass(cls):
        if utils.dock.displaymode_fashion != utils.getDdeDockDisplayMode():
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != utils.getDdeDockPosition():
            utils.setDdeDockPosition(utils.dock.position_bottom)

    def testDragIconToDock(self):
        utils.keySingle(utils.k.windows_l_key)
        try:
            launcherwin = utils.findWindow("dde-launcher")
        except:
            self.assertTrue(False, "Can't open dde-launcher")

        utils.keyTypeString("gedit")

        try:
            launcher_icon = self.ddedockobject.child(self.dock.string_dock_Launcher)
        except:
            self.assertTrue(False, "Can't find launcher icon")


        apps = launcher.getLauncherAllApps()
        fromXY = launcher.getAppCenterCoor(apps[0])
        toXY = utils.getDockIconCenterPoint(launcher_icon)

        utils.mouseDragIconToDock((int(fromXY[0]), int(fromXY[1])), toXY)
        time.sleep(1)
        self.testGeditExistOnDock()
        time.sleep(1)

    def testDragDockIconToDesktop(self):
        icongedit_icon = self.ddedockobject.child(self.gediticonname)
        self.assertTrue(icongedit_icon != None)
        fromXY = utils.getDockIconCenterPoint(icongedit_icon)
        utils.mouseDrag(fromXY, (fromXY[0], fromXY[1] - 100))

        ddedock = utils.getDdeDockObject()
        icongedit_icon_later = ddedock.child(self.gediticonname)
        self.assertTrue(None == icongedit_icon_later)

    def testOpenGedit(self):
        icongedit = self.ddedockobject.child(self.gediticonname)
        icongedit.click()
        geditwin1 = utils.findWindow(self.dock.string_Text_Editor_Window1,
                comparetype="notequal")
        self.assertTrue(geditwin1 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin2 = utils.findWindow(self.dock.string_Text_Editor_Window2,
                comparetype="notequal")
        self.assertTrue(geditwin2 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin3 = utils.findWindow(self.dock.string_Text_Editor_Window3,
                comparetype="notequal")
        self.assertTrue(geditwin3 != None)

        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin4 = utils.findWindow(self.dock.string_Text_Editor_Window4,
                comparetype="notequal")
        self.assertTrue(geditwin4 != None)

    def testCloseGedit(self):
        icongedit = self.ddedockobject.child(self.gediticonname)
        icongedit.click(3)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.down_key)
        utils.keySingle(utils.k.enter_key)
        geditwin1 = utils.findWindow(self.dock.string_Text_Editor_Window4,
                mode="nowait", comparetype="notequal")
        geditwin2 = utils.findWindow(self.dock.string_Text_Editor_Window4,
                mode="nowait", comparetype="notequal")
        geditwin3 = utils.findWindow(self.dock.string_Text_Editor_Window4,
                mode="nowait", comparetype="notequal")
        geditwin4 = utils.findWindow(self.dock.string_Text_Editor_Window4,
                mode="nowait", comparetype="notequal")
        self.assertTrue(None == geditwin1)
        self.assertTrue(None == geditwin2)
        self.assertTrue(None == geditwin3)
        self.assertTrue(None == geditwin4)

    def testGeditExistOnDock(self):
        try:
            icongedit = self.ddedockobject.child(self.gediticonname)
            self.assertTrue(icongedit.size[0] > 1)
            self.assertTrue(icongedit.size[1] > 1)
            self.assertTrue(icongedit.position[0] > 1)
            self.assertTrue(icongedit.position[1] > 1)
        except:
            self.assertTrue(False, "Icon Gedit doesn't exist on Dock")


    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Gedit('testDragIconToDock'))
        suite.addTest(Gedit('testOpenGedit'))
        suite.addTest(Gedit('testCloseGedit'))
        suite.addTest(Gedit('testDragDockIconToDesktop'))

        return suite

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    executeTestCase.runTest(Gedit)
