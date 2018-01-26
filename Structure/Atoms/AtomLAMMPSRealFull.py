#!/usr/bin/env python3
#coding=utf-8


class AtomLAMMPSRealFull:
    """
        Describes LAMMPS "full" atom in "real" units.
        Default parameters stand for isolated hydrogen atom with zero velocity in
    the coordinates begining. Its type is "1", its molecule is also "1". Flags are
    also set to zero. Unforrtunately, at this moment I do not understand their
    purpose.
    ***
        Maybe it is not a good practice to have internal variables with names
    that differ from the methods of the access to them. Maybe it should be done
    in a better way some day.
    ***
    """
    def __init__(self,
                 atomNumber=1,
                 moleculeNumber=1,
                 atomType=1, # forcefield type
                 atomCharge=1,
                 atomMass=None, # it may be specified optionally
                 atomX=0,
                 atomY=0,
                 atomZ=0,
                 atomFlagOne=0,
                 atomFlagTwo=0,
                 atomFlagThree=0,
                 atomComment=None,
                 atomVx=0,
                 atomVy=0,
                 atomVz=0):
        self.__atomTypeName = 'AtomLAMMPSRealFull'
        self.__atomNumber = atomNumber
        self.__moleculeNumber = moleculeNumber
        self.__atomType = atomType
        self.__atomCharge = atomCharge
        self.__atomMass = atomMass
        self.__x = atomX
        self.__y = atomY
        self.__z = atomZ
        self.__flagOne = atomFlagOne
        self.__flagTwo = atomFlagTwo
        self.__flagThree = atomFlagThree
        self.__comment = atomComment
        self.__Vx = atomVx
        self.__Vy = atomVy
        self.__Vz = atomVz
        self.__connectedWith = set()

    def atomTypeName(self):
        return self.__atomTypeName

    def setAtomNumber(self, atomNumber):
       """
           This function is made for structure manipulations, when atomNumber
       can change (for example, after deletion or insertion of some atoms).
       """
       self.__atomNumber = atomNumber

    def setAtomMass(self, atomMass):
       """
           Atom Masses in datafile are stored ni a different place than other
       charactristics, so I suppose this method to be useful.
       """
       self.__atomMass = atomMass

    def setAtomX(self, atomX):
        self.__x = atomX

    def setAtomY(self, atomY):
        self.__y = atomY

    def setAtomZ(self, atomZ):
        self.__z = atomZ

    def mooveAlongXAxis(self, dx):
        self.__x += dx

    def mooveAlongYAxis(self, dy):
        self.__y += dy

    def mooveAlongZAxis(self, dz):
        self.__z += dz

    def move(self, dx, dy, dz):
        self.__x += dx
        self.__y += dy
        self.__z += dz

    def setAtomVx(self, atomVx):
        self.__Vx = atomVx

    def setAtomVy(self, atomVy):
        self.__Vy = atomVy

    def setAtomVz(self, atomVz):
        self.__Vz = atomVz

    def addNeighbour(self, neighbour):
        self.__connectedWith.add(neighbour)

    def atomNumber(self):
        return self.__atomNumber

    def moleculeNumber(self):
        return self.__moleculeNumber

    def atomType(self):
        return self.__atomType

    def atomCharge(self):
        return self.__atomCharge

    def atomMass(self):
        return self.__atomMass

    def atomX(self):
        return self.__x

    def atomY(self):
        return self.__y

    def atomZ(self):
        return self.__z

    def atomFlagOne(self):
        return self.__flagOne

    def atomFlagTwo(self):
        return self.__flagTwo

    def atomFlagThree(self):
        return self.__flagThree

    def atomComment(self):
        return self.__comment

    def atomVx(self):
        return self.__Vx

    def atomVy(self):
        return self.__Vy

    def atomVz(self):
        return self.__Vz

    def neighbours(self):
        return self.__connectedWith
