#!/usr/bin/env python3
#coding=utf-8


# my imports
from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData

class PhysicalSystem:
    """
         Would store the information about atoms and potential to describe them and
    system ranges (xlo, xhi, ...).
         It is done for the AtomicWidget class.
    """
    def __init__(self,
                 method=None,
                 fname='DataExamples/10x20.data',
                 atomicStyle='full',
                 potential=None,
                 masses=[],
                 atoms=[AtomLAMMPSRealFull(), ],
                 velocities=[],
                 bonds=[],
                 angles=[],
                 dihedrals=[],
                 impropers=[],
                 boundaries=None):
        if not method or method == 'manual':
            if not method:
                print('PhysicalSystem.__init__()',
                      'method of system creation is not specified',
                      'using default values')
            else:
                pass
                #print('PhysicalSystem.__init__()',
                #      'method of system creation is "manual"')
            self.__potential = potential
            self.__masses = masses
            self.__atoms = atoms
            self.__bonds = bonds
            self.__angles = angles
            self.__dihedrals = dihedrals
            self.__impropers = impropers
            self.__boundaries = boundaries
            self.__velocities = velocities
        elif method == "from file":
            if fname is None:
                print("ERROR: atomic system should be read from file, but",
                      "the filename is not defined.")
                sys.exit()
            self.initFromFile(fname, atomicStyle)

    def initFromFile(self, fname, atomicStyle):
        print("... AtomicSystem: reading system from file ", fname)
        """
            Draft implementation, start. [2018-01-22/16:58]
        """
        parser = ParserLAMMPSData(fname, atomicType)
        self.__potential = parser.parsedPotential()
        self.__atoms = parser.parsedAtoms()
        self.__bonds = parser.parsedBonds()
        self.__angles = parser.parsedAngles()
        self.__dihedrals = parser.parsedDihedrals()
        self.__impropers = parser.parsedImpropers()
        """
            Draft implementation, end. [2018-01-22/16:58]
        """
        print("... AtomicSystem: system has been read")

    def potential(self):
        return self.__potential

    def masses(self):
        return self.__masses

    def velocities(self):
        return self.__velocities

    def atoms(self):
        return self.__atoms

    def bonds(self):
        return self.__bonds

    def angles(self):
        return self.__angles

    def dihedrals(self):
        return self.__dihedrals

    def impropers(self):
        return self.__impropers

    def boundaries(self):
        return self.__boundaries
