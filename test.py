#!/usr/bin/env python3
#coding=utf-8


"""
This tool maybe would help me to create initial structures of composite OMMT - PA6.
"""


# profiling imports
import cProfile
import time

# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# my imports
from Graphics.Widgets.MainWidget import MainWidget


def main():
    """
        Simple test, draws atomic system from file "DataExamples/10x20.data".
    """
    app = QApplication(sys.argv)
    w = MainWidget()

    # now there is some commands sequence, that is hardcoded into MainWidget
    # its purpose is to test some functionality without writing long string
    # into program's concole
    # w.setFname(fname="DataExamples/10x20.data")
    # w.setFname(fname="DataExamples/MT2EtOH_cvff.data")
    # w.setFname(fname="DataExamples/PA6_monomer.data")

    ### tmp code, made to simulate input of some commands, start [2018-01-26/11:35]
    w.executeTransmittedCommand('loadSystemFromFile ' +
                               # 'DataExamples/PA6_monomer.data')
                                'datafile.data')
    w.executeTransmittedCommand('setProjection XZ')
    #w.executeTransmittedCommand('moveAtomsAlongX 0')
    #w.executeTransmittedCommand('moveAtomsAlongY 0')
    #w.executeTransmittedCommand('moveAtomsAlongZ 0')
    #w.executeTransmittedCommand('setDrawingStyle custom')
    #w.executeTransmittedCommand('setDrawingRule custom')
    #w.executeTransmittedCommand('addTextStringName scale')
    #w.executeTransmittedCommand('removeTextStringName scale')
    #w.executeTransmittedCommand('addTextStringName drawingStyleName')
    #w.executeTransmittedCommand('addAtomStringName all')
    ### tmp code, made to simulate input of some commands, end [2018-01-26/11:35]

    w.show()
    sys.exit(app.exec_())

#cProfile.run('main()')
main()
