#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Structure.LAMMPSFullSystem import LAMMPSFullSystem
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData
from Structure.DrawnSystem import DrawnSystem
from Graphics.DrawingStyle import DrawingStyle


class UserCommandsExecutor:
    """
        Transforms the string of commands into the sequence of the function calls.
    """
    def __init__(self, atomicWidget, mainWidget):
        self.__aw = atomicWidget
        self.__mw = mainWidget

##### general methods
    def exit(self, exitString):
        print(exitString)
        print('bye!')
        import sys
        sys.exit()

    def loadFromFile(self, fname):
        #print('UserCommandExecutor, loading system from file', fname)
        rld = ReaderLAMMPSData(fname=fname, atomicStyle='full')
        lmpFullSystem = LAMMPSFullSystem(method='manual',
                                         atoms=rld.parsedAtoms(),
                                         bonds=rld.parsedBonds(),
                                         angles=rld.parsedAngles(),
                                         dihedrals=rld.parsedDihedrals(),
                                         impropers=rld.parsedImpropers(),
                                         boundaries=rld.parsedBoundaries())
        drawnSystem = DrawnSystem(LAMMPSFullSystem=lmpFullSystem)
        self.__aw.updateProperty('LAMMPSFullSystem', lmpFullSystem)
        self.__aw.updateProperty('drawnSystem', drawnSystem)
        self.__aw.update()

##### methods to manipulate with a displayed picture
    # (not the physical system!)
    def setProjection(self, projection):
        self.__aw.updateProperty('projection', projection)

    def setDrawingStyle(self, drawingStyleName):
        drawingStyle = DrawingStyle(drawingStyleName)
        self.__aw.updateProperty('drawingStyle', drawingStyle)

    """
    def removeTextStringName(self, stringName):
        self.__aw.removeTextStringName(stringName)

    def addAtomStringName(self, stringName):
        self.__aw.addAtomStringName(stringName)

    def addTextStringName(self, stringName):
        self.__aw.addTextStringName(stringName)
    """

    def setAtomColor(self, color):
        drawingStyle = self.__aw.getProperty('drawingStyle')
        drawingStyle.updateProperty('atomColor', color)
        drawingStyle.updateProperty('atomColorPolicy', 'common')

    def setAtomRadius(self, radius):
        drawingStyle = self.__aw.getProperty('drawingStyle')
        drawingStyle.updateProperty('commonAtomRadius', radius)
        drawingStyle.updateProperty('atomRadiusPolicy', 'common')

    def setBondColor(self, color):
        drawingStyle = self.__aw.getProperty('drawingStyle')
        drawingStyle.updateProperty('bondColor', color)
        drawingStyle.updateProperty('bondColorPolicy', 'common')

##### methods to manipulate with the physical system
    def moveAtomsAlongX(self, offsetAlongX):
        system = self.__aw.getProperty('LAMMPSFullSystem')
        if system is not None:
            for lmpAtom in system.getProperty('atoms'):
                lmpAtom.moveAlongXAxis(offsetAlongX)
        else:
            print('ERROR, uce.moveAtomsAlongX:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return
        drawnSystem = DrawnSystem(LAMMPSFullSystem=system)
        self.__aw.updateProperty('LAMMPSFullSystem', system)

    def moveAtomsAlongY(self, offsetAlongY):
        system = self.__aw.getProperty('LAMMPSFullSystem')
        if system is not None:
            for lmpAtom in system.getProperty('atoms'):
                lmpAtom.moveAlongYAxis(offsetAlongY)
        else:
            print('ERROR, uce.moveAtomsAlongY:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return
        drawnSystem = DrawnSystem(LAMMPSFullSystem=system)
        self.__aw.updateProperty('LAMMPSFullSystem', system)

    def moveAtomsAlongZ(self, offsetAlongZ):
        system = self.__aw.getProperty('LAMMPSFullSystem')
        if system is not None:
            for lmpAtom in system.getProperty('atoms'):
                lmpAtom.moveAlongZAxis(offsetAlongZ)
        else:
            print('ERROR, uce.moveAtomsAlongZ:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return
        drawnSystem = DrawnSystem(LAMMPSFullSystem=system)
        self.__aw.updateProperty('LAMMPSFullSystem', system)
