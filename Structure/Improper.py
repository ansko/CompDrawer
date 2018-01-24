#!/usr/bin/env python3
#coding=utf-8


class Improper:
    def __init__(self,
                 improperNumber,
                 improperType,
                 atomOne,
                 atomTwo,
                 atomThree,
                 atomFour):
        self.__improperNumber = improperNumber
        self.__improperType = improperType
        self.__atomOne = atomOne
        self.__atomTwo = atomTwo
        self.__atomThree = atomThree
        self.__atomFour = atomFour

    def improperNumber(self):
        return self.__improperNumber

    def improperType(self):
        return self.__improperType

    def improperAtomOne(self):
        return self.__atomOne

    def improperAtomTwo(self):
        return self.__atomTwo

    def improperAtomThree(self):
        return self.__atomThree

    def improperAtomFour(self):
        return self.__atomFour
