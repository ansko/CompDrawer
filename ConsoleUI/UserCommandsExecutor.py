#!/usr/bin/env python3
#coding=utf-8


# my imports
from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData
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
        physicalAtomicSystem = PhysicalAtomicSystem(method='manual',
                                            atoms=rld.parsedAtoms(),
                                            bonds=rld.parsedBonds(),
                                            angles=rld.parsedAngles(),
                                            dihedrals=rld.parsedDihedrals(),
                                            impropers=rld.parsedImpropers(),
                                            ranges=rld.parsedRanges())
        self.__aw.setPhysicalAtomicSystem(
                                         physicalAtomicSystem=physicalAtomicSystem)

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
        #print('UserCommandExecutor, moving atoms along x axis')
        for atom in self.__aw.physicalAtomicSystem().atoms():
            atom.mooveAlongXAxis(offsetAlongX)

    def moveAtomsAlongY(self, offsetAlongY):
        #print('UserCommandExecutor, moving atoms along y axis')
        for atom in self.__aw.physicalAtomicSystem().atoms():
            atom.mooveAlongYAxis(offsetAlongY)

    def moveAtomsAlongZ(self, offsetAlongZ):
        #print('UserCommandExecutor, moving atoms along z axis')
        for atom in  self.__aw.physicalAtomicSystem().atoms():
            atom.mooveAlongZAxis(offsetAlongZ)
