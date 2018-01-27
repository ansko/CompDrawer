#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Base import Base
from Graphics.DrawingStyle import DrawingStyle
from Graphics.MyPainter import MyPainter
from Structure.LAMMPSFullSystem import LAMMPSFullSystem
from Structure.DrawnSystem import DrawnSystem


# constants, I should avoid them
SIZEX = 500
SIZEY = 500
SIZEZ = 500


class AtomicWidget(QLabel, Base):
    def __init__(self):
        QLabel.__init__(self)
        Base.__init__(self)
        self.__setProperties = dict()
        self.updateProperty('className', 'AtomicWidget')
        self.updateProperty('paintingOffsetX', 0)
        self.updateProperty('paintingOffsetY', 0)
        self.updateProperty('paintingOffsetX', 0)
        self.updateProperty('scale', 1)
        self.updateProperty('projection', 'XY')
        self.updateProperty('stringsDrawn', 0)
    def updateProperty(self, propertyName, propertyValue):
        if propertyValue is None:
            print('WARNING, Base.updatePRoperty():',
                  'propertyValue is None')
            return
        Base.updateProperty(self, propertyName, propertyValue)
        if propertyName == 'LAMMPSFullSystem':
            drawnSystem = DrawnSystem(LAMMPSFullSystem = propertyValue)
            Base.updateProperty(self, 'drawnSystem', drawnSystem)

    def paintEvent(self, event):
        p = MyPainter()
        p.begin(self)
        p.translate(self.width() / 2, self.height() / 2)
        drawnSystem = self.getProperty('drawnSystem')
        p.drawDrawnSystem(drawnSystem)
        p.end()
