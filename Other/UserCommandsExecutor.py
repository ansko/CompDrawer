#!/usr/bin/env python3
#coding=utf-8


# my imports
from Other.AtomicSystem import AtomicSystem
from Other.ParserLAMMPSData import ParserLAMMPSData


class UserCommandsExecutor:
    """
        Transforms the string of commands into the sequence of the function calls.
    """
    def __init__(self, atomicWidget, mainWidget):
        self.__aw = atomicWidget
        self.__mw = mainWidget

    def moveAlongX(self, atomicSystem, offsetAlongX):
        print('UserCommandExecutor, moving atoms along x axis')
        for atom in atomicSystem.atoms():
            atom.mooveAlongXAxis(offsetAlongX)

    def moveAlongY(self, atomicSystem, offsetAlongY):
        print('UserCommandExecutor, moving atoms along y axis')
        for atom in atomicSystem.atoms():
            atom.mooveAlongYAxis(offsetAlongY)

    def moveAlongZ(self, atomicSystem, offsetAlongZ):
        print('UserCommandExecutor, moving atoms along z axis')
        for atom in  atomicSystem.atoms():
            atom.mooveAlongZAxis(offsetAlongZ)

    def loadFromFile(self, fname):
        print('UserCommandExecutor, loading system from file', fname)
        pld = ParserLAMMPSData(fname=fname, atomicStyle='full')
        atomicSystem = AtomicSystem(method='manual',
                                    atoms=pld.parsedAtoms(),
                                    bonds=pld.parsedBonds(),
                                    angles=pld.parsedAngles(),
                                    dihedrals=pld.parsedDihedrals(),
                                    impropers=pld.parsedImpropers())
        self.__aw.setAtomicSystem(atomicSystem=atomicSystem)

    def setProjection(self, projection):
        print('UserCommandExecutor, setting the projection', projection)
        self.__aw.setProjection(projection)
