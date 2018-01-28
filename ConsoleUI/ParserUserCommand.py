#!/usr/bin/env python3
#coding=utf-8


# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from ConsoleUI.UserCommandsExecutor import UserCommandsExecutor
from Graphics.DrawingStyle import DrawingStyle

class ParserUserCommand:
    """
        It gets a string and returns the sequence of functions that
    should be called.
    """
    def __init__(self, atomicWidget, mainWidget):
        self.__uce = UserCommandsExecutor(atomicWidget, mainWidget)

    def parseCommand(self, commandRaw):
        self.__functionCalls = []
        self.__functionArgs = []
        command = commandRaw.split()
        if len(command) == 0:
            return
        commandName = command[0]
        if commandName == 'pass':
            return
    ##### General commands
        elif commandName == 'loadSystemFromFile':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is loadSystemFromFile',
                      'but the fname is not specified')
                return
            fname = command[1]
            self.__functionCalls.append(self.__uce.loadFromFile)
            self.__functionArgs.append([fname,])

        elif commandName in ['quite', 'exit']:
            self.__functionCalls.append(self.__uce.exit)
            self.__functionArgs.append(['normal termination',])
            sys.exit()
    ##### Commands to manipulate by the system geometry
        # and, consequently, by the picture, too.
        elif commandName == 'moveAtomsAlongX':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongX, but the offset is not defined')
                return
            offsetAlongX = float(command[1])
            self.__functionCalls.append(self.__uce.moveAtomsAlongX)
            self.__functionArgs.append([offsetAlongX,])
        elif commandName == 'moveAtomsAlongY':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongY, but the offset is not defined')
                return
            offsetAlongY = float(command[1])
            self.__functionCalls.append(self.__uce.moveAtomsAlongY)
            self.__functionArgs.append([offsetAlongY,])
        elif commandName == 'moveAtomsAlongZ':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongZ, but the offset is not defined')
                return
            offsetAlongZ = float(command[1])
            self.__functionCalls.append(self.__uce.moveAtomsAlongZ)
            self.__functionArgs.append([offsetAlongZ,])
        elif commandName == 'setAtomColor':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is setAtomColor, but the color is not defined')
                return
            color = QColor(command[1])
            self.__functionCalls.append(self.__uce.setAtomColor)
            self.__functionArgs.append([color,])
        elif commandName == 'setAtomRadius':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is setAtomRadius, but the radius is not defined')
                return
            radius = float(command[1])
            self.__functionCalls.append(self.__uce.setAtomRadius)
            self.__functionArgs.append([radius,])
        elif commandName == 'setBondColor':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is setBondColor, but the color is not defined')
                return
            color = QColor(command[1])
            self.__functionCalls.append(self.__uce.setBondColor)
            self.__functionArgs.append([color,])
   ##### Commands to manipulate just by the picture.
        elif commandName == 'setProjection':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is setProjection,'
                      'but the projection is not defined')
                return
            projection = command[1]
            self.__functionCalls.append(self.__uce.setProjection)
            self.__functionArgs.append([projection,])
        elif commandName == 'setDrawingStyle':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is setDrawingStyle,'
                      'but the style is not defined')
                return
            drawingStyle = command[1]
            self.__functionCalls.append(self.__uce.setDrawingStyle)
            self.__functionArgs.append([drawingStyle,])
        ## It is not supported now.
        elif commandName == 'removeTextStringName':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is removeTextStringName,'
                      'but the string name is not defined')
                return
            stringName = command[1]
            self.__functionCalls.append(self.__uce.removeTextStringName)
            self.__functionArgs.append([stringName,])
        elif commandName == 'addTextStringName':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is addTextStringName,'
                      'but the string name is not defined')
                return
            stringName = command[1]
            self.__functionCalls.append(self.__uce.addTextStringName)
            self.__functionArgs.append([stringName,])
        elif commandName == 'addAtomStringName':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is addAtomsStringName,'
                      'but the string name is not defined')
                return
            stringName = command[1]
            self.__functionCalls.append(self.__uce.addAtomStringName)
            self.__functionArgs.append([stringName,])
   ##### No such command
        else:
            print('ERROR: ParserUserCommand.parseCommand(),'
                  'unknown command:',
                   commandName)
            return
        if len(self.__functionCalls) != len(self.__functionArgs):
            print('ParserUserCommand.parseCommand():',
                  'lengths of commands and args for them differ.')
            return

    def functionCalls(self):
        return self.__functionCalls

    def functionArgs(self):
        return self.__functionArgs
