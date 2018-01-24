#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Graphics.DisplayStyles.DisplayStyle import DisplayStyle


class MyPainter(QPainter):
    def __init__(self, displayStyle):
        super().__init__()
        self.__displayStyle = displayStyle

    def begin(self, widget):
        super().begin(widget)
        self.setPen(self.__displayStyle.pen())
        self.setBrush(self.__displayStyle.brush())
