#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import os
import gettext
from lib.executeTestCase import runTest

# import ddedock.testFashionDefaultIcons
# import ddedock.testEfficientDefaultIcons
# import ddedock.testFashionIconsPopup
# import ddedock.testEfficientIconsPopup
from ddedock.testFashionFunction import FashionFunction
from ddedock.testEfficientFunction import EfficientFunction
from ddedock.testOtherDirectionDockSize import OtherDirectionDockSize
from ddedock.testDockKeepShown import DockKeepShown
from ddedock.testDockKeepHidden import DockKeepHidden
from ddedock.testDockSmartHide import DockSmartHide
from ddedock.testDockKeepShownOtherDirection import DockKeepShownOtherDirection
from ddedock.testDockKeepHiddenOtherDirection import DockKeepHiddenOtherDirection
from ddedock.testDockSmartHideOtherDirection import DockSmartHideOtherDirection
from ddedock.testDockMenu import DockMenu
from ddedock.testDockFashionMode import DockFashionModeTop
from ddedock.testDockEfficientMode import DockEfficientModeTop

from ddedock.testFashionDockSize import FashionDockSize
from ddedock.testEfficientDockSize import EfficientDockSize
from ddedock.testFashionDockSizeLarge import FashionDockSizeLarge
from ddedock.testFashionDockSizeMedium import FashionDockSizeMedium
from ddedock.testFashionDockSizeSmall import FashionDockSizeSmall
from ddedock.testEfficientDockSizeLarge import EfficientDockSizeLarge
from ddedock.testEfficientDockSizeMedium import EfficientDockSizeMedium
from ddedock.testEfficientDockSizeSmall import EfficientDockSizeSmall
from ddedock.testDockSizeLargeOtherDirection import DockSizeLargeOtherDirection
from ddedock.testDockSizeMediumOtherDirection import DockSizeMediumOtherDirection
from ddedock.testDockSizeSmallOtherDirection import DockSizeSmallOtherDirection

from ddedock.testGedit import Gedit
from ddedock.testDeepinScreenshot import DeepinScreenshot
from ddedock.testGoogleChrome import GoogleChrome

from ddedock.testDockIconMenuName import DockIconMenuName
from ddedock.testDockIconMenuMultiClose import DockIconMenuMultiClose
from ddedock.testDockIconMenu import DockIconMenu
from ddedock.testDockIconMenuRemove import DockIconMenuRemove

from ddedock.testHideDisplayApp import HideDisplayApp
from ddedock.testDockMenuRU import DockMenuRU

from ddedock.testDockMenuRun import DockMenuRun
from ddedock.testDockMenuUnDock import DockMenuUnDock

from ddedock.testFashionIconsPopup import FashionIconsPopup
from ddedock.testEfficientIconsPopup import EfficientIconsPopup

from ddedock.testDockSoundPluginClick import DockSoundPluginClick

def main():
    # suite00 = ddedock.testFashionDefaultIcons.suite()
    # suite01 = ddedock.testEfficientDefaultIcons.suite()
    # suite02 = ddedock.testFashionIconsPopup.suite()
    # suite03 = ddedock.testEfficientIconsPopup.suite()

    classes = []

    # dde-dock
    classes.append(FashionFunction)
    classes.append(EfficientFunction)
    classes.append(OtherDirectionDockSize)
    classes.append(DockKeepShown)
    classes.append(DockKeepHidden)
    classes.append(DockSmartHide)
    classes.append(DockKeepShownOtherDirection)
    classes.append(DockKeepHiddenOtherDirection)
    classes.append(DockSmartHideOtherDirection)
    classes.append(DockMenu)
    classes.append(DockFashionModeTop)
    classes.append(DockEfficientModeTop)

    classes.append(FashionDockSize)
    classes.append(EfficientDockSize)
    classes.append(FashionDockSizeLarge)
    classes.append(FashionDockSizeMedium)
    classes.append(FashionDockSizeSmall)
    classes.append(EfficientDockSizeLarge)
    classes.append(EfficientDockSizeMedium)
    classes.append(EfficientDockSizeSmall)
    classes.append(DockSizeLargeOtherDirection)
    classes.append(DockSizeMediumOtherDirection)
    classes.append(DockSizeSmallOtherDirection)

    classes.append(Gedit)
    classes.append(DeepinScreenshot)
    classes.append(GoogleChrome)

    classes.append(DockIconMenuName)
    classes.append(DockIconMenuMultiClose)
    classes.append(DockIconMenu)
    classes.append(DockIconMenuRemove)

    classes.append(HideDisplayApp)
    classes.append(DockMenuRU)

    classes.append(DockMenuRun)
    classes.append(DockMenuUnDock)

    classes.append(FashionIconsPopup)
    classes.append(EfficientIconsPopup)

    # 插件 -> 声音
    classes.append(DockSoundPluginClick)

    for c in classes:
        runTest(c)

if __name__ == "__main__":
    unittest.installHandler()
    LOCALE_DIR = os.path.abspath("./lib/locale")
    gettext.install('dsystem', LOCALE_DIR)
    main()
