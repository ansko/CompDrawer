#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConsoleWidget(QLineEdit):
    def __init__(self):
        super().__init__()

    def addParent(self, parent):
        self.__parent = parent

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.__parent.executeCommand()
        elif event.key() == Qt.Key_Backspace:
            if self.text() == '':
                return
            self.setText(self.text()[0:-1])
        elif event.key() == Qt.Key_Up:
            commandsHistory = self.__parent.commandsHistory()
            self.__parent.increaseHistoryOffset()
            self.setText(commandsHistory[-1])
        elif event.key() == Qt.Key_Down:
            commandsHistory = self.__parent.commandsHistory()
            self.__parent.decreaseHistoryOffset()
            self.setText(commandsHistory[-1])
        elif Qt.ControlModifier == event.modifiers() and event.key() == Qt.Key_V:
            mimeData = qApp.clipboard().mimeData()
            if mimeData.hasText():
                self.setText(mimeData.text())
        else:
            self.setText(self.text() + event.text())
            self.update()
