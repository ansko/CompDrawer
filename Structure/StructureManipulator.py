#!/usr/bin/env python3
#coding=utf-8


from AtomicSystem.PhysicalAtomicSystem import PhysicalAtomicSystem


class StructureManipulator:
    def __init__(self):
        self.__physicalAtomicSystem = None

    def setPhysicalAtomicSystem(self, structure):
        self.__physicalAtomicSystem = structure

    def removePhysicalAtomicSystem(self):
        self.__physicalAtomicSystem = None

    def physicalAtomicSystem(self):
        return self.__physicalAtomicSystem

    def removeAtom(self,
                   method,
                   *args):
        if self.__physicalAtomicSystem is None:
            print('ERROR: sm, physicalAtomicSystem is not set')
            return
        if method == 'numbers':
            if len(args) < 1:
                print('ERROR: sm, not enough args for method ids')
            atomNumbersToRemove = args[0]
            masses = self.__physicalAtomicSystem.masses()
            ranges = self.__physicalAtomicSystem.ranges()
            atoms = self.__physicalAtomicSystem.atoms()
            bonds = self.__physicalAtomicSystem.bonds()
            angles = self.__physicalAtomicSystem.angles()
            dihedrals = self.__physicalAtomicSystem.dihedrals()
            impropers = self.__physicalAtomicSystem.impropers()
            bondNumbersToRemove = []
            angleNumbersToRemove = []
            dihedralNumbersToRemove = []
            improperNumbersToRemove = []
            # finding bonds, angles etc. that should be removed
            for bond in bonds:
                 if (bond.bondAtomOne().atomNumber() in atomNumbersToRemove or
                     bond.bondAtomTwo().atomNumber() in atomNumbersToRemove):
                     bondNumbersToRemove.append(bond.bondNumber())
            for angle in angles:
                 if (angle.angleAtomOne().atomNumber() in atomNumbersToRemove or
                     angle.angleAtomTwo().atomNumber() in atomNumbersToRemove or
                     angle.angleAtomThree().atomNumber in atomNumbersToRemove):
                     angleNumbersToRemove.append(angle.angleNumber())
            for dihedral in dihedrals:
                 if dihedral.dihedralAtomOne().atomNumber() in atomNumbersToRemove:
                     dihedralNumbersToRemove.append(dihedral.dihedralNumber())
                 if dihedral.dihedralAtomTwo().atomNumber() in atomNumbersToRemove:
                     dihedralNumbersToRemove.append(dihedral.dihedralNumber())
                 if dihedral.dihedralAtomThree().atomNumber() in atomNumbersToRemove:
                     dihedralNumbersToRemove.append(dihedral.dihedralNumber())
                 if dihedral.dihedralAtomFour().atomNumber() in atomNumbersToRemove:
                     dihedralNumbersToRemove.append(dihedral.dihedralNumber())
            for improper in impropers:
                 if improper.improperAtomOne().atomNumber() in atomNumbersToRemove:
                     improperNumbersToRemove.append(improper.improperNumber())
                 if improper.improperAtomTwo().atomNumber() in atomNumbersToRemove:
                     improperNumbersToRemove.append(improper.improperNumber())
                 if improper.improperAtomThree().atomNumber() in atomNumbersToRemove:
                     improperNumbersToRemove.append(improper.improperNumber())
                 if improper.improperAtomFour().atomNumber() in atomNumbersToRemove:
                     improperNumbersToRemove.append(improper.improperNumber())
            # removing everything that should be removed
            atomNumbersToRemove.sort()
            bondNumbersToRemove.sort()
            angleNumbersToRemove.sort()
            dihedralNumbersToRemove.sort()
            improperNumbersToRemove.sort()
            for atomNumber in atomNumbersToRemove[::-1]:
                atoms.pop(atomNumber - 1)
            for bondNumber in bondNumbersToRemove[::-1]:
                bonds.pop(bondNumber - 1)
            for angleNumber in angleNumbersToRemove[::-1]:
                angles.pop(angleNumber - 1)
            for dihedralNumber in dihedralNumbersToRemove[::-1]:
                dihedrals.pop(dihedralNumber - 1)
            for improperNumber in improperNumbersToRemove[::-1]:
                impropers.pop(improperNumber - 1)
            # now we should make proper numeration of atoms, bonds etc.
            for atomNumber in range(len(atoms)):
                atoms[atomNumber].setAtomNumber(atomNumber + 1)
            for bondNumber in range(len(bonds)):
                bonds[bondNumber].setBondNumber(bondNumber + 1)
            for angleNumber in range(len(angles)):
                angles[angleNumber].setAngleNumber(angleNumber + 1)
            for dihedralNumber in range(len(dihedrals)):
                dihedrals[dihedralNumber].setDihedralNumber(dihedralNumber + 1)
            for improperNumber in range(len(impropers)):
                impropers[improperNumber].setImproperNumber(improperNumber + 1)
            # writing data
            self.__physicalAtomicSystem = PhysicalAtomicSystem(method='manual',
                                                fname=None,
                                                atomicStyle='full',
                                                potential=None,
                                                masses=masses,
                                                atoms=atoms,
                                                bonds=bonds,
                                                angles=angles,
                                                dihedrals=dihedrals,
                                                impropers=impropers,
                                                ranges=ranges)
