#!/usr/bin/env python3
#coding=utf-8


class Base(object):
    def __init__(self):
        self.__setProperties = dict()
        self.__setProperties['className'] = 'Base'

    def updateProperty(self, propertyName, propertyValue):
        if propertyValue is None:
            print('WARNING, Base.updatePRoperty():',
                  'propertyValue is None',
                  'propertyName is', propertyName)
        self.__setProperties[propertyName] = propertyValue

    def getProperty(self, propertyName):
        if propertyName not in self.__setProperties.keys():
            return None
        return self.__setProperties[propertyName]

    def setPropertiesNames(self):
        return self.__setPropertiesKeys()

    def setProperties(self):
        return self.__setProperties

    def __str__(self):
        result = self.__setProperties['className'] + ' with set properties\n\t'
        for key, value in self.__setProperties.items():
            if key == 'className':
                continue
            result += str(key) + ": " + str(value) + "; "
        return result[:-2:]   # Returning the result 
                              # without the last "; ".
