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
from Other.AtomicSystem import AtomicSystem
from Potentials.Potential import Potential
from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from Widgets.AtomicWidget import AtomicWidget
from Widgets.MainWidget import MainWidget


def main():
    """
        Simple test, draws atomic system from file "DataExamples/10x20.data".
    """
    app = QApplication(sys.argv)
    w = MainWidget()
    w.show()
    sys.exit(app.exec_())

#cProfile.run('main()')
main()
