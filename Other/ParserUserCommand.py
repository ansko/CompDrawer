#!/usr/bin/env python3
#coding=utf-8


# my imports
from Other.UserCommandsExecutor import UserCommandsExecutor


class ParserUserCommand:
    """
        It gets a string and returns the sequence of functions that
    should be called.
    """
    def __init__(self,
                 atomicWidget,
                 commandRaw='pass'):
        self.__functionCalls = []
        self.__functionArgs = []
        self.__atomicSystem = atomicWidget.atomicSystem()
        self.__uce = UserCommandsExecutor(self.__atomicSystem)
        command = commandRaw.split()
        print(command)
        if len(command) == 0:
            return
        commandName = command[0]
        if commandName == 'pass':
            return
        elif commandName == 'moveAtomsAlongX':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.__init__(),',
                      'command is moveAtomsAlongX, but the offset is not defined')
                return
            offsetAlongX = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongX)
            self.__functionArgs.append([offsetAlongX,])
        elif commandName == 'moveAtomsAlongY':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.__init__(),',
                      'command is moveAtomsAlongY, but the offset is not defined')
                return
            offsetAlongY = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongY)
            self.__functionArgs.append([offsetAlongY,])
        elif commandName == 'moveAtomsAlongZ':
            if len(command) < 2:
                print('ERROR: ParserUserCommand.__init__(),',
                      'command is moveAtomsAlongZ, but the offset is not defined')
                return
            offsetAlongZ = float(command[1])
            self.__functionCalls.append(self.__uce.moveAlongZ)
            self.__functionArgs.append([offsetAlongZ,])

    def functionCalls(self):
        return self.__functionCalls

    def functionArgs(self):
        return self.__functionArgs
