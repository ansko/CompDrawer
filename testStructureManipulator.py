#!/usr/bin/env python3
#coding=utf-8


# profiling imports
import cProfile
import time

# standart modules imports
import sys

# my imports
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData
from DataIO.WriterLAMMPSData import WriterLAMMPSData
from Structure.StructureManipulator import StructureManipulator
from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem


def main():
    """
        Simple test of my class StructureManipulator.
    """
    ifname = 'DataExamples/PA6_monomer.data'
    ofname = 'datafile.data'
    atomicStyle='full'
    # reading data
    rld = ReaderLAMMPSData(fname=ifname, atomicStyle=atomicStyle)
    physicalAtomicSystem = PhysicalAtomicSystem(method='manual',
                                                fname=ifname,
                                                atomicStyle=atomicStyle,
                                                potential=None,
                                                masses=rld.parsedMasses(),
                                                atoms=rld.parsedAtoms(),
                                                bonds=rld.parsedBonds(),
                                                angles=rld.parsedAngles(),
                                                dihedrals=rld.parsedDihedrals(),
                                                impropers=rld.parsedImpropers(),
                                                ranges=rld.parsedRanges())
    # manipulating data
    sm = StructureManipulator()
    sm.setPhysicalAtomicSystem(physicalAtomicSystem)
    sm.removeAtom('numbers', [1,])
    # writing data
    physicalAtomicSystem = sm.physicalAtomicSystem()
    wld = WriterLAMMPSData(physicalAtomicSystem=physicalAtomicSystem,
                           fname=ofname,
                           atomicStyle=atomicStyle)
    wld.addParserAttributes(rld)
    wld.writeLAMMPSData()

main()
