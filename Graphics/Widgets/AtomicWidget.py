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
from Graphics.DrawingRules.DrawingRule import DrawingRule
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
        self.__drawingRule = DrawingRule(generalRuleName=drawingRuleName)
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
        #print('aw.setProjection', projection)
        if projection in ['XY', 'XZ', 'YZ']:
            self.__projection = projection
            
            self.update()

    def setDrawingStyle(self, drawingStyle):
        self.__drawingStyle = drawingStyle

    def setDrawingRule(self, drawingRule):
        self.__drawingRule = drawingRule

    def setAtomDrawingRule(self, atomDrawingRule):
        self.__drawingRule.setAtomDrawingRule(atomDrawingRule)

    def setBondDrawingRule(self, bondDrawingRule):
        self.__drawingRule.setBondDrawingRule(bondDrawingRule)

    def setTextDrawingRule(self, textDrawingRule):
        self.__drawingRule.setTextDrawingRule(textDrawingRule)

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

    def __initUI(self):
        # at the beginning of the loop
        # values are equal to the first atom coordinates
        xmin = self.__drawnSystem.atoms()[0].atomX()
        xmax = self.__drawnSystem.atoms()[0].atomX()
        ymin = self.__drawnSystem.atoms()[0].atomY()
        ymax = self.__drawnSystem.atoms()[0].atomY()
        zmin = self.__drawnSystem.atoms()[0].atomZ()
        zmax = self.__drawnSystem.atoms()[0].atomZ()
        # after that we update them
        for atom in self.__drawnSystem.atoms():
            x = atom.atomX()
            y = atom.atomY()
            z = atom.atomZ()
            if x < xmin:
                xmin = x
            elif x > xmax:
                xmax = x
            if y < ymin:
                ymin = y
            elif y > ymax:
                ymax = y
            if z < zmin:
                zmin = z
            elif z > zmax:
                zmax = z
        lx = xmax - xmin
        ly = ymax - ymin
        lz = zmax - zmin
        multiplierX = SIZEX / (lx + 2 * R)
        multiplierY = SIZEY / (ly + 2 * R)
        multiplierZ = SIZEZ / (lz + 2 * R)
        self.__scale = min(multiplierX, multiplierY, multiplierZ)
        centerX = (xmax + xmin) / 2
        centerY = (ymax + ymin) / 2
        centerZ = (zmax + zmin) / 2
        self.__paintingOffsetX = -centerX
        self.__paintingOffsetY = -centerY
        self.__paintingOffsetZ = -centerZ

    def paintEvent(self, event):
        sysProp = self.__drawnSystem.getPropertyValue
        self.__drawnSystem.calculateScale()

        p = MyPainter()
        p.setDrawnSystem(self.__drawnSystem)
        p.setProjection(self.__projection)

        p.begin(self)
        p.translate(self.width() / 2, self.height() / 2)

        p.drawAxes()
        for drawnAtom in self.__drawnSystem.drawnAtoms():
            p.drawDrawnAtom(drawnAtom)
        for drawnBond in self.__drawnSystem.drawnBonds():
            pass

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
