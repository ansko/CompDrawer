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
       # default values to see easily if there is some error
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
        #self.translate(self.__widgetConnectedWith.width() / 2,
        #               self.__widgetConnectedWith.height() / 2)

    def end(self):
        #self.translate(-self.__widgetConnectedWith.width() / 2,
        #               -self.__widgetConnectedWith.height() / 2)
        super().end()

    def setScale(self, scale):
        self.__scale = scale

    def setRadius(self, r):
        self.__r = r

    def setProjection(self, projection):
        self.__projection = projection

    def setDrawnSystem(self, drawnSystem):
        self.__drawnSystem = drawnSystem

    def drawAxes(self):
        self.drawLine(0, 0, 100, 0)
        self.drawLine(0, 0, 0, -100)
        self.drawText(95, 15, self.__projection[0])
        self.drawText(-10, -95, self.__projection[1])

    def drawDrawnAtom(self, drawnAtom):
        self.setPen(QPen())

        if self.__projection in [None, 'XY']:
            x = (drawnAtom.getPropertyValue('atomX') + 
                 drawnAtom.getPropertyValue('offsetX')) * self.__scale
            y = (drawnAtom.getPropertyValue('atomY') +
                 drawnAtom.getPropertyValue('offsetY')) * self.__scale
        elif self.__projection == 'XZ':
            x = (drawnAtom.getPropertyValue('atomX') +
                 drawnAtom.getPropertyValue('offsetX')) * self.__scale
            y = (drawnAtom.getPropertyValue('atomZ') +
                 drawnAtom.getPropertyValue('offsetZ')) * self.__scale
        elif self.__projection == 'YZ':
            x = (drawnAtom.getPropertyValue('atomY') +
                 drawnAtom.getPropertyValue('offsetY')) * self.__scale
            y = (drawnAtom.getPropertyValue('atomZ') +
                 drawnAtom.getPropertyValue('offsetZ')) * self.__scale
        r = self.__r
        self.drawEllipse(x - r, y - r, 2 * r, 2 * r)

    def drawDrawnBond(self, drawnBond):
        print('mp.ddb, drawDrawnBond not implemented yet')
