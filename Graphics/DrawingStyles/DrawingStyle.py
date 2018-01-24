#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DrawingStyle:
    def __init__(self,
                 styleName=None,
                 backgroundColor=None,
                 penColor=None,
                 brushColor=None):
        if styleName is None:
            self.__styleName = 'none'
            self.__atomPen = QPen()
            self.__atomBrush = QBrush()
            self.__bondPen = QPen()
            self.__bondBrush = QBrush()
            self.__bgColor = Qt.black
            self.__textPen = QPen(Qt.black)
            self.__textBrush = None
            self.__textLocations = [QPointF(0, (i + 1) * 10) for i in range(10)]
            self.__boundariesPen = QPen(Qt.black)
            self.__boundariesBrush = None
        elif styleName == 'simple':
            self.__styleName = 'simple'
            self.__atomPen = QPen(Qt.blue)
            self.__atomBrush = QBrush(Qt.blue)
            self.__bondPen = QPen(Qt.gray)
            self.__bondBrush = QBrush(Qt.gray)
            self.__bgColor = Qt.white
            self.__textPen = QPen(Qt.black)
            self.__textBrush = None
            self.__textLocations = [QPointF(0, (i + 1) * 10) for i in range(10)]
            self.__boundariesPen = QPen(Qt.black)
            self.__boundariesBrush = None

    def atomBrush(self):
        if self.__atomBrush is not None:
            return self.__atomBrush
        else:
            return Qt.NoBrush

    def atomPen(self):
        if self.__atomPen is not None:
            return self.__atomPen
        else:
            return Qt.NoPen

    def bondBrush(self):
        if self.__bondBrush is not None:
            return self.__bondBrush
        else:
            return Qt.NoBrush

    def bondPen(self):
        if self.__bondPen is not None:
            return self.__bondPen
        else:
            return Qt.NoPen

    def textPen(self):
        if self.__textPen is not None:
            return self.__textPen
        else:
            return Qt.NoPen

    def textBrush(self):
        if self.__textBrush is not None:
            return self.__textBrush
        else:
            return Qt.NoBrush

    def textLocations(self):
        return self.__textLocations

    def boundariesPen(self):
        if self.__boundariesPen is not None:
            return self.__boundariesPen
        else:
            return Qt.NoPen

    def boundariesBrush(self):
        if self.__boundariesBrush is not None:
            return self.__boundariesBrush
        else:
            return Qt.NoBrush

    def bgColor(self):
        return self.__bgColor

    def styleName(self):
        return self.__styleName
