#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Widgets.AtomicWidget import AtomicWidget
from Other.ParserUserCommand import ParserUserCommand


class MainWidget(QWidget):
    """
        UI widget
    """
    def __init__(self):
        super().__init__()
        self.__initUI()

    def __initUI(self):
        self.setFixedSize(500, 600)
        self.__vbl = QVBoxLayout(self)
        self.__aw = AtomicWidget()
        self.__qle = QLineEdit()
        self.__qle.returnPressed.connect(self.executeCommand)
        self.__vbl.addWidget(self.__aw)
        self.__vbl.addWidget(self.__qle)
        self.setLayout(self.__vbl)

    def executeCommand(self):
        commandRaw = self.__qle.text()
        puc = ParserUserCommand(commandRaw=commandRaw,
                                atomicWidget=self.__aw)
        commands = puc.functionCalls()
        args = puc.functionArgs()
        self.__qle.setText('')
        for i, command in enumerate(commands):
            arg = args[i]
            command(*arg)
        self.update()
