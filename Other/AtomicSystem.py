#!/usr/bin/env python3
#coding=utf-8


# my imports
from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from Other.ParserLAMMPSData import ParserLAMMPSData

class AtomicSystem:
    """
         Would store the information about atoms and potential to describe them and
    system ranges (xlo, xhi, ...).
         It is done for the AtomicWidget class.
    """
    def __init__(self,
                 method=None,
                 fname='DataExamples/10x20.data',
                 atomicType='full',
                 potential=None,
                 atoms=[AtomLAMMPSRealFull(), ]):
        if not method:
            self.__potential = potential
            self.__atoms = atoms
        elif method == "from file":
            if fname is None:
                print("ERROR: atomic system should be read from file, but",
                      "the filename is not defined.")
                sys.exit()
            self.initFromFile(fname, atomicType)

    def initFromFile(self, fname, atomicType):
        print("... AtomicSystem: reading system from file ", fname)
        """
            Draft implementation, start. [2018-01-22/16:58]
        """
        parser = ParserLAMMPSData(fname, atomicType)
        self.__potential = parser.parsedPotential()
        self.__atoms = parser.parsedAtoms()
        """
            Draft implementation, end. [2018-01-22/16:58]
        """
        print("... AtomicSystem: system has been read")

    def potential(self):
        return self.__potential

    def atoms(self):
        return self.__atoms
