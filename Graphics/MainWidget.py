#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *

# my imports
from Base import Base
from ConsoleUI.ParserUserCommand import ParserUserCommand
from Graphics.AtomicWidget import AtomicWidget
from Graphics.ConsoleWidget import ConsoleWidget


class MainWidget(QWidget, Base):
    def __init__(self):
        QWidget.__init__(self)
        Base.__init__(self)
        self.__setProperties = dict()
        self.updateProperty('className', 'MainWidget')
        self.updateProperty('commandHistory', [])
        self.updateProperty('historyOffset', 0)
        self.__initUI()


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
        offset = self.getProperty('historyOffset')
        if -offset < len(self.__commandsHistory):
            self.setProperty('historyOffset', offset - 1)

    def decreaseHistoryOffset(self):
        offset = self.getProperty('historyOffset')
        if -offset > 0:
            self.setProperty('historyOffset', offset + 1)


    def __initUI(self):
        self.setFixedSize(500, 600)
        vbl = QVBoxLayout(self)
        self.__aw = AtomicWidget()
        self.__qle = ConsoleWidget()
        self.__qle.addParent(self)
        vbl.addWidget(self.__aw)
        vbl.addWidget(self.__qle)
        self.setLayout(vbl)


######### temporary code, start [2018-01-23/17:03]
    # Should be removed later, because it is dangerous.
    def executeTransmittedCommand(self, commandRaw):
        self.__qle.setText(commandRaw)
        self.executeCommand()
######### temporary code, end [2018-01-23/17:03]


    def executeCommand(self):
    # Maybe, it is bad that this method is not private?
        history = self.getProperty('commandHistiry')
        # If this is the first command during program run,
        # there is no history set.
        if history is None:
            history = []
        commandRaw = self.__qle.text()
        history.append(commandRaw)
        self.setProperty('commandsHistory', history)
        print('MainWidget.executeCommand(), executing:', commandRaw)
        puc = ParserUserCommand(self.__aw, self)
        puc.parseCommand(commandRaw=commandRaw)
        commands = puc.functionCalls()
        args = puc.functionArgs()
        self.__qle.setText('')
        for i, command in enumerate(commands):
            arg = args[i]
            command(*arg)
        self.update()
