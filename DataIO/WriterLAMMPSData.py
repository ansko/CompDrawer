#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import datetime
import sys

# my imports
from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from Structure.Bond import Bond
from Structure.Angle import Angle
from Structure.Dihedral import Dihedral
from Structure.Improper import Improper


"""
    - Types of bonds, angles, etc. are hardcoded!
"""


class WriterLAMMPSData:
    def __init__(self, physicalAtomicSystem, atomicStyle, fname=None):
        self.__avaliableAtomicStyles = ['full', ]
        if atomicStyle not in self.__avaliableAtomicStyles:
            print('ERROR:',
                  'WriterLAMMPSData: this atomic style is not avaliable now!',
                  'Yor style is', atomicStyle,
                  'while avaliable styles are', self.__avaliableAtomicStyles)
            sys.exit()
        self.__physicalAtomicSystem = physicalAtomicSystem
        self.__fname = fname
        self.__atomicStyle = atomicStyle
        self.__parserAttributes = dict()

    def writeLAMMPSData(self):
        if self.__atomicStyle == 'full':
            self.__writeLAMMPSDataFull()

    def addParserAttributes(self, parserLAMMPSDataSomeStyle):
        if self.__atomicStyle == 'full':
            self.__addParserFullAttributes(parserLAMMPSDataSomeStyle)

    def parserAttributes(self):
        return self.__parserAttributes

