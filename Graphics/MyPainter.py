#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Base import Base
from Graphics.DrawingStyle import DrawingStyle


class MyPainter(QPainter, Base):
    def __init__(self):
        QPainter.__init__(self)
        Base.__init__(self)

    def begin(self, widget):
        super().begin(widget)
        self.updateProperty('parentWidget', widget)
        self.updateProperty('projection', widget.getProperty('projection'))

    def drawDrawnSystem(self, drawnSystem):
        if drawnSystem is None:
            print('ERROR, MyPainter.drawDrawnSystem:',
                  'drawnSystem is None')
            return
        drawnAtoms = drawnSystem.getProperty('drawnAtoms')
        drawnBonds = drawnSystem.getProperty('drawnBonds')
        for bond in drawnBonds:
            self.drawDrawnBond(bond)
        for atom in drawnAtoms:
            self.drawDrawnAtom(atom)

    def drawLegend(self):
        pass

    def drawAxes(self):
        self.drawLine(0, 0, 245, 0)
        self.drawLine(0, 0, 0, -245)
        self.drawText(230, 15, self.__projection[0])
        self.drawText(-10, -240, self.__projection[1])

    def drawDrawnAtom(self, drawnAtom):
        r = 5#self.__drawingStyle.atomRadius(drawnAtom)
        pen = QPen()# self.__drawingStyle.atomPen(drawnAtom)
        brush = QBrush()#self.__drawingStyle.atomBrush(drawnAtom)
        self.setPen(pen)
        self.setBrush(brush)
        projection = self.getProperty('projection')
        sysProps = self.getProperty('parentWidget').\
                        getProperty('drawnSystem').getProperty
        if projection in [None, 'XY']:
            dx = sysProps(propertyName='offsetX')
            dy = sysProps(propertyName='offsetY')
            x = drawnAtom.getProperty('atomX')
            y = drawnAtom.getProperty('atomY')
        elif projection == 'XZ':
            dx = sysProps(propertyName='offsetX')
            dy = sysProps(propertyName='offsetZ')
            x = drawnAtom.getProperty('atomX')
            y = drawnAtom.getProperty('atomZ')
        elif projection == 'YZ':
            dx = sysProps(propertyName='offsetX')
            dy = sysProps(propertyName='offsetZ')
            x = drawnAtom.getProperty('atomY')
            y = drawnAtom.getProperty('atomZ')
        scale = sysProps('scale')
        self.drawEllipse((x + dx) * scale - r,
                         (y + dy) * scale - r,
                         2 * r, 2 * r)

    def drawDrawnBond(self, drawnBond):
        pen = QPen()# self.__drawingStyle.bondPen(drawnBond)
        brush = QBrush()# self.__drawingStyle.bondBrush(drawnBond)
        self.setPen(pen)
        self.setBrush(brush)
        atomOne = drawnBond.getProperty(propertyName='LAMMPSAtomOne')
        atomTwo = drawnBond.getProperty(propertyName='LAMMPSAtomTwo')
        if atomOne is None:
            print('ERROR, MyPainter.drawDrawBond():',
                  'atomOne is None')
            return None
        if atomTwo is None:
            print('ERROR, MyPainter.drawDrawBond():',
                  'atomTwo is None')
            return None
        projection = self.getProperty('projection')
        if projection is None:
            print('ERROR, MyPainter.drawDrawBond():',
                  'projection is None')
            return None
        if self.getProperty('parentWidget').getProperty('drawnSystem') is None:
            print('ERROR, MyPainter.drawDrawBond():',
                  'drawnSystem is None')
            return None
        sysProps = self.getProperty('parentWidget').\
                        getProperty('drawnSystem').getProperty
        if projection == 'XY':
            dx = sysProps(propertyName='offsetX')
            dy = sysProps(propertyName='offsetY')
            if atomOne.getProperty('typeName') =='AtomLAMMPSRealFull':
                x1 = atomOne.atomX()
                y1 = atomOne.atomY()
            else:
                x1 = atomOne.getProperty(propertyName='atomX')
                y1 = atomOne.getProperty(propertyName='atomY')
            if atomTwo.getProperty('typeName') =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomX()
                y2 = atomTwo.atomY()
            else:
                x2 = atomTwo.getProperty(propertyName='atomX')
                y2 = atomTwo.getProperty(propertyName='atomY')
        elif projection == 'XZ':
            dx = sysProps(propertyName='offsetX')
            dy = sysProps(propertyName='offsetZ')
            if atomOne.getProperty('typeName') =='AtomLAMMPSRealFull':
                x1 = atomOne.atomX()
                y1 = atomOne.atomZ()
            else:
                x1 = atomOne.getProperty(propertyName='atomX')
                y1 = atomOne.getProperty(propertyName='atomZ')
            if atomTwo.getProperty('typeName') =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomX()
                y2 = atomTwo.atomZ()
            else:
                x2 = atomTwo.getProperty(propertyName='atomX')
                y2 = atomTwo.getProperty(propertyName='atomZ')
        elif projection == 'YZ':
            dx = sysProps(propertyName='offsetY')
            dy = sysProps(propertyName='offsetZ')
            if atomOne.getProperty('typeName') =='AtomLAMMPSRealFull':
                x1 = atomOne.atomY()
                y1 = atomOne.atomZ()
            else:
                x1 = atomOne.getProperty(propertyName='atomY')
                y1 = atomOne.getProperty(propertyName='atomZ')
            if atomTwo.getProperty('typeName') =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomY()
                y2 = atomTwo.atomZ()
            else:
                x2 = atomTwo.getProperty(propertyName='atomY')
                y2 = atomTwo.getProperty(propertyName='atomZ')
        else:
            print('ERROR, mp.ddb():',
                  'unknown projection',
                  'set projection is', projection)
            return
        if x1 is None:
            print('ERROR, mp.ddb():',
                  'x1 is None')
            return
        if x2 is None:
            print('ERROR, mp.ddb():',
                  'x2 is None')
            return
        if y1 is None:
            print('ERROR, mp.ddb():',
                  'y1 is None')
            return
        if y2 is None:
            print('ERROR, mp.ddb():',
                  'y2 is None')
            return
        if dx is None:
            print('ERROR, mp.ddb():',
                  'dx is None')
            return
        if dy is None:
            print('ERROR, mp.ddb():',
                  'dy is None')
            return
        scale = sysProps('scale')
        if scale is None:
            scale = 1
            print('WARNING, mp.ddb:',
                  'scale is None')
        self.drawLine((x1 + dx) * scale,
                      (y1 + dy) * scale,
                      (x2 + dx) * scale,
                      (y2 + dy) * scale)
