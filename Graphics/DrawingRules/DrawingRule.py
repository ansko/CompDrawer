#!/usr/bin/env python3
#coding=utf-8


class DrawingRule:
    def __init__(self, ruleName=None):
        if ruleName is None:
            self.__flag = True

    def ifDraw(self, atom):
        return self.__flag
