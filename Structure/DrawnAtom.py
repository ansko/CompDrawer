#!/usr/bin/env python3
#coding=utf-8


# my imports
from Base import Base

from Structure.AtomLAMMPS import AtomLAMMPS
from Structure.AtomGeometrical import AtomGeometrical


class DrawnAtom(Base):
    def __init__(self,
                # possible atom types
                 atomLAMMPSRealFull=None,
                 atomGeometrical=None,
                 atomPhysical=None,
                # physical variables
                 atomNumber=None,
                 atomX=None,
                 atomY=None,
                 atomZ=None,
                 atomVx=None,
                 atomVy=None,
                 atomVz=None,
                 atomMolecule=None,
                 atomMass=None,
                 atomType=None,
                 atomCharge=None,
                 atomFlagOne=None,
                 atomFlagTwo=None,
                 atomFlagThree=None,
               # drawn variables
                 atomDrawnRadius=None,
                 atomOffsetX = None,
                 atomOffsetY = None,
                 atomOffsetZ = None,
                 selectionState=None, # atomState = active/passive 
                                      # (is it selected or not)
                 paintingVisibility=None):
        Base.__init__(self)
        self.__setProperties = dict()
        if atomLAMMPSRealFull is not None:
            atomProp = atomLAMMPSRealFull.getProperty
            self.updateProperty('atomX', atomProp('atomX'))
            self.updateProperty('atomY', atomProp('atomY'))
            self.updateProperty('atomZ', atomProp('atomZ'))
            self.updateProperty('atomNumber', atomProp('atomNumber'))
            if atomProp('atomMolecule') is not None:
                self.updateProperty('atomMolecule', atomProp('atomMolecule'))
            if atomProp('atomCharge') is not None:
                self.updateProperty('atomCharge', atomProp('atomCharge'))
            if atomProp('atomType') is not None:
                self.updateProperty('atomType', atomProp('atomType'))
            if atomProp('atomVx') is not None:
                self.updateProperty('atomVx', atomProp('atomVx'))
            if atomProp('atomVy') is not None:
                self.updateProperty('atomVy', atomProp('atomVy'))
            if atomProp('atomVz') is not None:
                self.updateProperty('atomVz', atomProp('atomVz'))
            if atomProp('atomFlagOne') is not None:
                self.updateProperty('atomFlagOne', atomProp('atomFlagOne'))
            if atomProp('atomFlagTwo') is not None:
                self.updateProperty('atomFlagTwo', atomProp('atomFlagTwo'))
            if atomProp('atomFlagThree') is not None:
                self.updateProperty('atomFlagThree', atomProp('atomFlagThree'))
        else:
            print('ERROR, da.__init__():',
                  'this atom type is not supported')

        if atomNumber is not None:
            self.__setProperties['atomNumber'] = atomNumber
        if atomMolecule is not None:
            self.__setProperties['atomMolecule'] = atomMolecule
        if atomMass is not None:
            self.__setProperties['atomMass'] = atomMass
        if atomType is not None:
            self.__setProperties['atomType'] = atomType
        if atomCharge is not None:
            self.__setProperties['atomCharge'] = atomCharge
        if selectionState is not None:
            self.__setProperties['selectionState'] = atomState
        if atomVx is not None:
            self.__setProperties['atomVx'] = atomVx
        if atomVy is not None:
            self.__setProperties['atomVy'] = atomVy
        if atomVz is not None:
            self.__setProperties['atomVz'] = atomVz
        if atomFlagOne is not None:
            self.__setProperties['atomFlagOne'] = atomFlagOne
        if atomFlagOne is not None:
            self.__setProperties['atomFlagTwo'] = atomFlagTwo
        if atomFlagOne is not None:
            self.__setProperties['atomFlagThree'] = atomFlagThree
      ## Be careful here! I suppose, this might cause errors.
        if atomDrawnRadius is None:
            self.__setProperties['drawnRadius'] = 50
        else:
            self.__setProperties['drawnRadius'] = atomDrawnRadius
        if atomOffsetX is None:
            self.__setProperties['offsetX'] = 0
        else:
            self.__setProperties['offsetX'] = atomOffsetX
        if atomOffsetY is None:
            self.__setProperties['offsetY'] = 0
        else:
            self.__setProperties['offsetY'] = atomOffsetY
        if atomOffsetZ is None:
            self.__setProperties['offsetZ'] = 0
        else:
            self.__setProperties['offsetZ'] = atomOffsetZ
