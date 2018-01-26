#!/usr/bin/env python3
#coding=utf-8


from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from Structure.Atoms.AtomGeometrical import AtomGeometrical


class DrawnAtom:
    """
        This class is made to store atoms that will be drawn later.
        There are many characeristics in this class, not all of them have
    physical meaning
    """
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
        self.__setProperties = dict() # all properties that are already set
                                      # are stored here
        """self.__allProperties = ['atomNumber',
                                'atomLAMMPSRealFull',
                                'atomGeometrical',
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
        """
        if atomLAMMPSRealFull is not None:
            alrf = atomLAMMPSRealFull
            #print('da.__init__() alrf', alrf.atomX())
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
        elif atomGeometrical is not None:
            ag = atomGeometrical
            print('da.__init__()', ag.atomX())
            self.__setProperties['atomX'] = ag.atomX()
            self.__setProperties['atomY'] = ag.atomY()
            self.__setProperties['atomZ'] = ag.atomZ()
        elif atomPhysical is not None:
            ap = atomPhysical
            self.__setProperties['atomX'] = ap.atomX()
            #print('da.__init__()', ap.atomX())
            self.__setProperties['atomY'] = ap.atomY()
            self.__setProperties['atomZ'] = ap.atomZ()
            self.__setProperties['atomCharge'] = ap.atomCharge()
            self.__setProperties['atomMass'] = ap.atomMass()
            self.__setProperties['atomBonds'] = ap.atomBonds()
            self.__setProperties['atomAngles'] = ap.atomAngles()
            self.__setProperties['atomDihedrals'] = ap.atomDihedrals()
            self.__setProperties['atomImpropers'] = ap.atomImpropers()
        else:
            print('ERROR, da.__init__():',
                  'this atom type is not supported')

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
       # careful!
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
