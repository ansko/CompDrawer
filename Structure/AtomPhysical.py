#!/usr/bin/env python3
#coding=utf-8


from Structure.AtomGeometrical import AtomGeometrical


class AtomPhysical(AtomGeometrical):
    def __init__(self,
                 x=None,
                 y=None,
                 z=None,
                 atomCharge=None,
                 atomMass=None,
                # atomMolecule=None, # it may be optional, I think
                 pairCoeffs=None,
                # maybe, it should be specified in proper classes?..
                 #bondCoeffs=None,
                 #angleCoeffs=None,
                 #dihedralCoeffs=None,
                 #improperCoeffs=None,
                 atomBonds=None,
                 atomAngles=None,
                 atomDihedrals=None,
                 atomImpropers=None):
        self.__typeName = 'AtomPhysical'
        self.__x = x
        self.__y = y
        self.__z = z
        self.__atomCharge = atomCharge
        self.__atomMass = atomMass
        self.__atomMolecule = atomMolecule
        self.__pairCoeffs = pairCoeffs,
        self.__atomBonds = atomBonds,
        self.__atomAngles = atomAngles
        self.__atomDihedrals = atomDihedrals
        self.__atomImpropers = atomImpropers
        if atomCharge is None or atomMass is None:
            print('ERROR, ap.__init__():',
                  'atom is too unphysical,'
                  'maybe it chould be AtomGeometrical instead?')
            return

        def atomTypeName(self):
            return self.__typeName

        def x(self):
            return self.__x

        def y(self):
            return self.__y

        def z(self):
            return self.__z

        def atomCharge(self):
            return self.__atomCharge

        def atomMass(self):
            return self.__atomMass

        def atomMolecule(self):
            return self.__atomMolecule

        def pairCoeffs(self):
            return self.__pairCoeffs

        def atomBonds(self):
            if self.__atomBonds is None:
                return []
            return self.__atomBonds

        def atomAngles(self):
            if self.__atomAngles is None:
                return []
            return self.__atomAngles

        def atomDihedrals(self):
            if self.__atomDihedrals is None:
                return []
            return self.__atomDihedrals

        def atomImpropers(self):
            if self.__atomImpropers is None:
                return []
            return self.__atomImpropers
