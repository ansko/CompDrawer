#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Other.AtomicSystem import AtomicSystem


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
    def __init__(self, drawingStyle):
        super().__init__()
        self.__drawingStyle = drawingStyle
        self.__paintingOffsetX = 0
        self.__paintingOffsetY = 0
        self.__paintingOffsetZ = 0
        self.__guestAtomicSystems = []
        self.__scale = 1
        self.__atomicSystem = None
        self.__projection = 'XY'

    def setAtomicSystem(self, atomicSystem):
        self.__atomicSystem = atomicSystem
        self.__initUI()

    def setProjection(self, projection):
        if projection in ['XY', 'XZ', 'YZ']:
            self.__projection = projection
            self.update()

    def setDrawingStyle(self, drawingStyle):
        self.__drawingStyle = drawingStyle

    def atomicSystem(self):
        return self.__atomicSystem

    def drawingStyle(self):
        return self.__drawingStyle

    def __initUI(self):
        xmin = self.__atomicSystem.atoms()[0].atomX()
        xmax = self.__atomicSystem.atoms()[0].atomX()
        ymin = self.__atomicSystem.atoms()[0].atomY()
        ymax = self.__atomicSystem.atoms()[0].atomY()
        zmin = self.__atomicSystem.atoms()[0].atomZ()
        zmax = self.__atomicSystem.atoms()[0].atomZ()
        for atom in self.__atomicSystem.atoms():
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

    """
        Draft implementation, start. [2018-01-22/16:57]
    """
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setPen(QPen())
        p.setBrush(QBrush(Qt.black))
        p.drawText(QPointF(0,
                           10),
                   'scale = ' + str(round(self.__scale, 1)))
        p.translate(self.width() / 2, self.height() / 2)
        p.drawLine(0, 0, 0, -250)
        p.drawText(5, -240, self.__projection[1])
        p.drawText(230, -10, self.__projection[0])
        p.drawLine(0, 0, 250, 0)
        p.scale(1, -1)
        if self.__atomicSystem is None:
            return
        if self.__atomicSystem.atoms() is None:
            return
        for atom in self.__atomicSystem.atoms():
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
        for bond in self.__atomicSystem.bonds():
            if True in bond.crosses():
                continue
            x = bond.atomOne().atomX()
            otherX = bond.atomTwo().atomX()
            y = bond.atomOne().atomY()
            otherY = bond.atomTwo().atomY()
            z = bond.atomOne().atomZ()
            otherZ = bond.atomTwo().atomZ()
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
        p.end()
    """
        Draft implementation, end. [2018-01-22/16:57]
    """

    def atomicSystem(self):
        return self.__atomicSystem

    def guestAtomicSystems(self):
        return self.__guestAtomicSystems

    def drawingStyle(self):
        return self.__drawingStyle

    def addAtomicSystem(self, atomicSystem):
        self.__guestAtomicSystems.append(atomicSystem)
