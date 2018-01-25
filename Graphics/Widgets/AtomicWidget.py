#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem
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
        if self.__drawingStyle is None:
            print('aw.pE, style is none')
            return
        p = QPainter()
        p.begin(self)
      ### drawing text
        if self.__drawingStyle.textLocations() is not None:
            textPen = self.__drawingStyle.textPen()
            textBrush = self.__drawingStyle.textBrush()
            textLocations = self.__drawingStyle.textLocations()
            p.setPen(textPen)
            p.setBrush(textBrush)
            if self.__drawingRule.ifDrawText('scale'):
                if len(textLocations) < 1 + self.__stringsDrawn:
                    self.__stringsDrawn += 1
                    print('aw.pE, too few textLocations')
                    return
                p.drawText(textLocations[self.__stringsDrawn], 'scale = ' +
                                             str(round(self.__scale, 1)))
                self.__stringsDrawn += 1
            if self.__drawingRule.ifDrawText('drawingStyleName'):
                if len(textLocations) < 1 + self.__stringsDrawn:
                    self.__stringsDrawn += 1
                    print('aw.pE, too few textLocations')
                    return
                p.drawText(textLocations[self.__stringsDrawn], 
                          'drawingStyleName = ' +
                          self.__drawingStyle.styleName())
                self.__stringsDrawn += 1
            if self.__drawingRule.ifDrawText('drawingRuleName'):
                if len(textLocations) < 1 + self.__stringsDrawn:
                    self.__stringsDrawn += 1
                    print('aw.pE, too few textLocations')
                    return
                p.drawText(textLocations[self.__stringsDrawn],
                           'drawingRuleName = ' +
                           self.__drawingRule.generalRuleName())
                self.__stringsDrawn += 1
      ### drawing axis
        p.translate(self.width() / 2, self.height() / 2)
        p.drawLine(0, 0, 0, -250)
        p.drawText(5, -240, self.__projection[1])
        p.drawText(230, -10, self.__projection[0])
        p.drawLine(0, 0, 250, 0)
        p.scale(1, -1)
      ### drawing atomic system:
        if self.__physicalAtomicSystem is None:
            return
        if self.__physicalAtomicSystem.atoms() is None:
            return
       ## drawing atoms
        for atom in self.__physicalAtomicSystem.atoms():
            if not self.__drawingRule.ifDrawAtom(atom):
                continue
            atomPen = self.__drawingStyle.atomPen(atom)
            atomBrush = self.__drawingStyle.atomBrush(atom)
            p.setPen(atomPen)
            p.setBrush(atomBrush)
            x = (atom.atomX() + self.__paintingOffsetX) * self.__scale
            y = (atom.atomY() + self.__paintingOffsetY) * self.__scale
            z = (atom.atomZ() + self.__paintingOffsetZ) * self.__scale
            if self.__projection == 'XY':
                p.drawEllipse(x - R,
                              y - R,
                              2 * R,
                              2 * R)
            elif self.__projection == 'XZ':
                p.drawEllipse(x - R,
                              z - R,
                              2 * R,
                              2 * R)
            elif self.__projection == 'YZ':
                p.drawEllipse(y - R,
                              z - R,
                              2 * R,
                              2 * R)
            else:
                print('ERROR:',
                      'AtomicWidget.paintEvent()',
                      'some error in projection')
       ## drawing bonds
        bondPen = self.__drawingStyle.bondPen()
        bondBrush = self.__drawingStyle.bondBrush()
        p.setPen(bondPen)
        p.setBrush(bondBrush)
        for bond in self.__physicalAtomicSystem.bonds():
            if True in bond.crosses():
                continue
            x = bond.bondAtomOne().atomX()
            otherX = bond.bondAtomTwo().atomX()
            y = bond.bondAtomOne().atomY()
            otherY = bond.bondAtomTwo().atomY()
            z = bond.bondAtomOne().atomZ()
            otherZ = bond.bondAtomTwo().atomZ()
            if self.__projection == 'XY':
                p.drawLine((x + self.__paintingOffsetX) * self.__scale,
                           (y + self.__paintingOffsetY) * self.__scale,
                           (otherX + self.__paintingOffsetX) * self.__scale,
                           (otherY + self.__paintingOffsetY) * self.__scale)
            elif self.__projection == 'XZ':
                p.drawLine((x + self.__paintingOffsetX) * self.__scale,
                           (z + self.__paintingOffsetZ) * self.__scale,
                           (otherX + self.__paintingOffsetX) * self.__scale,
                           (otherZ + self.__paintingOffsetZ) * self.__scale)
            elif self.__projection == 'YZ':
                p.drawLine((y + self.__paintingOffsetY) * self.__scale,
                           (z + self.__paintingOffsetZ) * self.__scale,
                           (otherY + self.__paintingOffsetY) * self.__scale,
                           (otherZ + self.__paintingOffsetZ) * self.__scale)
            else:
                print('ERROR:',
                      'AtomicWidget.paintEvent()',
                      'some error in projection')
       ## drawing boundaries
        ranges = self.__physicalAtomicSystem.ranges()
        if ranges is None:
            p.end()
            return
        boundariesPen = self.__drawingStyle.boundariesPen()
        boundariesBrush = self.__drawingStyle.boundariesBrush()
        p.setPen(boundariesPen)
        p.setBrush(boundariesBrush)
        xlo = (ranges[0] + self.__paintingOffsetX) * self.__scale
        xhi = (ranges[1] + self.__paintingOffsetX) * self.__scale
        ylo = (ranges[2] + self.__paintingOffsetY) * self.__scale
        yhi = (ranges[3] + self.__paintingOffsetY) * self.__scale
        zlo = (ranges[4] + self.__paintingOffsetZ) * self.__scale
        zhi = (ranges[5] + self.__paintingOffsetZ) * self.__scale
        if self.__projection == 'XY':
            p.drawRect(xlo, ylo, xhi - xlo, yhi - ylo)
        elif self.__projection == 'XZ':
            p.drawRect(xlo, zlo, xhi - xlo, zhi - zlo)
        elif self.__projection == 'YZ':
            p.drawRect(ylo, zlo, yhi - ylo, zhi - zlo)
        else:
            print('ERROR:',
                  'AtomicWidget.paintEvent()',
                  'some error in projection')
        p.end()
        self.__stringsDrawn = 0

    def scale(self):
        return self.__scale

    def setScale(self, scale):
        if scale != 0:
            self.__scale = scale

    def physicalAtomicSystem(self):
        return self.__physicalAtomicSystem

    def drawingStyle(self):
        return self.__drawingStyle
