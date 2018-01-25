#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Structure.PhysicalAtomicSystem import PhysicalAtomicSystem
from Graphics.DrawingRules.DrawingRule import DrawingRule
from Graphics.DrawingStyles.DrawingStyle import DrawingStyle

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
        self.__physicalAtomicSystem = None
        self.__projection = 'XY'
        self.__stringsDrawn = 0

    def setPhysicalAtomicSystem(self, physicalAtomicSystem):
        self.__physicalAtomicSystem = physicalAtomicSystem
        self.__initUI()

    def setProjection(self, projection):
        if projection in ['XY', 'XZ', 'YZ']:
            self.__projection = projection
            self.update()

    def setDrawingStyle(self, drawingStyle):
        #print('aw,', drawingStyle.styleName())
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
        xmin = self.__physicalAtomicSystem.atoms()[0].atomX()
        xmax = self.__physicalAtomicSystem.atoms()[0].atomX()
        ymin = self.__physicalAtomicSystem.atoms()[0].atomY()
        ymax = self.__physicalAtomicSystem.atoms()[0].atomY()
        zmin = self.__physicalAtomicSystem.atoms()[0].atomZ()
        zmax = self.__physicalAtomicSystem.atoms()[0].atomZ()
        # after that we update them
        for atom in self.__physicalAtomicSystem.atoms():
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
        p = QPainter()
        self.__drawnSystem.calculateScale()
        scale = self.__drawnSystem.scale()
        scalePolicy = self.__drawnSystem.getPropertyValue('scalePolicy')
        if scalePolicy == 'united':
            scalex = scale
            scaley = scale
            scalez = scale
        axes = self.__drawnSystem.getPropertyValue('axes')
       # Draw axes (or not):
        if sysProp('drawAxesFlag') is not None:
            p.begin(self)
            p.translate(self.width() / 2, self.height() / 2)
            axesPenColorPolicy = sysProp('axesPenColorPolicy')
            if axesPenColorPolicy == 'united':
                axesPenColorUnited = sysProp('axesPenColorUnited')
                pen = QPen(axesPenColorUnited)
                p.setPen(pen)
            xlabel = axes[0] # x label means that the label is near the widget's
                             # x axe, not the system's x axe!
            ylabel = axes[1] # same for y
            p.drawLine(0, 0, 100, 0)
            p.drawLine(0, 0, 0, -100)
            p.drawText(95, 15, 'X')
            p.drawText(-10, -95, 'Y')
            p.end()
       # Draw atoms (or not):
        if sysProp('drawAtomsFlag') is not None:
            p.begin(self)
            p.translate(self.width() / 2, self.height() / 2)
            p.scale(1, -1)
            if 'X' in axes:
                dx = sysProp('offsetX')
            if 'Y' in axes:
                dy = sysProp('offsetY')
            if 'Z' in axes:
                dz = sysProp('offsetZ')
            atomBrushColorPolicy = sysProp('atomBrushColorPolicy')
            if atomBrushColorPolicy == 'united':
                atomBrushColorUnited = sysProp('atomBrushColorUnited')
                brush = QBrush(QColor(atomBrushColorUnited))
                p.setBrush(brush)
            elif atomBrushColorPolicy == 'atomType':
                atomBrushes = sysProp('atomBrushes')
            for drawnAtom in self.__drawnSystem.drawnAtoms():
                atProp = drawnAtom.getPropertyValue
                if atomBrushColorPolicy == 'united':
                    pass
                elif atomBrushColorPolicy == 'atomType':
                    atomType = atProp('atomType')
                    brush = atomBrushesByType[atomType + 1]
                    p.setBrush(brush)
                r = atProp('drawnRadius')
                if r is None:
                    r = 50
                if axes == 'XY':
                    x = atProp('atomX') + dx
                    y = atProp('atomY') + dy
                    p.drawEllipse(x * scalex - r, y * scaley - r, 2 * r, 2 * r)
                elif axes == 'XZ':
                    x = atProp('atomX') + dx
                    z = atProp('atomY') + dz
                    p.drawEllipse(x * scalex - r, z * scalez - r, 2 * r, 2 * r)
                elif axes == 'YZ':
                    y = atProp('atomX') + dy
                    z = atProp('atomY') + dz
                    p.drawEllipse(y * scaley - r, z * scalez - r, 2 * r, 2 * r)
            p.end()
       # Draw bonds (or not):
        if sysProp('drawBondsFlag') is not None:
            p.begin(self)
            p.translate(self.width() / 2, self.height() / 2)
            p.scale(1, -1)
            if 'X' in axes:
                dx = sysProp('offsetX')
            if 'Y' in axes:
                dy = sysProp('offsetY')
            if 'Z' in axes:
                dz = sysProp('offsetZ')
            bondPenColorPolicy = sysProp('bondPenColorPolicy')
            if bondPenColorPolicy == 'united':
                bondPenColorUnited = sysProp('bondPenColorUnited')
                pen = QPen(QColor(bondPenColorUnited))
                p.setPen(pen)
            elif bondPenColorPolicy == 'bondType':
                bondPens = sysProp('bondPens')
            for i in range(len(self.__drawnSystem.drawnBonds()) - 1):
                bond = self.__drawnSystem.drawnBonds()[i]
                boProp = bond.getPropertyValue
                x1 = boProp('physicalAtomOne').atomX()
                x2 = boProp('physicalAtomTwo').atomX()
                y1 = boProp('physicalAtomOne').atomY()
                y2 = boProp('physicalAtomTwo').atomY()
                z1 = boProp('physicalAtomOne').atomZ()
                z2 = boProp('physicalAtomTwo').atomZ()
                if axes == 'XY':
                    x1 += dx
                    x2 += dx
                    y1 += dy
                    y2 += dy
                    p.drawLine(x1 * scalex,
                               y1 * scaley,
                               x2 * scalex,
                               y2 * scaley)
            p.end()

    def setDrawnSystem(self, drawnSystem):
        self.__drawnSystem = drawnSystem

    def drawnSystem(self):
        return self.__drawnSystem

    def scale(self):
        return self.__scale

    def setScale(self, scale):
        if scale != 0:
            self.__scale = scale

    def physicalAtomicSystem(self):
        return self.__physicalAtomicSystem

    def drawingStyle(self):
        return self.__drawingStyle
