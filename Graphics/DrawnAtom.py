#!/usr/bin/env python3
#coding=utf-8


from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull


class DrawnAtom:
    """
        This class is made to store atoms that will be drawn later.
        There are many characeristics in this class, not all of them have
    physical meaning
    """
    def __init__(self,
                 atomLAMMPSRealFull=None,
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
                 selectionState=None, # atomState = active/passive 
                                      # (is it selected or not)
                 paintingVisibility=None):
        self.__setProperties = dict() # all properties that are already set
                                      # are stored here
        self.__allProperties = ['atomNumber',
                                'atomX',
                                'atomY',
                                'atomZ',
                                'atomMolecule',
                                'atomMass',
                                'atomType',
                                'atomCharge',
                                'selectionState',
                                'atomVx',
                                'atomVy',
                                'atomVz',
                                'atomFlagOne',
                                'atomFlagTwo',
                                'atomFlagThree',
                                'paintingVisibility']
        if atomLAMMPSRealFull is not None:
            alrf = atomLAMMPSRealFull
            self.__setProperties['atomX'] = alrf.atomX()
            self.__setProperties['atomY'] = alrf.atomY()
            self.__setProperties['atomZ'] = alrf.atomZ()
            self.__setProperties['atomNumber'] = alrf.atomNumber()
            self.__setProperties['atomMolecule'] = alrf.moleculeNumber()
            self.__setProperties['atomType'] = alrf.atomType()
            self.__setProperties['atomCharge'] = alrf.atomCharge
            self.__setProperties['atomVx'] = alrf.atomVx()
            self.__setProperties['atomVy'] = alrf.atomVy()
            self.__setProperties['atomVz'] = alrf.atomVz()
            self.__setProperties['atomFlagOne'] = alrf.atomFlagOne
            self.__setProperties['atomFlagTwo'] = alrf.atomFlagTwo
            self.__setProperties['atomFlagThree'] = alrf.atomFlagThree

        if atomX is not None:
            self.__setProperties['atomX'] = atomX
        if atomY is not None:
            self.__setProperties['atomY'] = atomY
        if atomZ is not None:
            self.__setProperties['atomZ'] = atomZ
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

    def setProperties(self):
        return self.__setProperties

    def updatePropertyValue(self, propertyName, propertyValue):
        self.__setProperties[propertyName] = propertyValue

    def getPropertyValue(self, propertyName):
        if propertyName in self.__setProperties.keys():
            return self.__setProperties[propertyName]

    def removeProperty(self, propertyName):
        if propertyName in self.__setProperties.keys():
            self.__setProperties.remove(propertyName)
