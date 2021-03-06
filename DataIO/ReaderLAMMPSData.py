#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# my imports
from Structure.AtomLAMMPS import AtomLAMMPS
from Structure.BondLAMMPS import BondLAMMPS
from Structure.Angle import Angle
from Structure.Dihedral import Dihedral
from Structure.Improper import Improper


class ReaderLAMMPSData:
    """
        Parses LAMMPS's ".data" file.
    """
    def __init__(self, fname, atomicStyle):
        self.__avaliableAtomicStyles = ['full', ]
        if atomicStyle not in self.__avaliableAtomicStyles:
            print('ERROR:',
                  'ParserLAMMPSData: this atomic style is not avaliable now!',
                  'Yor style is', atomicStyle,
                  'while avaliable styles are', self.__avaliableAtomicStyles)
            sys.exit()
        self.__fname = fname
        if atomicStyle == 'full':
            self.__readDataFull()

    def __readDataFull(self):
        flagAtomsBegan = False
        flagVelocitiesBegan = False
        flagBondsBegan = False
        flagAnglesBegan = False
        flagDihedralsBegan = False
        flagImpropersBegan = False
        flagMassesBegan = False
        flagPotentialBegan = False
        flagPairCoeffsBegan = False
        flagBondCoeffsBegan = False
        flagAngleCoeffsBegan = False
        flagDihedralCoeffsBegan = False
        flagImproperCoeffsBegan = False
        potential = None
        atoms = []
        atomsNumber = 0
        atomTypesNumber = 0
        bonds = []
        bondsNumber = 0
        bondTypesNumber = 0
        angles = []
        anglesNumber = 0
        angleTypesNumber = 0
        dihedrals = []
        dihedralsNumber = 0
        dihedralTypesNumber = 0
        impropers = []
        impropersNumber = 0
        improperTypesNumber = 0
        comment = None
        zRangesLineNumber = None
        xlo = None
        xhi = None
        ylo = None
        yhi = None
        zlo = None
        zhi = None
        inclines = True
        masses = []
        pairCoeffs = []
        bondCoeffs = []
        angleCoeffs = []
        dihedralCoeffs = []
        improperCoeffs = []
        with open(self.__fname, 'r') as f:
            print('ParserLAMMPSData: started reading from file ', self.__fname)
            for lineNumber, line in enumerate(f):
                if lineNumber == 0:
                    comment = line
                elif line.endswith(' atoms\n'):
                    atomsNumber = int(line.split()[0])
                    atoms = [None for i in range(atomsNumber)]
                elif line.endswith(' bonds\n'):
                    bondsNumber = int(line.split()[0])
                    bonds = [None for i in range(bondsNumber)]
                elif line.endswith(' angles\n'):
                    anglesNumber = int(line.split()[0])
                    angles = [None for i in range(anglesNumber)]
                elif line.endswith(' dihedrals\n'):
                    dihedralsNumber = int(line.split()[0])
                    dihedrals = [None for i in range(dihedralsNumber)]
                elif line.endswith(' impropers\n'):
                    impropersNumber = int(line.split()[0])
                    impropers = [None for i in range(impropersNumber)]
                elif line.endswith('atom types\n'):
                    atomTypesNumber = int(line.split()[0])
                elif line.endswith('bond types\n'):
                    bondTypesNumber = int(line.split()[0])
                elif line.endswith('angle types\n'):
                    angleTypesNumber = int(line.split()[0])
                elif line.endswith('dihedral types\n'):
                    dihedralTypesNumber = int(line.split()[0])
                elif line.endswith('improper types\n'):
                    improperTypesNumber = int(line.split()[0])
                elif line.endswith('xlo xhi\n'):
                    xlo = float(line.split()[0])
                    xhi = float(line.split()[1])
                elif line.endswith('ylo yhi\n'):
                    ylo = float(line.split()[0])
                    yhi = float(line.split()[1])
                elif line.endswith('zlo zhi\n'):
                    zlo = float(line.split()[0])
                    zhi = float(line.split()[1])
                    zRangesLineNumber = lineNumber
                elif (zRangesLineNumber is not None and # String with inclines, 
                      lineNumber == zRangesLineNumber): # it may be absent.
                    if len(line.split()) == 0:
                        continue
                    if line.split()[0] != '0':
                        continue
                    inclines = False
                elif line.startswith('Masses'):
                     flagMassesBegan = True
                elif line.startswith('Pair Coeffs'):
                     flagPotentialBegan = True
                     flagPairCoeffsBegan = True
                elif line.startswith('Bond Coeffs'):
                     flagBondCoeffsBegan = True
                elif line.startswith('Angle Coeffs'):
                     flagAngleCoeffsBegan = True
                elif line.startswith('Dihedral Coeffs'):
                     flagDihedralCoeffsBegan = True
                elif line.startswith('Improper Coeffs'):
                     flagImproperCoeffsBegan = True
                elif line.startswith('Atoms'):
                     flagAtomsBegan = True
                elif line.startswith('Velocities'):
                     flagVelocitiesBegan = True
                elif line.startswith('Bonds'):
                     flagBondsBegan = True
                     flagVelocitiesBegan = True # this is not good
                                                # they really did not begin
                elif line.startswith('Angles'):
                     flagAnglesBegan = True
                elif line.startswith('Dihedrals'):
                     flagDihedralsBegan = True
                elif line.startswith('Impropers'):
                     flagImpropersBegan = True
                elif flagMassesBegan and not flagPotentialBegan: # Reading masses
                      if len(line.split()) == 0:
                          continue
                      masses.append(float(line.split()[1]))
                elif flagPotentialBegan and not flagAtomsBegan:
                      if len(line.split()) == 0:
                          continue
                      if flagPairCoeffsBegan and not flagBondCoeffsBegan:
                          pairCoeffs.append([float(line.split()[1]),
                                             float(line.split()[2])])
                      elif flagBondCoeffsBegan and not flagAngleCoeffsBegan:
                          bondCoeffs.append([float(line.split()[1]),
                                             float(line.split()[2])])
                      elif flagAngleCoeffsBegan and not flagDihedralCoeffsBegan:
                          angleCoeffs.append([float(line.split()[1]),
                                              float(line.split()[2])])
                      elif flagDihedralCoeffsBegan and not flagImproperCoeffsBegan:
                          dihedralCoeffs.append([float(line.split()[1]),
                                                 float(line.split()[2]),
                                                 float(line.split()[3])])
                      elif flagImproperCoeffsBegan:
                          improperCoeffs.append([float(line.split()[1]),
                                                 float(line.split()[2]),
                                                 float(line.split()[3])])
                elif flagAtomsBegan and not flagVelocitiesBegan:
                       ls = line.split()
                       if len(ls) < 10:
                           continue
                       atomNumber = int(ls[0])
                       moleculeNumber = int(ls[1])
                       atomType = int(ls[2])
                       atomCharge = float(ls[3])
                       atomX = float(ls[4])
                       atomY = float(ls[5])
                       atomZ = float(ls[6])
                       atomFlagOne = int(ls[7])
                       atomFlagTwo = int(ls[8])
                       atomFlagThree = int(ls[9])
                       if len(ls) > 10:
                           if len(ls) == 11:
                               comment = ls[10]
                           else:
                               comment = " ".join(*ls[10:-1:1])
                       else:
                           comment = None
                       atoms[atomNumber - 1] = AtomLAMMPS(
                                                   atomNumber,
                                                   atomX,
                                                   atomY,
                                                   atomZ,
                                                   moleculeNumber=moleculeNumber,
                                                   atomType=atomType,
                                                   atomCharge=atomCharge,
                                                   atomFlagOne=atomFlagOne,
                                                   atomFlagTwo=atomFlagTwo,
                                                   atomFlagThree=atomFlagThree,
                                                   atomComment=comment
                                               )
                elif flagVelocitiesBegan and not flagBondsBegan:
                    ls = line.split()
                    if len(ls) < 4:
                        continue
                    atomNumber = int(ls[0]) # Index = number - 1, because
                                            # indices start from 0, 
                                            # while numbers - from 1.
                    atomVx = float(ls[1])
                    atomVy = float(ls[2])
                    atomVz = float(ls[3])
                    atoms[atomNumber - 1].setAtomVx(atomVx=atomVx)
                    atoms[atomNumber - 1].setAtomVy(atomVy=atomVy)
                    atoms[atomNumber - 1].setAtomVz(atomVz=atomVz)
                elif flagBondsBegan and not flagAnglesBegan:
                    ls = line.split()
                    if len(ls) < 4:
                        continue
                    bondNumber = int(ls[0])
                    bondType = int(ls[1])
                    atomOneNumber = int(ls[2])
                    atomTwoNumber = int(ls[3])
                    atomOne = atoms[atomOneNumber - 1]
                    atomTwo = atoms[atomTwoNumber - 1]
                    neighbors = atomOne.getProperty('neighbors')
                    if neighbors is None:
                        neighbors = []
                    neighbors.append(atomTwo)
                    atomOne.updateProperty('neighbors', neighbors)
                    neighbors = atomTwo.getProperty('neighbors')
                    if neighbors is None:
                        neighbors = []
                    neighbors.append(atomOne)
                    atomTwo.updateProperty('neighbors', neighbors)
                    bonds[bondNumber - 1] = BondLAMMPS(bondNumber,
                                                       bondType,
                                                       atomOne,
                                                       atomTwo)
                    bonds[bondNumber - 1].setBoxBoundaries([xlo, xhi,
                                                            ylo, yhi,
                                                            zlo, zhi])
                elif flagAnglesBegan and not flagDihedralsBegan:
                    ls = line.split()
                    if len(ls) < 5:
                        continue
                    angleNumber = int(ls[0])
                    angleType = int(ls[1])
                    atomOneNumber = int(ls[2])
                    atomTwoNumber = int(ls[3])
                    atomThreeNumber = int(ls[4])
                    atomOne = atoms[atomOneNumber - 1]
                    atomTwo = atoms[atomTwoNumber - 1]
                    atomThree = atoms[atomThreeNumber - 1]
                    angles[angleNumber - 1] = Angle(angleNumber=angleNumber,
                                                    angleType=angleType,
                                                    atomOne = atomOne,
                                                    atomTwo = atomTwo,
                                                    atomThree = atomThree)
                elif flagDihedralsBegan and not flagImpropersBegan:
                    ls = line.split()
                    if len(ls) < 6:
                        continue
                    dihedralNumber = int(ls[0])
                    dihedralType = int(ls[1])
                    atomOneNumber = int(ls[2])
                    atomTwoNumber = int(ls[3])
                    atomThreeNumber = int(ls[4])
                    atomFourNumber = int(ls[5])
                    atomOne = atoms[atomOneNumber - 1]
                    atomTwo = atoms[atomTwoNumber - 1]
                    atomThree = atoms[atomThreeNumber - 1]
                    atomFour = atoms[atomFourNumber - 1]
                    dihedrals[dihedralNumber - 1] = Dihedral(
                                                     dihedralNumber=dihedralNumber,
                                                     dihedralType=dihedralType,
                                                     atomOne=atomOne,
                                                     atomTwo=atomTwo,
                                                     atomThree=atomThree,
                                                     atomFour=atomFour)
                elif flagImpropersBegan:
                    ls = line.split()
                    if len(ls) < 6:
                        continue
                    improperNumber = int(ls[0])
                    improperType = int(ls[1])
                    atomOneNumber = int(ls[2])
                    atomTwoNumber = int(ls[3])
                    atomThreeNumber = int(ls[4])
                    atomFoutNumber = int(ls[5])
                    atomOne = atoms[atomOneNumber - 1]
                    atomTwo = atoms[atomTwoNumber - 1]
                    atomThree = atoms[atomThreeNumber - 1]
                    atomFour = atoms[atomFourNumber - 1]
                    impropers[improperNumber - 1] = Improper(
                                                     improperNumber=improperNumber,
                                                     improperType=improperType,
                                                     atomOne=atomOne,
                                                     atomTwo=atomTwo,
                                                     atomThree=atomThree,
                                                     atomFour=atomFour)
                else:
                    if len(line.split()) == 0:
                        continue
                    print('This string does not seem to contain data:', line)
        self.__parsedComment = comment
        self.__parsedPotential = potential
        self.__parsedAtoms = atoms
        self.__parsedBonds = bonds
        self.__parsedAngles = angles
        self.__parsedDihedrals = dihedrals
        self.__parsedImpropers = impropers
        self.__parsedAtomTypesNumber = atomTypesNumber
        self.__parsedBondTypesNumber = bondTypesNumber
        self.__parsedAngleTypesNumber = angleTypesNumber
        self.__parsedDihedralTypesNumber = dihedralTypesNumber
        self.__parsedImproperTypesNumber = improperTypesNumber
        self.__parsedBoundaries = [xlo, xhi, ylo, yhi, zlo, zhi]
        self.__parsedMasses = masses
        self.__parsedInclines = inclines
        self.__parsedPairCoeffs = pairCoeffs
        self.__parsedBondCoeffs = bondCoeffs
        self.__parsedAngleCoeffs = angleCoeffs
        self.__parsedDihedralCoeffs = dihedralCoeffs
        self.__parsedImproperCoeffs = improperCoeffs
        print('ParserLAMMPSData finished reading')

    def fname(self):
        return self.__fname

    def parsedBoundaries(self):
        return self.__parsedBoundaries

    def parsedPotential(self):
        return self.__parsedPotential

    def parsedAtoms(self):
        return self.__parsedAtoms

    def parsedBonds(self):
        return self.__parsedBonds

    def parsedAngles(self):
        return self.__parsedAngles

    def parsedDihedrals(self):
        return self.__parsedDihedrals

    def parsedImpropers(self):
        return self.__parsedImpropers

    def parsedAtomTypesNumber(self):
        return self.__parsedAtomTypesNumber

    def parsedBondTypesNumber(self):
        return self.__parsedBondTypesNumber

    def parsedAngleTypesNumber(self):
        return self.__parsedAngleTypesNumber

    def parsedDihedralTypesNumber(self):
        return self.__parsedDihedralTypesNumber

    def parsedImproperTypesNumber(self):
        return self.__parsedImproperTypesNumber

    def parsedComment(self):
        return self.__parsedComment

    def parsedMasses(self):
        return self.__parsedMasses

    def parsefInclines(self):
        return self.__parsedInclines

    def parsedPairCoeffs(self):
        return self.__parsedPairCoeffs

    def parsedBondCoeffs(self):
        return self.__parsedBondCoeffs

    def parsedAngleCoeffs(self):
        return self.__parsedAngleCoeffs

    def parsedDihedralCoeffs(self):
        return self.__parsedDihedralCoeffs

    def parsedImproperCoeffs(self):
        return self.__parsedImproperCoeffs
