#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Graphics.DrawingRules.DrawingRule import DrawingRule
from Graphics.DrawingStyles.DrawingStyle import DrawingStyle
from Graphics.Widgets.MainWidget import MainWidget

def main():
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())


main()
