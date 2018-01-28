#!/usr/bin/env python3
#coding=utf-8


# my imports
from Base import Base
from Structure.AtomLAMMPS import AtomLAMMPS
from DataIO.ReaderLAMMPSData import ReaderLAMMPSData


class LAMMPSFullSystem(Base):
    def __init__(self,
                 method=None,
                 fname=None,
                 atomicStyle=None,
                 potential=None,
                 masses=None,
                 atoms=None,
                 velocities=None,
                 bonds=None,
                 angles=None,
                 dihedrals=None,
                 impropers=None,
                 boundaries=None):
        Base.__init__(self)
        self.__setProperties = dict()
        if method is None:
            print('ERROR, PhysicalSystem.__init__():',
                  'method of system creation is not specified',
                  '(it is None).')
            return
        elif method == "from file":
            if fname is None:
                print('ERROR, PhysicalSystem.__init__():',
                      'atomic system should be read from file, but',
                      'the fname parameter is not specified.',
                      '(it is None).')
                return
            if atomicStyle is None:
                print('ERROR, PhysicalSystem.__init__():',
                      'atomic system should be read from file, but',
                      'the atomicStyle parameter is not specified.',
                      '(it is None).')
                return
            self.initFromFile(fname, atomicStyle)
        elif method == 'manual':
            if None in [atoms, bonds]:
                print('ERROR, PhysicalSystem.__init__():',
                      'atoms is ', atoms,
                      'bonds is ', bonds,
                      'both of them should be not None.')
                return
        if potential is not None:
            self.updateProperty('potential', potential)
        if masses is not None:
            self.updateProperty('masses', masses)
        if atoms is not None:
            self.updateProperty('atoms', atoms)
        if bonds is not None:
            self.updateProperty('bonds', bonds)
        if angles is not None:
            self.updateProperty('angles', angles)
        if dihedrals is not None:
            self.updateProperty('dihedrals', dihedrals)
        if impropers is not None:
            self.updateProperty('impropers', impropers)
        if boundaries is not None:
            self.updateProperty('boundaries', boundaries)
        if velocities is not None:
            self.updateProperty('velocities', velocities)

    def initFromFile(self, fname, atomicStyle):
        """
            Now it is suitable just for 'full' LAMMPS atom types.
        """
        print("... AtomicSystem: reading system from file ", fname)
        reader = ReaderLAMMPSData(fname, atomicStyle)
        if reader.parsedPotential() is not None:
            self.updateProperty('potential', reader.parsedPotential())
        self.updateProperty('atoms', reader.parsedAtoms())
        if reader.parsedBonds() is not None:
            self.updateProperty('bonds', reader.parsedBonds())
        if reader.parsedAngles() is not None:
            self.updateProperty('angles', reader.parsedAngles())
        if reader.parsedDihedrals() is not None:
            self.updateProperty('dihedrals', reader.parsedDihedrals())
        if reader.parsedImpropers() is not None:
            self.updateProperty('impropers', reader.parsedImpropers())
        print("... AtomicSystem: system has been read")
