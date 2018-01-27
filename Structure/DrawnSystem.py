#!/usr/bin/env python3
#coding=utf-8


from Base import Base
from Structure.DrawnAtom import DrawnAtom
from Structure.DrawnBond import DrawnBond
from Structure.AtomGeometrical import AtomGeometrical
from Structure.AtomLAMMPS import AtomLAMMPS
from Structure.AtomPhysical import AtomPhysical


# Constants...
ATOMIC_WIDGET_SIZE = 500
R = 5

class DrawnSystem(Base):
    def __init__(self,
                 boundaries=None,
                 drawnAtoms=None,
                 drawnBonds=None,
                 LAMMPSFullSystem=None):
        Base.__init__(self)
        self.__setProperties = dict()
        if (boundaries is None and
            drawnAtoms is None and
            drawnBonds is None and
            LAMMPSFullSystem is None):
            print('ERROR, ds.__init__():',
                  'impossible to create drawn system, to few arguments')
            return
        elif LAMMPSFullSystem is not None:
            boundaries = LAMMPSFullSystem.getProperty('boundaries')
            if boundaries is not None:
                self.updateProperty('boundaries', boundaries)
            atoms = LAMMPSFullSystem.getProperty('atoms')
            if atoms is not None:
                for atom in atoms:
                    drawnAtom = DrawnAtom(atomLAMMPSRealFull=atom)
                    self.addDrawnAtom(drawnAtom=drawnAtom)
            bonds = LAMMPSFullSystem.getProperty('bonds')
            for LAMMPSBond in bonds:
                drawnBond = DrawnBond(LAMMPSBond=LAMMPSBond)
                self.addDrawnBond(drawnBond=drawnBond)
        else:
            print('ERROR, ds.__init__():'
                  'cannot create DrawnSystem from this system')
            return
        self.updateProperty('className', 'DrawnSystem')
        self.updateProperty('drawAxesFlag', True)
        self.updateProperty('drawBoundariesFlag', True)
        self.updateProperty('drawAtomsFlag', True)
        self.updateProperty('drawBondsFlag', True)
        self.updateProperty('axes', 'XY')
        self.rescale()
        self.assignOffsets()

    def addDrawnAtom(self, drawnAtom):
        drawnAtoms = self.getProperty('drawnAtoms')
        if drawnAtoms is None:
            drawnAtoms = []
        drawnAtoms.append(drawnAtom)
        self.updateProperty('drawnAtoms', drawnAtoms)

    def addDrawnBond(self, drawnBond):
        drawnBonds = self.getProperty('drawnBonds')
        if drawnBonds is None:
            drawnBonds = []
        drawnBonds.append(drawnBond)
        self.updateProperty('drawnBonds', drawnBonds)

    def rescale(self):
        scale = 1
        drawnAtoms = self.getProperty('drawnAtoms')
        minx = drawnAtoms[0].getProperty('atomX')
        maxx = drawnAtoms[0].getProperty('atomX')
        miny = drawnAtoms[0].getProperty('atomY')
        maxy = drawnAtoms[0].getProperty('atomY')
        minz = drawnAtoms[0].getProperty('atomZ')
        maxz = drawnAtoms[0].getProperty('atomZ')
        for atom in drawnAtoms:
            x = atom.getProperty('atomX')
            y = atom.getProperty('atomY')
            z = atom.getProperty('atomZ')
            if x < minx:
                minx = x
            if x > maxx:
                maxx = x
            if y < miny:
                miny = y
            if y > maxy:
                maxy = y
            if z < minz:
                minz = z
            if z > maxz:
                maxz = z
        scaleX = ATOMIC_WIDGET_SIZE / (maxx - minx + R)
        scaleY = ATOMIC_WIDGET_SIZE / (maxy - miny + R)
        scaleZ = ATOMIC_WIDGET_SIZE / (maxz - minz + R)
        scale = min(scaleX, scaleY, scaleZ)
        self.updateProperty('scale', scale)

    def assignOffsets(self):
        offsetX = 0
        offsetY = 0
        offsetZ = 0
        drawnAtoms = self.getProperty('drawnAtoms')
        for atom in drawnAtoms:
            offsetX += atom.getProperty('atomX')
            offsetY += atom.getProperty('atomY')
            offsetZ += atom.getProperty('atomZ')
        offsetX /= len(drawnAtoms)
        offsetY /= len(drawnAtoms)
        offsetZ /= len(drawnAtoms)
        self.updateProperty('offsetX', -offsetX)
        self.updateProperty('offsetY', -offsetY)
        self.updateProperty('offsetZ', -offsetZ)
