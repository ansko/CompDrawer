#!/usr/bin/env python3
#coding=utf-8


# my imports
from Base import Base


class DrawnBond(Base):
    def __init__(self,
                 x1=None,
                 x2=None,
                 y1=None,
                 y2=None,
                 LAMMPSBond=None,
                 bondType=None,
                 bondPhysicalAtom1=None,
                 bondPhysicalAtom2=None,
                 bondDrawnAtom1=None,
                 bondDrawnAtom2=None):
        Base.__init__(self)
        self.__setProperties = dict()
        if LAMMPSBond is not None:
            bondProps = LAMMPSBond.getProperty
            self.updateProperty('LAMMPSAtomOne', bondProps('atomOne'))
            self.updateProperty('LAMMPSAtomTwo', bondProps('atomTwo'))
        else:
            print('ERROR, DrawnBond.__init__():',
                  'unsopportes bond type to convert into DrawnBond')
            return
