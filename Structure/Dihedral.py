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

    def dihedralType(self):
        return self.__dihedralType

    def atomOne(self):
        return self.__atomOne

    def atomTwo(self):
        return self.__atomTwo

    def atomThree(self):
        return self.__atomThree

    def atomFour(self):
        return self.__atomFour
