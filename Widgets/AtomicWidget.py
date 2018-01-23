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
R = 5
SIZEX = 500
SIZEY = 500
SIZEZ = 500


class AtomicWidget(QLabel):
    """
        This widget is done to draw all atoms in the system.
        By default it draws lonesome hydrogen atom, because that is what default.
    system contains.
    """
    def __init__(self,
                 atomicSystem=AtomicSystem(method="from file",
                                           fname="DataExamples/MT2EtOH_cvff.data"),
                                           drawingStyle='primitive'):
        super().__init__()
        self.setFixedSize(SIZEX, SIZEY) # Maybe it will be possible manually set
                                        # this parameters later.
        self.__atomicSystem = atomicSystem
        self.__drawingStyle = drawingStyle
        self.__paintingOffsetX = 0
        self.__paintinfOffsetY = 0
        self.__paintingOffsetZ = 0
        xmin = atomicSystem.atoms()[0].atomX()
        xmax = atomicSystem.atoms()[0].atomX()
        ymin = atomicSystem.atoms()[0].atomY()
        ymax = atomicSystem.atoms()[0].atomY()
        zmin = atomicSystem.atoms()[0].atomZ()
        zmax = atomicSystem.atoms()[0].atomZ()
        for atom in atomicSystem.atoms():
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
        self.__multiplierX = SIZEX / (lx + 2 * R)
        self.__multiplierY = SIZEY / (ly + 2 * R)
        self.__multiplierZ = SIZEZ / (lz + 2 * R)
        self.__centerX = (xmax + xmin) / 2
        self.__centerY = (ymax + ymin) / 2
        self.__centerZ = (zmax + zmin) / 2
        self.__paintingOffsetX = -self.__centerX
        self.__paintingOffsetY = -self.__centerY
        self.__paintingOffsetZ = -self.__centerZ
    """
        Draft implementation, start. [2018-01-22/16:57]
    """
    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.scale(1, -1)
        p.translate(self.width() / 2, -self.height() / 2)
        p.setPen(QPen())
        p.setBrush(QBrush(Qt.black))
        if self.__atomicSystem.atoms() is None:
            return
        for atom in self.__atomicSystem.atoms():
            x = (atom.atomX() + self.__paintingOffsetX) * self.__multiplierX
            y = (atom.atomY() + self.__paintingOffsetY) * self.__multiplierY
            z = (atom.atomZ() + self.__paintingOffsetZ) * self.__multiplierZ
            p.drawEllipse(x - R,
                          z - R,
                          2 * R,
                          2 * R)
        for i in range(len(self.__atomicSystem.atoms())):
            atom = self.__atomicSystem.atoms()[i]
            x = (atom.atomX() + self.__paintingOffsetX) * self.__multiplierX
            y = (atom.atomY() + self.__paintingOffsetY) * self.__multiplierY
            z = (atom.atomZ() + self.__paintingOffsetZ) * self.__multiplierZ
            for nextAtom in atom.neighbours():
                nextX = (nextAtom.atomX() +
                         self.__paintingOffsetX) * self.__multiplierX
                nextY = (nextAtom.atomY() +
                         self.__paintingOffsetY) * self.__multiplierY
                nextZ = (nextAtom.atomZ() +
                         self.__paintingOffsetZ) * self.__multiplierZ
                p.drawLine(x, z, nextX, nextZ)
        p.end()
    """
        Draft implementation, end. [2018-01-22/16:57]
    """

    def atomicSystem(self):
        return self.__atomicSystem

    def drawingStyle(self):
        return self.__drawingStyle
