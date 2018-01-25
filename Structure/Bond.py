#!/usr/bin/env python3
#coding=utf-8


# constants, this is bad!
TOO_LONG_BOND_MAX_LENGTH = 5

class Bond:
    def __init__(self,
                 bondNumber,
                 bondType,
                 atomOne,
                 atomTwo):
        self.__bondNumber = bondNumber
        self.__bondType = bondType
        self.__atomOne = atomOne
        self.__atomTwo = atomTwo
        self.__xlo = None
        self.__xhi = None
        self.__ylo = None
        self.__yhi = None
        self.__zlo = None
        self.__zhi = None
        self.__length = None
        self.__crossesX = False
        self.__crossesY = False
        self.__crossesZ = False

    def setBoxRanges(self, ranges):
        self.__xlo = ranges[0]
        self.__xhi = ranges[1]
        self.__ylo = ranges[2]
        self.__yhi = ranges[3]
        self.__zlo = ranges[4]
        self.__zhi = ranges[5]
        self.__normalizeLength()

    def __normalizeLength(self):
        xBoxLen = self.__xhi - self.__xlo
        yBoxLen = self.__yhi - self.__ylo
        zBoxLen = self.__zhi - self.__zlo
        dx = self.__atomOne.atomX() - self.__atomTwo.atomX()
        if abs(dx) > TOO_LONG_BOND_MAX_LENGTH:
            self.__crossesX = True
        dy = self.__atomOne.atomY() - self.__atomTwo.atomY()
        if abs(dy) > TOO_LONG_BOND_MAX_LENGTH:
            self.__crossesY = True
        dz = self.__atomOne.atomZ() - self.__atomTwo.atomZ()
        if abs(dz) > TOO_LONG_BOND_MAX_LENGTH:
            self.__crossesZ = True
        dx = min(abs(dx), abs(xBoxLen - dx))
        dy = min(abs(dy), abs(yBoxLen - dy))
        dz = min(abs(dz), abs(zBoxLen - dz))
        self.__length = (dx**2 + dy**2 + dz**2)**0.5

    def crosses(self):
        return (self.__crossesX, self.__crossesY, self.__crossesZ)

    def bondNumber(self):
        return self.__bondNumber

    def setBondNumber(self, bondNumber):
        self.__bondNumber = bondNumber

    def bondType(self):
        return self.__bondType

    def bondAtomOne(self):
        return self.__atomOne

    def bondAtomTwo(self):
        return self.__atomTwo

    def bondLength(self):
        return self.__length
