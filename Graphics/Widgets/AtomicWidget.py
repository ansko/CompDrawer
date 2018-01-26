#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Structure.PhysicalSystem import PhysicalSystem
from Graphics.DrawingStyles.DrawingStyle import DrawingStyle
from Graphics.DrawnSystem import DrawnSystem
from Graphics.MyPainter import MyPainter


# constants, I should avoid them
R = 2
SIZEX = 500
SIZEY = 500
SIZEZ = 500


class AtomicWidget(QLabel):
    """
        This widget is done to draw all atoms in the system.
        By default it draws lonesome hydrogen atom, because that is what default
    system contains.
    """
    def __init__(self,
                 drawingStyleName=None,
                 drawingRuleName=None):
        super().__init__()
        if drawingStyleName is not None:
            self.__drawingStyle = DrawingStyle(styleName=None)
        else:
            self.__drawingStyle = DrawingStyle(styleName='default')
        self.__paintingOffsetX = 0
        self.__paintingOffsetY = 0
        self.__paintingOffsetZ = 0
        self.__scale = 1
        self.__physicalSystem = None
        self.__drawnSystem = None
        self.__projection = 'XY'
        self.__stringsDrawn = 0

    def setPhysicalSystem(self, physicalSystem):
        self.__physicalSystem = physicalSystem
        drawnSystem = DrawnSystem(physicalSystem=physicalSystem)
        self.__drawnSystem = drawnSystem

    def setDrawnSystem(self, drawnSystem):
        self.__drawnSystem = drawnSystem
        self.__initUI()

    def setProjection(self, projection):
        if projection in ['XY', 'XZ', 'YZ']:
            self.__projection = projection

    def setDrawingStyle(self, drawingStyle):
        self.__drawingStyle = drawingStyle

    def addAtomStringName(self, stringName):
        self.__drawingRule.addAtomStringName(stringName)

    def addTextStringName(self, stringName):
        self.__drawingStyle.addLocation()
        self.__drawingRule.addStringName(stringName)

    def removeTextStringName(self, stringName):
        self.__drawingStyle.removeLocation()
        self.__drawingRule.removeStringName(stringName)

    def physicalAtomicSystem(self):
        return self.__physicalAtomicSystem

    def drawingStyle(self):
        return self.__drawingStyle

    def paintEvent(self, event):
        self.__drawnSystem.calculateScale()

        p = MyPainter()
        p.setDrawnSystem(self.__drawnSystem)
        p.setProjection(self.__projection)
        p.setScale(self.__drawnSystem.scale())

        p.begin(self)
        p.translate(self.width() / 2, self.height() / 2)

        p.drawLegend()
        p.drawAxes()
        for drawnAtom in self.__drawnSystem.drawnAtoms():
            p.drawDrawnAtom(drawnAtom)
        for drawnBond in self.__drawnSystem.drawnBonds():
            p.drawDrawnBond(drawnBond)

        p.end()

    def drawnSystem(self):
        return self.__drawnSystem

    def scale(self):
        return self.__scale

    def setScale(self, scale):
        if scale != 0:
            self.__scale = scale

    def physicalSystem(self):
        return self.__physicalSystem

    def drawingStyle(self):
        return self.__drawingStyle
