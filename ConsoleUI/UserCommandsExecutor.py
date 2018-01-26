#!/usr/bin/env python3
#coding=utf-8


# my imports
from Structure.PhysicalSystem import PhysicalSystem
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData
from Graphics.DrawnSystem import DrawnSystem
from Graphics.DrawingStyles.DrawingStyle import DrawingStyle
from Graphics.DrawingRules.DrawingRule import DrawingRule

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
        physicalSystem = PhysicalSystem(method='manual',
                                        atoms=rld.parsedAtoms(),
                                        bonds=rld.parsedBonds(),
                                        angles=rld.parsedAngles(),
                                        dihedrals=rld.parsedDihedrals(),
                                        impropers=rld.parsedImpropers(),
                                        boundaries=rld.parsedBoundaries())
        #print('uce.lff()', rld.parsedAtoms()[0].atomX())
        drawnSystem = DrawnSystem(physicalSystem=physicalSystem)
        self.__aw.setPhysicalSystem(physicalSystem=physicalSystem)
        #self.__aw.setDrawnSystem(drawnSystem=drawnSystem) # no need, because
                                                           # setPhysicalSystem
                                                           # automatically calls
                                                           # setDrawnSystem

##### methods to manipulate with a displayed picture
    # (not the physical system!)
    def setProjection(self, projection):
        self.__aw.setProjection(projection)

    def setDrawingStyle(self, drawingStyleName):
        drawingStyle = DrawingStyle(drawingStyleName)
        self.__aw.setDrawingStyle(drawingStyle)

    def setDrawingRule(self, drawingRuleName):
        drawingRule = DrawingRule(drawingRuleName)
        self.__aw.setDrawingRule(drawingRule)

    def removeTextStringName(self, stringName):
        self.__aw.removeTextStringName(stringName)

    def addAtomStringName(self, stringName):
        self.__aw.addAtomStringName(stringName)

    def addTextStringName(self, stringName):
        self.__aw.addTextStringName(stringName)

##### methods to manipulate with the physical system
    def moveAtomsAlongX(self, offsetAlongX):
        if self.__aw.physicalSystem() is not None:
            for physicalAtom in self.__aw.physicalSystem().atoms():
                physicalAtom.mooveAlongXAxis(offsetAlongX)
        else:
            print('ERROR, uce.moveAtomsAlongX:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return

    def moveAtomsAlongY(self, offsetAlongY):
        #print('UserCommandExecutor, moving atoms along y axis')
        if self.__aw.physicalSystem() is not None:
            for physicalAtom in self.__aw.physicalSystem().atoms():
                physicalAtom.mooveAlongXAxis(offsetAlongY)
        else:
            print('ERROR, uce.moveAtomsAlongY:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return

    def moveAtomsAlongZ(self, offsetAlongZ):
        #print('UserCommandExecutor, moving atoms along z axis')
        if self.__aw.physicalSystem() is not None:
            for physicalAtom in self.__aw.physicalSystem().atoms():
                physicalAtom.mooveAlongXAxis(offsetAlongZ)
        else:
            print('ERROR, uce.moveAtomsAlongZ:',
                  'physical system is not set',
                  'it is possible to move just image instead of pruposed action')
            return
