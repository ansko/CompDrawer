#!/usr/bin/env python3
#coding=utf-8


# my imports
from Other.UserCommandsExecutor import UserCommandsExecutor


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
        elif commandName == 'loadSystemFromFile':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is loadSystemFromFile',
                      'but the fname is not specified')
                return
            fname = command[1]
            self.__functionCalls.append(self.__uce.loadFromFile)
            self.__functionArgs.append([fname,])
        elif commandName == 'moveAtomsAlongX':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongX, but the offset is not defined')
                return
            offsetAlongX = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongX)
            self.__functionArgs.append([offsetAlongX,])
        elif commandName == 'moveAtomsAlongY':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongY, but the offset is not defined')
                return
            offsetAlongY = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongY)
            self.__functionArgs.append([offsetAlongY,])
        elif commandName == 'moveAtomsAlongZ':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),',
                      'command is moveAtomsAlongZ, but the offset is not defined')
                return
            offsetAlongZ = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongZ)
            self.__functionArgs.append([offsetAlongZ,])
        elif commandName == 'setProjection':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.parseCommand(),'
                      'command is setProjection,'
                      'but the projection is not defined')
                return
            projection = command[1]
            self.__functionCalls.append(self.__uce.setProjection)
            self.__functionArgs.append([projection,])
        else:
            print('ERROR: ParserUserCommand.parseCommand(),'
                  'unknown command')
            return
        if len(self.__functionCalls) != len(self.__functionArgs):
            print('ParserUserCommand.parseCommand():',
                  'lengths of commands and args for them differ')
            return

    def functionCalls(self):
        return self.__functionCalls

    def functionArgs(self):
        return self.__functionArgs
