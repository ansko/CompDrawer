#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Base import Base


class DrawingStyle(Base):
    def __init__(self,
                 styleName,
                 backgroundColor=None,
                 penColor=None,
                 brushColor=None):
        Base.__init__(self)
        self.__setProperties = dict()
        self.updateProperty('className', 'DrawingStyle')
        self.__defaultAtomRadius = 50    # To indicate unset value
        if styleName in [None, 'default']:
            self.updateProperty('styleName', 'default')
            self.__atomPen = QPen(Qt.black)
            self.__atomBrush = QBrush(Qt.black)
            self.__bondPen = QPen(Qt.black)
            self.__bondBrush = QBrush(Qt.black)
            self.__commonAtomRadius = 50
        elif styleName == 'custom':
            self.updateProperty('styleName', 'custom')
            self.__atomPen = Qt.NoPen
            self.__atomBrush = Qt.NoBrush
            self.__bondPen = Qt.NoPen
            self.__bondBrush = Qt.NoBrush
        else:
            print('ERROR, DrawingStyle.__init__():',
                  'unsupported drawing style',
                  'specified style name is', styleName)
            return

    def atomPen(self, drawnAtom):
        if self.getProperty('styleName') in ['default',]:
            return self.__atomPen
        elif self.getProperty('styleName') == 'custom':
            if self.getProperty('atomColorPolicy')  == 'common':
                self.__atomPen = QPen(self.getProperty('atomColor'))
                return self.__atomPen

    def atomRadius(self, drawnAtom):
        if self.getProperty('atomRadiusPolicy') == 'common':
            if self.getProperty('commonAtomRadius') is not None:
                return self.getProperty('commonAtomRadius')
            else:
                print('ERROR, DrawingStyle.atomRadius():',
                      'request for the default radius, but it is None')
                return
        else:
            print('ERROR, DrawingStyle.atomRadius:',
                  'atomRadiusPolicy is not set')
            return
        return None

    def atomBrush(self, drawnAtom):
        if self.getProperty('styleName') in ['default',]:
            return self.__atomBrush
        elif self.getProperty('styleName') == 'custom':
            # Later it will depend on the drawnAtom.
            if self.getProperty('atomColorPolicy') == 'common':
                brush = QBrush(self.getProperty('atomColor'))
                self.__atomBrush = brush
            return self.__atomBrush

    def bondPen(self, drawnBond):
        if self.getProperty('styleName') in ['default',]:
            return self.__bondPen
        elif self.getProperty('styleName') == 'custom':
            if self.getProperty('bondColorPolicy')  == 'common':
                self.__bondPen = QPen(self.getProperty('bondColor'))
            return self.__bondPen

    def bondBrush(self, drawnBond):
        if self.getProperty('styleName') in ['default',]:
            return self.__bondBrush
        elif self.getProperty('styleName') == 'custom':
            if self.getProperty('bondColorPolicy')  == 'common':
                self.__bondBrush = QBrush(self.getProperty('bondColor'))
            return self.__bondBrush

    def addLocation(self):
        if len(self.__textLocations) == 0:
            y = 10
        else:
            y = self.__textLocations[-1].y() + 10
        self.__textLocations.append(QPointF(0, y))

    def removeLocation(self):
        if len(self.__textLocations) == 0:
            return
        elif len(self.__textLocations) == 1:
            self.__textLocations = []
        else:
            self.__textLocations = self.__textLocations[0:-1]
