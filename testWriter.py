#!/usr/bin/env python3
#coding=utf-8


# profiling imports
import cProfile
import time

# standart modules imports
import sys

# my imports
from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem
from Other.ParserLAMMPSData import ParserLAMMPSData
from Other.WriterLAMMPSData import WriterLAMMPSData


def main():
    """
        Simple test of my class WriterLAMMPSData".
    """
    ifname = 'DataExamples/PA6_monomer.data'
    ofname = 'datafile.data'
#    ofname = None
    atomicStyle='full'
    pld = ParserLAMMPSData(fname=ifname, atomicStyle=atomicStyle)
    physicalAtomicSystem = PhysicalAtomicSystem(method='manual',
                                                fname=ifname,
                                                atomicStyle=atomicStyle,
                                                potential=None,
                                                masses=pld.parsedMasses(),
                                                atoms=pld.parsedAtoms(),
                                                bonds=pld.parsedBonds(),
                                                angles=pld.parsedAngles(),
                                                dihedrals=pld.parsedDihedrals(),
                                                impropers=pld.parsedImpropers(),
                                                ranges=pld.parsedRanges())
    wld = WriterLAMMPSData(physicalAtomicSystem=physicalAtomicSystem,
                           fname=ofname,
                           atomicStyle=atomicStyle)
    wld.addParserAttributes(pld)
    wld.writeLAMMPSData()


main()
