#!/usr/bin/env python3
#coding=utf-8


class AtomGeometrical:
    """
        Describes 'geometrical' atom - it has only coordinates
    """
    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__typeName = 'AtomGeometrical'

    def typeName(self):
        return self.__typeName

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def z(self):
        return self.__z

    def move(self, dx, dy, dz):
        self.__x += dx
        self.__y += dy
        self.__z += dz
