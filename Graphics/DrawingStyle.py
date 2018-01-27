#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Base import Base


class DrawingStyle(Base):
    def __init__(self,
                 styleName,
                 backgroundColor=None,
                 penColor=None,
                 brushColor=None):
        Base.__init__(self)
        self.__setProperties = dict()
        self.updateProperty('className', 'DrawingStyle')
        if styleName is None:
            print('ERROR, DrawingStyle.__init__():',
                  'styleName is None')
            return
        else:
            self.updateProperty('styleName', styleName)
        if styleName == 'custom':
            return

    def addLocation(self):
        if len(self.__textLocations) == 0:
            y = 10
        else:
            y = self.__textLocations[-1].y() + 10
        self.__textLocations.append(QPointF(0, y))

    def removeLocation(self):
        if len(self.__textLocations) == 0:
            return
        elif len(self.__textLocations) == 1:
            self.__textLocations = []
        else:
            self.__textLocations = self.__textLocations[0:-1]
