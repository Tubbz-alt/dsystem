#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import time
from lib import executeTestCase
from lib import utils
from lib import runner

casename = "all-436:一直显示"

class DockKeepShown(unittest.TestCase):
    caseid = '33410'
    @classmethod
    def setUpClass(cls):
        cls.ddedockobject = utils.getDdeDockObject()
        cls.defaultdisplaymode = utils.getDdeDockDisplayMode()
        cls.defaultposition = utils.getDdeDockPosition()
        cls.defaulthidemode = utils.getDdeDockHideMode()
        cls.dock_mainwindow = "dock-mainwindow"
        cls.filemanager = "深度文件管理器"
        cls.filemanager_windowname = "深度文件管理器"

        if utils.dock.displaymode_fashion != cls.defaultdisplaymode:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.dock.position_bottom != cls.defaultposition:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.dock.hidemode_keepshowing != cls.defaulthidemode:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

    @classmethod
    def tearDownClass(cls):
        if utils.getDdeDockDisplayMode() != utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

        if utils.getDdeDockPosition() != utils.dock.position_bottom:
            utils.setDdeDockPosition(utils.dock.position_bottom)

        if utils.getDdeDockHideMode() != utils.dock.hidemode_keepshowing:
            utils.setDdeDockHideMode(utils.dock.hidemode_keepshowing)

        filemanager = cls.ddedockobject.child(cls.filemanager)
        win = utils.findWindow(cls.filemanager_windowname)
        if win != None:
            win.unmaximize()
            win.close(time.time())

    def testOpenFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        filemanager.click()
        win = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win != None)

    def testMaximizeFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.maximize()
        self.assertTrue(win != None)

    def testMinimizeFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.minimize()
        time.sleep(1)
        self.assertTrue(win != None)
        win_test = utils.findWindow(self.filemanager_windowname)
        self.assertTrue(win_test.is_minimized())

    def testActivateFileManager(self):
        filemanager = self.ddedockobject.child(self.filemanager)
        win = utils.findWindow(self.filemanager_windowname)
        win.activate(time.time())
        self.assertTrue(win != None)
        self.assertTrue(win.is_maximized())

    def testCheckDockSize(self):
        main_window = self.ddedockobject.child(self.dock_mainwindow)
        (width, height) = main_window.size
        self.assertTrue(height > 1)

    def testExChangeDisplayMode(self):
        if utils.getDdeDockDisplayMode() == utils.dock.displaymode_fashion:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_efficient)
        elif utils.getDdeDockDisplayMode() == utils.dock.displaymode_efficient:
            utils.setDdeDockDisplayMode(utils.dock.displaymode_fashion)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DockKeepShown('testOpenFileManager'))
        suite.addTest(DockKeepShown('testMaximizeFileManager'))
        suite.addTest(DockKeepShown('testCheckDockSize'))
        suite.addTest(DockKeepShown('testMinimizeFileManager'))
        suite.addTest(DockKeepShown('testCheckDockSize'))
        suite.addTest(DockKeepShown('testExChangeDisplayMode'))
        suite.addTest(DockKeepShown('testActivateFileManager'))
        suite.addTest(DockKeepShown('testCheckDockSize'))
        suite.addTest(DockKeepShown('testMinimizeFileManager'))
        suite.addTest(DockKeepShown('testCheckDockSize'))
        return suite

if __name__ == "__main__":
    executeTestCase.runTest(DockKeepShown)
