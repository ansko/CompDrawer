#!/usr/bin/env python3
#coding=utf-8


class Dihedral:
    def __init__(self,
                 dihedralNumber,
                 dihedralType,
                 atomOne,
                 atomTwo,
                 atomThree,
                 atomFour):
        self.__dihedralNumber = dihedralNumber
        self.__dihedralType = dihedralType
        self.__atomOne = atomOne
        self.__atomTwo = atomTwo
        self.__atomThree = atomThree
        self.__atomFour = atomFour

    def dihedralNumber(self):
        return self.__dihedralNumber

    def setDihedralNumber(self, dihedralNumber):
        self.__dihedralNumber = dihedralNumber

    def dihedralType(self):
        return self.__dihedralType

    def dihedralAtomOne(self):
        return self.__atomOne

    def dihedralAtomTwo(self):
        return self.__atomTwo

    def dihedralAtomThree(self):
        return self.__atomThree

    def dihedralAtomFour(self):
        return self.__atomFour
