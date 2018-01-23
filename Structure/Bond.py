#!/usr/bin/env python3
#coding=utf-8


class Bond:
    def __init__(self,
                 bondNumber,
                 bondType,
                 atomOne,
                 atomTwo):
        self.__bondNumber = bondNumber
        self.__bondType = bondType
        self.__atomOne = atomOne
        self.__atomTwo = atomTwo
        self.__xlo = None
        self.__xhi = None
        self.__ylo = None
        self.__yhi = None
        self.__zlo = None
        self.__zhi = None

    def setBoxRanges(self, ranges):
        self.__xlo = ranges[0]
        self.__xhi = ranges[1]
        self.__ylo = ranges[2]
        self.__yhi = ranges[3]
        self.__zlo = ranges[4]
        self.__zhi = ranges[5]

    def bondNumber(self):
        return self.__bondNumber

    def bondType(self):
        return self.__bondType

    def atomOne(self):
        return self.__atomOne

    def atomTwo(self):
        return self.__atomTwo
