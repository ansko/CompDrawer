#!/usr/bin/env python3
#coding=utf-8


class UserCommandsExecutor:
    """
        Transforms the string of commands into the sequence of the function calls.
    """
    def __init__(self, atomicSystem):
        self.__atomicSystem = atomicSystem

    def moveAlongX(self, offsetAlongX):
        print('UserCommandExecutor, moving atoms along x axis')
        for atom in self.__atomicSystem.atoms():
            atom.mooveAlongXAxis(offsetAlongX)

    def moveAlongY(self, offsetAlongY):
        print('UserCommandExecutor, moving atoms along y axis')
        for atom in self.__atomicSystem.atoms():
            atom.mooveAlongYAxis(offsetAlongY)

    def moveAlongZ(self, offsetAlongZ):
        print('UserCommandExecutor, moving atoms along z axis')
        for atom in self.__atomicSystem.atoms():
            atom.mooveAlongZAxis(offsetAlongZ)
