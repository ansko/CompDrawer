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
from Graphics.Widgets.MainWidget import MainWidget
from Graphics.DrawnAtom import DrawnAtom
from Graphics.DrawnBond import DrawnBond
from Graphics.DrawnSystem import DrawnSystem

def main():
    """
        Simple test, draws atomic system from file "DataExamples/10x20.data".
    """
    app = QApplication(sys.argv)
    rld = ReaderLAMMPSData(fname='datafile.data', atomicStyle='full')
    physicalAtoms = rld.parsedAtoms()
    physicalBonds = rld.parsedBonds()
    ds = DrawnSystem(drawnAtoms=[], drawnBonds=[], boundaries=[])
    ds.setAxesPenColor(axesPenColorPolicy='united',
                       axesPenColor=QColor('green'))
    ds.setAtomBrushColor(atomBrushColorPolicy='united',
                         atomBrushColor=QColor('red'))
    ds.setBondPenColor(bondPenColorPolicy='united',
                       bondPenColor=QColor('blue'))
    for atom in physicalAtoms:
        da = DrawnAtom(atomLAMMPSRealFull=atom)
        # proper flag should be done for this
        da.updatePropertyValue('drawnRadius', 5)
        ds.addDrawnAtom(da)
    for bond in physicalBonds:
        db = DrawnBond(physicalBond=bond)
        ds.addDrawnBond(db)
    ds.updateProperty('scale', 15)
    w = MainWidget()
    w.setDrawnSystem(ds)
    w.show()
    sys.exit(app.exec_())

#cProfile.run('main()')
main()
