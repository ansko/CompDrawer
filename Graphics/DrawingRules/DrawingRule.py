#!/usr/bin/env python3
#coding=utf-8


class DrawingRule:
    """
        Methods ifDrawAtom and ifDrawBons are used to decide
    whether draw atom/bond/text/boundaries or not. The way to draw it is defined in
    the DrawingStyle class. Maybe it is not the best idea.
    """
    def __init__(self,
                 generalRuleName=None,
                 atomRuleName=None,
                 bondRuleName=None,
                 textRuleName=None):
        #print('dr', generalRuleName)
        if generalRuleName in ['default', ]:
            self.__generalRuleName = 'default'
            self.__stringsToDraw = set()
            self.__atomsToDraw = set.update(('all',))
        else:
            self.__generalRuleName = generalRuleName
            self.__stringsToDraw = set()
            self.__atomsToDraw = set()

    def generalRuleName(self):
        return self.__generalRuleName

    def ifDrawAtom(self, atom):
        #print('DR', self.__generalRuleName, self.__atomsToDraw)
        if self.__generalRuleName in ['default', 'atomsOnly']:
            return True
        elif self.__generalRuleName in ['bondsOnly',]:
            return False
        elif self.__generalRuleName in ['custom',]:
            if 'all' in self.__atomsToDraw:
                return True
        return False

    def ifDrawBond(self, bond):
        if self.__generalRuleName in ['default', 'bondsOnly']:
            return True
        elif self.__generalRuleName in ['atomsOnly',]:
            return False
        return False

    def ifDrawText(self, stringName):
        if self.__generalRuleName in ['default', 'everything']:
            return True
        elif self.__generalRuleName in ['atomsOnly', 'bondsOnly']:
            return False
        else:
            if stringName in self.__stringsToDraw:
                return True
        return False

    def addAtomStringName(self, atomStringName):
        self.__atomsToDraw.update((atomStringName,))

    def removeAtomType(self, atomType):
        if atomType in self.__atomsToDraw:
            self.__atomsToDraw.remove(atomType)

    def addStringName(self, stringName):
        self.__stringsToDraw.update((stringName,))

    def removeStringName(self, stringName):
        if stringName in self.__stringsToDraw:
            self.__stringsToDraw.remove(stringName)

    def ifDrawBoundaries(self):
        if self.__generalRuleName in ['default',]:
            return True
        return False
