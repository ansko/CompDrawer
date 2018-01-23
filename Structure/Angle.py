#!/usr/bin/env python3
#coding=utf-8


class Angle:
    def __init__(self,
                 angleNumber,
                 angleType,
                 atomOne,
                 atomTwo, # middle atom
                 atomThree):
        self.__angleNumber = angleNumber
        self.__angleType = angleType
        self.__atomOne = atomOne
        self.__atomTwo = atomTwo
        self.__atomThree = atomThree

    def angleNumber(self):
        return self.__angleNumber

    def angleType(self):
        return self.__angleType

    def atomOne(self):
        return self.__atomOne

    def atomTwo(self):
        return self.__atomTwo

    def atomThree(self):
        return self.__atomThree
