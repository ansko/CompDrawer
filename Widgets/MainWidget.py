#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Widgets.AtomicWidget import AtomicWidget
from Widgets.ConsoleWidget import ConsoleWidget
from Other.ParserUserCommand import ParserUserCommand


class MainWidget(QWidget):
    """
        UI widget
    """
    def __init__(self):
        super().__init__()
        self.__commandsHistory = []
        self.__historyOffset = 0
        self.__initUI()

    def setFname(self, fname):
        self.__fname = fname

    def commandsHistory(self):
        if self.__historyOffset == 0:
            result = self.__commandsHistory
        else:
            result = self.__commandsHistory[0:self.__historyOffset:]
        if len(result) == 0:
            result = self.__commandsHistory
            self.__historyOffset = 0
        return result

    def increaseHistoryOffset(self):
        if -self.__historyOffset < len(self.__commandsHistory):
            self.__historyOffset -= 1

    def decreaseHistoryOffset(self):
        if -self.__historyOffset > 0:
            self.__historyOffset += 1

    def __initUI(self):
        self.setFixedSize(500, 600)
        self.__vbl = QVBoxLayout(self)
        self.__aw = AtomicWidget(drawingStyle='primitive')
        self.__qle = ConsoleWidget()
        self.__qle.addParent(self)
        self.__vbl.addWidget(self.__aw)
        self.__vbl.addWidget(self.__qle)
        self.setLayout(self.__vbl)

######### temporary code, start [2018-01-23/17:03]
        self.__qle.setText('loadSystemFromFile DataExamples/PA6_monomer.data')
        self.executeCommand()
        self.__qle.setText('setProjection XZ')
        self.executeCommand()
        self.__qle.setText('moveAtomsAlongX 0')
        self.executeCommand()
        self.__qle.setText('moveAtomsAlongY 0')
        self.executeCommand()
        self.__qle.setText('moveAtomsAlongZ 0')
        self.executeCommand()
######### temporary code, end [2018-01-23/17:03]

    def executeCommand(self): # maybe, it is bad that this method is not private?
        commandRaw = self.__qle.text()
        self.__commandsHistory.append(commandRaw)
        print('executing', commandRaw)
        puc = ParserUserCommand(self.__aw, self)
        puc.parseCommand(commandRaw=commandRaw)
        commands = puc.functionCalls()
        args = puc.functionArgs()
        self.__qle.setText('')
        for i, command in enumerate(commands):
            arg = args[i]
            print('ARG:', arg)
            command(*arg)
        self.update()
