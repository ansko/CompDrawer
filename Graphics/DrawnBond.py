#!/usr/bin/env python3
#coding=utf-8


from Structure.Bond import Bond


class DrawnBond:
    def __init__(self,
                 x1=None,
                 x2=None,
                 y1=None,
                 y2=None,
                 physicalBond=None,
                 bondType=None,
                 bondPhysicalAtom1=None,
                 bondPhysicalAtom2=None,
                 bondDrawnAtom1=None,
                 bondDrawnAtom2=None):
        self.__setProperties = dict()
        if physicalBond is not None:
            self.__setProperties['physicalAtomOne'] = physicalBond.bondAtomOne()
            self.__setProperties['physicalAtomTwo'] = physicalBond.bondAtomTwo()

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
