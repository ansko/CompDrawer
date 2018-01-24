#!/usr/bin/env python3
#coding=utf-8


# my imports
from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem
from Other.ParserLAMMPSData import ParserLAMMPSData


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
        print('UserCommandExecutor, loading system from file', fname)
        pld = ParserLAMMPSData(fname=fname, atomicStyle='full')
        physicalAtomicSystem = PhysicalAtomicSystem(method='manual',
                                            atoms=pld.parsedAtoms(),
                                            bonds=pld.parsedBonds(),
                                            angles=pld.parsedAngles(),
                                            dihedrals=pld.parsedDihedrals(),
                                            impropers=pld.parsedImpropers(),
                                            ranges=pld.parsedRanges())
        self.__aw.setPhysicalAtomicSystem(
                                         physicalAtomicSystem=physicalAtomicSystem)

##### methods to manipulate with a displayed picture
    # (not the physical system!)
    def setProjection(self, projection):
        print('UserCommandExecutor, setting the projection', projection)
        self.__aw.setProjection(projection)

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
