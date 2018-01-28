#!/usr/bin/env python3
#coding=utf-8


from Base import Base


# constants, this is bad!
TOO_LONG_BOND_MAX_LENGTH = 5


class BondLAMMPS(Base):
    def __init__(self,
                 bondNumber,
                 bondType,
                 atomOne,
                 atomTwo):
        Base.__init__(self)
        self.updateProperty('className', 'bondLAMMPS')
        self.updateProperty('bondNumber', bondNumber)
        self.updateProperty('bondType', bondType)
        self.updateProperty('atomOne', atomOne)
        self.updateProperty('atomTwo', atomTwo)

    def setBoxBoundaries(self, boundaries):
        self.updateProperty('boundaries', boundaries)
        self.__normalizeLength()

    def __normalizeLength(self):
        if self.getProperty('boundaries') is None:
            print('ERROR, BondLAMMPS.__normalizeLength():',
                  'box boundaries are not specified')
            return None
        xhi = self.getProperty('boundaries')[0]
        xlo = self.getProperty('boundaries')[1]
        yhi = self.getProperty('boundaries')[2]
        ylo = self.getProperty('boundaries')[3]
        zhi = self.getProperty('boundaries')[4]
        zlo = self.getProperty('boundaries')[5]
        xBoxLen = xhi - xlo
        yBoxLen = yhi - ylo
        zBoxLen = zhi - zlo
        atomOne = self.getProperty('atomOne')
        atomTwo = self.getProperty('atomTwo')
        dx = atomOne.getProperty('atomX') - atomTwo.getProperty('atomX')
        if abs(dx) > TOO_LONG_BOND_MAX_LENGTH:
            self.updatePRoperty('crossesX', True)
        dy = atomOne.getProperty('atomY') - atomTwo.getProperty('atomY')
        if abs(dy) > TOO_LONG_BOND_MAX_LENGTH:
            self.updatePRoperty('crossesY', True)
        dz = atomOne.getProperty('atomZ') - atomTwo.getProperty('atomZ')
        if abs(dz) > TOO_LONG_BOND_MAX_LENGTH:
            self.updatePRoperty('crossesZ', True)
        dx = min(abs(dx), abs(xBoxLen - dx))
        dy = min(abs(dy), abs(yBoxLen - dy))
        dz = min(abs(dz), abs(zBoxLen - dz))
        self.updateProperty('length', (dx**2 + dy**2 + dz**2)**0.5)
