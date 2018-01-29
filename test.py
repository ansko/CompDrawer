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
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData
from Graphics.MainWidget import MainWidget
from Graphics.AtomicWidget import AtomicWidget
from Structure.AtomLAMMPS import AtomLAMMPS
from Structure.LAMMPSFullSystem import LAMMPSFullSystem


def main():
    """
        Simple test, draws atomic system from file "DataExamples/10x20.data".
    """
    app = QApplication(sys.argv)
    w = MainWidget()

    # Now there is some commands sequence,
    # that is hardcoded into MainWidget;
    # its purpose is to test some functionality
    # without writing long string
    # into program's concole by hands.
    w.executeTransmittedCommand('loadSystemFromFile ' +
                                'DataExamples/PA6_monomer.data')
    #                            'datafile.data')
    w.executeTransmittedCommand('setProjection XZ')
    w.executeTransmittedCommand('moveAtomsAlongX 0')
    w.executeTransmittedCommand('moveAtomsAlongY 0')
    w.executeTransmittedCommand('moveAtomsAlongZ 0')
    w.executeTransmittedCommand('setDrawingStyle custom')
    w.executeTransmittedCommand('setAtomColor red')
    w.executeTransmittedCommand('setAtomRadius 10')
    w.executeTransmittedCommand('setBondColor green')
    w.executeTransmittedCommand('select atoms id 1, 2, 3')

    w.show()
    sys.exit(app.exec_())

#cProfile.run('main()')
main()
