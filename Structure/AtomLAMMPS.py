#!/usr/bin/env python3
#coding=utf-8


from Base import Base


class AtomLAMMPS(Base):
    def __init__(self,
                 atomNumber,
                 atomX,
                 atomY,
                 atomZ,
                 moleculeNumber=None,    # * Marked with * may be not
                 atomType=None,          # * specified, but may be
                 atomCharge=None,        # * presented in LAMMPS
                 atomMass=None,          # * datafile. However,
                 atomFlagOne=None,       # * in 'full' atomic style
                 atomFlagTwo=None,       # * they should beset.
                 atomFlagThree=None,     # *
                 atomComment=None,       # *
                 atomVx=None,            # *
                 atomVy=None,            # *
                 atomVz=None):  
        Base.__init__(self)
        self.__setProperties = dict()
        self.updateProperty('className', 'AtomLAMMPS')
        self.updateProperty('atomNumber', atomNumber)
        self.updateProperty('atomX', atomX)
        self.updateProperty('atomY', atomY)
        self.updateProperty('atomZ', atomZ)
        if moleculeNumber is not None:
            self.updateProperty('moleculeNumber', moleculeNumber)
        if atomType is not None:
            self.updateProperty('atomType', atomType)
        if atomCharge is not None:
            self.updateProperty('atomCharge', atomCharge)
        if atomMass is not None:
            self.updateProperty('atomMass', atomMass)
        if atomFlagOne is not None:
            self.updateProperty('atomFlagOne', atomFlagOne)
        if atomFlagTwo is not None:
            self.updateProperty('atomFlagTwo', atomFlagTwo)
        if atomFlagThree is not None:
            self.updateProperty('atomFlagThree', atomFlagThree)
        if atomComment is not None:
            self.updateProperty('atomComment', atomComment)
        if atomVx is not None:
            self.updateProperty('atomVx', atomVx)
        if atomVy is not None:
            self.updateProperty('atomVy', atomVy)
        if atomVz is not None:
            self.updateProperty('atomVz', atomVz)

    def moveAlongXAxis(self, dx):
        x = self.getProperty('atomX')
        x += dx
        self.updateProperty('atomX', x)

    def moveAlongYAxis(self, dy):
        y = self.getProperty('atomY')
        y += dy
        self.updateProperty('atomY', y)

    def moveAlongZAxis(self, dz):
        z = self.getProperty('atomZ')
        z += dz
        self.updateProperty('atomZ', z)