####'full' atomic style, start
    def __addParserFullAttributes(self, parserLAMMPSDataFull):
        pldf = parserLAMMPSDataFull
        attrs = dict()
        attrs['atomTypesNumber'] = pldf.parsedAtomTypesNumber()
        attrs['bondTypesNumber'] = pldf.parsedBondTypesNumber()
        attrs['angleTypesNumber'] = pldf.parsedAngleTypesNumber()
        attrs['dihedralTypesNumber'] = pldf.parsedDihedralTypesNumber()
        attrs['improperTypesNumber'] = pldf.parsedImproperTypesNumber()
        attrs['pairCoeffs'] = pldf.parsedPairCoeffs()
        attrs['bondCoeffs'] = pldf.parsedBondCoeffs()
        attrs['angleCoeffs'] = pldf.parsedAngleCoeffs()
        attrs['dihedralCoeffs'] = pldf.parsedDihedralCoeffs()
        attrs['improperCoeffs'] = pldf.parsedImproperCoeffs()
        self.__parserAttributes = attrs

    def __writeLAMMPSDataFull(self):
        atSys = self.__physicalAtomicSystem
        if self.__fname == None:
            f = sys.stdout
        else:
            f = open(self.__fname, 'w')
        now = datetime.datetime.now()
        comment = ('LAMMPS data file. ' +
                   'CompDrawer / ' +
                   str(now.day) + ' ' + str(now.month) + ' ' + str(now.year) + ' /'
                   ' UNDEFINED_STRING') # This is not important for me now,
                                        # but it should be done in a proper
                                        # way later!
      ### Start string
        f.write(comment)
        f.write('\n\n')
      ### Number of atoms, etc.
        # is it possible for LAMMPS datafile indent here to be not equal to 7?..
        f.write(' ' * (7 - len(str(len(atSys.atoms())))))
        f.write(str(len(atSys.atoms())))
        f.write(' atoms\n')
        f.write(' ' * (7 - len(str(len(atSys.bonds())))))
        f.write(str(len(atSys.bonds())))
        f.write(' bonds\n')
        f.write(' ' * (7 - len(str(len(atSys.angles())))))
        f.write(str(len(atSys.angles())))
        f.write(' angles\n')
        f.write(' ' * (7 - len(str(len(atSys.dihedrals())))))
        f.write(str(len(atSys.dihedrals())))
        f.write(' dihedrals\n')
        f.write(' ' * (7 - len(str(len(atSys.impropers())))))
        f.write(str(len(atSys.impropers())))
        f.write(' impropers\n')
        f.write('\n')
      ### Number of atom types, etc.
        # is it possible for LAMMPS datafile indent here to be not equal to 4?..
        for key in ['atom', 'bond', 'angle', 'dihedral', 'improper']:
            keytn = key + 'TypesNumber'
            if self.__parserAttributes[keytn] == 0:
                continue
            f.write(' ' * (4 - len(str(self.__parserAttributes[keytn]))))
            f.write(str(self.__parserAttributes[keytn]))
            f.write(' ' + key + ' types\n')
        f.write('\n')
      ### Boundaries
        f.write('\t' + str(atSys.ranges()[0]) + '\t' + str(atSys.ranges()[1]))
        f.write(' xlo xhi\n')
        f.write('\t' + str(atSys.ranges()[2]) + '\t' + str(atSys.ranges()[3]))
        f.write(' ylo yhi\n')
        f.write('\t' + str(atSys.ranges()[4]) + '\t' + str(atSys.ranges()[5]))
        f.write(' zlo zhi\n')
        f.write('\n')
      ### Masses
        f.write('Masses\n\n')
        for i in range(len(atSys.masses())):
            f.write(' ' * (4 - len(str(i))) +
                    str(i + 1) +
                    ' ' * (4 - len(str(int(atSys.masses()[i])))) +
                    str(atSys.masses()[i]) + '\n')
        f.write('\n')
      ### Pair Coeffs # lj/cut/coul/long - maybe comment is optional?..
        array = ['Pair', 'Bond', 'Angle', 'Dihedral', 'Improper']
        for i, key in enumerate(array):
            keylc = key.lower() + 'Coeffs'
            if self.__parserAttributes[keylc] == 0:
                continue
            if i == 0:
                f.write(key + ' Coeffs # lj/cut/coul/long\n\n')
            elif i == len(array) - 1:
                f.write(key + ' Coeffs # cvff\n\n')
            else:
                f.write(key + ' Coeffs # harmonic\n\n')
            for coeffNumber, coeff in enumerate(self.__parserAttributes[keylc]):
                f.write(str(coeffNumber + 1) + ' ')
                for j in range(len(coeff)):
                    if coeff[j].is_integer():
                        coeff[j] = int(coeff[j])                    
                    f.write(str(coeff[j]))
                    if j != len(coeff) - 1:
                        f.write(' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys.atoms()) > 0:
            f.write('Atoms # full\n\n')
            for atom in atSys.atoms():
                f.write(str(atom.atomNumber()) + ' ')
                f.write(str(atom.moleculeNumber()) + ' ')
                f.write(str(atom.atomType()) + ' ')
                f.write(str(atom.atomCharge()) + ' ')
                f.write(str(atom.atomX()) + ' ')
                f.write(str(atom.atomY()) + ' ')
                f.write(str(atom.atomZ()) + ' ')
                f.write(str(atom.atomFlagOne()) + ' ')
                f.write(str(atom.atomFlagTwo()) + ' ')
                f.write(str(atom.atomFlagThree()) + ' ')
                f.write(str(atom.atomComment()))
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys.bonds()) > 0:
            f.write('Bonds\n\n')
            for bond in atSys.bonds():
                f.write(str(bond.bondNumber()) + ' ')
                f.write(str(bond.bondType()) + ' ')
                f.write(str(bond.bondAtomOne().atomNumber()) + ' ')
                f.write(str(bond.bondAtomTwo().atomNumber()) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys.angles()) > 0:
            f.write('Angles\n\n')
            for angle in atSys.angles():
                f.write(str(angle.angleNumber()) + ' ')
                f.write(str(angle.angleType()) + ' ')
                f.write(str(angle.angleAtomOne().atomNumber()) + ' ')
                f.write(str(angle.angleAtomTwo().atomNumber()) + ' ')
                f.write(str(angle.angleAtomThree().atomNumber()) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys.dihedrals()) > 0:
            f.write('Dihedrals\n\n')
            for dihedral in atSys.dihedrals():
                f.write(str(dihedral.dihedralNumber()) + ' ')
                f.write(str(dihedral.dihedralType()) + ' ')
                f.write(str(dihedral.dihedralAtomOne().atomNumber()) + ' ')
                f.write(str(dihedral.dihedralAtomTwo().atomNumber()) + ' ')
                f.write(str(dihedral.dihedralAtomThree().atomNumber()) + ' ')
                f.write(str(dihedral.dihedralAtomFour().atomNumber()) + ' ')
                f.write('\n')
            f.write('\n')
      ###
        if len(atSys.impropers()) > 0:
            f.write('Impropers\n\n')
            for improper in atSys.impropers():
                f.write(str(improper.improperNumber()) + ' ')
                f.write(str(improper.improperType()) + ' ')
                f.write(str(improper.improperAtomOne().atomNumber()) + ' ')
                f.write(str(improper.improperAtomTwo().atomNumber()) + ' ')
                f.write(str(improper.improperAtomThree().atomNumber()) + ' ')
                f.write(str(improper.improperAtomFour().atomNumber()) + ' ')
                f.write('\n')
      ###
####'full' atomic style, end
