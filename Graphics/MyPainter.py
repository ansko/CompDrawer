#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Graphics.DrawingStyles.DrawingStyle import DrawingStyle


class MyPainter(QPainter):
    def __init__(self, drawingStyle=None):
        super().__init__()
        if drawingStyle is not None:
            self.__drawingStyle = drawingStyle
        else:
            self.__drawingStyle = DrawingStyle(None)
       # default values to indicate if there is some error
        self.__projection = None
        self.__scale = 1
        self.__r = 50
        self.__drawnSystem = None
       # tmp code
        self.__atomPen = self.__drawingStyle.atomPen(self)
        self.__atomBrush = self.__drawingStyle.atomBrush(self)

    def begin(self, widget):
        super().begin(widget)
        self.__widgetConnectedWith = widget

    def setScale(self, scale):
        self.__scale = scale

    def setRadius(self, r):
        self.__r = r

    def setProjection(self, projection):
        self.__projection = projection

    def setDrawnSystem(self, drawnSystem):
        self.__drawnSystem = drawnSystem

    def drawLegend(self):
        pass

    def drawAxes(self):
        self.drawLine(0, 0, 245, 0)
        self.drawLine(0, 0, 0, -245)
        self.drawText(230, 15, self.__projection[0])
        self.drawText(-10, -240, self.__projection[1])

    def drawDrawnAtom(self, drawnAtom):
        r = self.__drawingStyle.atomRadius(drawnAtom)
        pen = self.__drawingStyle.atomPen(drawnAtom)
        brush = self.__drawingStyle.atomBrush(drawnAtom)
        self.setPen(pen)
        self.setBrush(brush)
        if self.__projection in [None, 'XY']:
            dx = self.__drawnSystem.getPropertyValue('offsetX')
            dy = self.__drawnSystem.getPropertyValue('offsetY')
            x = drawnAtom.getPropertyValue('atomX')
            y = drawnAtom.getPropertyValue('atomY')
        elif self.__projection == 'XZ':
            dx = self.__drawnSystem.getPropertyValue('offsetX')
            dy = self.__drawnSystem.getPropertyValue('offsetZ')
            x = drawnAtom.getPropertyValue('atomX')
            y = drawnAtom.getPropertyValue('atomZ')
        elif self.__projection == 'YZ':
            dx = self.__drawnSystem.getPropertyValue('offsetY')
            dy = self.__drawnSystem.getPropertyValue('offsetZ')
            x = drawnAtom.getPropertyValue('atomY')
            y = drawnAtom.getPropertyValue('atomZ')
        self.drawEllipse((x + dx) * self.__scale - r,
                         (y + dy) * self.__scale - r,
                         2 * r, 2 * r)

    def drawDrawnBond(self, drawnBond):
        pen = self.__drawingStyle.bondPen(drawnBond)
        brush = self.__drawingStyle.bondBrush(drawnBond)
        self.setPen(pen)
        self.setBrush(brush)
        atomOne = drawnBond.getPropertyValue(propertyName='physicalAtomOne')
        atomTwo = drawnBond.getPropertyValue(propertyName='physicalAtomTwo')
        if self.__projection == 'XY':
            dx = self.__drawnSystem.getPropertyValue(propertyName='offsetX')
            dy = self.__drawnSystem.getPropertyValue(propertyName='offsetY')
           # maybe AtomLAMMPSRealFull should be implemented like others?...
            if atomOne.atomTypeName() =='AtomLAMMPSRealFull':
                x1 = atomOne.atomX()
                y1 = atomOne.atomY()
            else:
                x1 = atomOne.getPropertyValue(propertyName='atomX')
                y1 = atomOne.getPropertyValue(propertyName='atomY')
            if atomTwo.atomTypeName() =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomX()
                y2 = atomTwo.atomY()
            else:
                x2 = atomTwo.getPropertyValue(propertyName='atomX')
                y2 = atomTwo.getPropertyValue(propertyName='atomY')
        elif self.__projection == 'XZ':
            dx = self.__drawnSystem.getPropertyValue(propertyName='offsetX')
            dy = self.__drawnSystem.getPropertyValue(propertyName='offsetZ')
            if atomOne.atomTypeName() =='AtomLAMMPSRealFull':
                x1 = atomOne.atomX()
                y1 = atomOne.atomZ()
            else:
                x1 = atomOne.getPropertyValue(propertyName='atomX')
                y1 = atomOne.getPropertyValue(propertyName='atomZ')
            if atomTwo.atomTypeName() =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomX()
                y2 = atomTwo.atomZ()
            else:
                x2 = atomTwo.getPropertyValue(propertyName='atomX')
                y2 = atomTwo.getPropertyValue(propertyName='atomZ')
        elif self.__projection == 'YZ':
            dx = self.__drawnSystem.getPropertyValue(propertyName='offsetY')
            dy = self.__drawnSystem.getPropertyValue(propertyName='offsetZ')
            if atomOne.atomTypeName() =='AtomLAMMPSRealFull':
                x1 = atomOne.atomY()
                y1 = atomOne.atomZ()
            else:
                x1 = atomOne.getPropertyValue(propertyName='atomY')
                y1 = atomOne.getPropertyValue(propertyName='atomZ')
            if atomTwo.atomTypeName() =='AtomLAMMPSRealFull':
                x2 = atomTwo.atomY()
                y2 = atomTwo.atomZ()
            else:
                x2 = atomTwo.getPropertyValue(propertyName='atomY')
                y2 = atomTwo.getPropertyValue(propertyName='atomZ')
        else:
            print('ERROR, mp.ddb():',
                  'unknown projection',
                  'your projection is', self.__projection)
            return
        self.drawLine((x1 + dx) * self.__scale,
                      (y1 + dy) * self.__scale,
                      (x2 + dx) * self.__scale,
                      (y2 + dy) * self.__scale)
