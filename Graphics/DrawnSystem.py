#!/usr/bin/env python3
#coding=utf-8


from Graphics.DrawnAtom import DrawnAtom
from Graphics.DrawnBond import DrawnBond
from Structure.Atoms.AtomGeometrical import AtomGeometrical
from Structure.Atoms.AtomLAMMPSRealFull import AtomLAMMPSRealFull
from Structure.Atoms.AtomPhysical import AtomPhysical


class DrawnSystem:
    def __init__(self,
                 boundaries=None,
                 drawnAtoms=None,
                 drawnBonds=None,
                 physicalSystem=None):
      # Default system does not contain atoms, bonds and boundaries,
      # and consequently does not draw them.
      # It must be done a lot to set the system into the proper state.
        self.__setProperties = dict() # some properties that one can specify
        self.__setProperties['drawAxesFlag'] = True#False
        self.__setProperties['drawBoundariesFlag'] = True#False
        self.__setProperties['drawAtomsFlag'] = True#False
        self.__setProperties['drawBondsFlag'] = True#False
        self.__setProperties['axes'] = 'XY'
        self.__setProperties['offsetX'] = 0
        self.__setProperties['offsetY'] = 0
        self.__setProperties['offsetZ'] = 0
        if (boundaries is None and
            drawnAtoms is None and
            drawnBonds is None and
            physicalSystem is None):
            print('ERROR, ds.__init__():',
                  'impossible to create drawn system, to few arguments')
            return
        elif (boundaries is not None and
              drawnAtoms is not None and
              drawnBonds is not None):
            self.__boundaries = boundaries
            self.__drawnAtoms = drawnAtoms
            self.__drawnBonds = drawnBonds
        elif physicalSystem is not None:
            self.__boundaries = physicalSystem.boundaries()
            self.__drawnAtoms = []
            for atom in physicalSystem.atoms():
               # physical system may have atoms of different type
               # (AtomLAMMPSRealFull, AtomPhysical, ...)
                if atom.atomTypeName() == 'AtomPhysical':
                    #atom = AtomPhysical(atom)
                    drawnAtom = DrawnAtom(atomPhysical=atom)
                elif atom.atomTypeName() == 'AtomLAMMPSRealFull':
                    #print('ds.init alrf', atom.atomX())
                    #atom = AtomLAMMPSRealFull(atom)
                    drawnAtom = DrawnAtom(atomLAMMPSRealFull=atom)
                else:
                    print('ERROR, ds.__init__():',
                          'atom in physical system is of unsopported type:',
                          atom.atomTypeName())
                self.addDrawnAtom(newDrawnAtom=drawnAtom)
            self.__drawnBonds = []
            for physicalBond in physicalSystem.bonds():
                drawnBond = DrawnBond(physicalBond=physicalBond)
                self.addDrawnBond(newDrawnBond=DrawnBond(physicalBond=physicalBond))
        else:
            print('ERROR, ds.__init__():'
                  'cannot create DrawnSystem')
            return

    def updateProperty(self, propertyName, propertyValue):
        self.__setProperties[propertyName] = propertyValue

    def removeProperty(self, propertyName):
        if propertyName in self.__setProperties.keys():
            self.__setProperties.remove(propertyName)

    def scale(self):
        if 'scale' in self.__setProperties.keys():
            return self.__setProperties['scale']
        return 1

    def getPropertyValue(self, propertyName):
        if propertyName in self.__setProperties.keys():
            return self.__setProperties[propertyName]
        return None

    def boundaries(self):
        return self.__boundaries

    def drawnAtoms(self):
        return self.__drawnAtoms

    def drawnBonds(self):
        return self.__drawnBonds

    def addDrawnAtom(self, newDrawnAtom):
        self.__drawnAtoms.append(newDrawnAtom)
      # The system should be translated to fit AtomicWidget
        x = 0
        y = 0
        z = 0
        if len(self.__drawnAtoms) != 0:
            for atom in self.__drawnAtoms:
                dx = atom.getPropertyValue('atomX')
                if dx is None:
                    dx = 0
                dy = atom.getPropertyValue('atomY')
                if dy is None:
                   dy = 0
                dz = atom.getPropertyValue('atomZ')
                if dz is None:
                   dz = 0
                x += dx
                y += dy
                z += dz
            x /= len(self.__drawnAtoms)
            y /= len(self.__drawnAtoms)
            z /= len(self.__drawnAtoms)
        self.__setOffsetX(-x)
        self.__setOffsetY(-y)
        self.__setOffsetZ(-z)

    def __setOffsetX(self, offsetX):
        for atom in self.__drawnAtoms:
            atom.updatePropertyValue(propertyName='offsetX', propertyValue=offsetX)

    def __setOffsetY(self, offsetY):
        for atom in self.__drawnAtoms:
            atom.updatePropertyValue(propertyName='offsetY', propertyValue=offsetY)

    def __setOffsetZ(self, offsetZ):
        for atom in self.__drawnAtoms:
            atom.updatePropertyValue(propertyName='offsetZ', propertyValue=offsetZ)

    def addDrawnBond(self, newDrawnBond):
       # Maybe, there should be a checking if atoms that make the bond exist
       # in the system
        self.__drawnBonds.append(newDrawnBond)

    def setAxesPenColor(self,
                          axesPenColorPolicy,
                          axesPenColor=None):
        if axesPenColorPolicy == 'united':
            self.__setProperties['axesPenColorPolicy'] = 'united'
            if axesPenColor is None:
                axesPenColor = Qt.black
            self.__setProperties['axesPenColorUnited'] = axesPenColor

    def setAtomBrushColor(self,
                          atomBrushColorPolicy,
                          atomBrushColor=None):
        if atomBrushColorPolicy == 'united':
            self.__setProperties['atomBrushColorPolicy'] = 'united'
            if atomBrushColor is None:
                atomBrushColor = Qt.black
            self.__setProperties['atomBrushColorUnited'] = atomBrushColor

    def setBondPenColor(self,
                          bondPenColorPolicy,
                          bondPenColor=None):
        if bondPenColorPolicy == 'united':
            self.__setProperties['bondPenColorPolicy'] = 'united'
            if bondPenColor is None:
                bondPenColor = Qt.black
            self.__setProperties['bondPenColorUnited'] = bondPenColor

    def calculateScale(self):
        lx = 0
        ly = 0
        lz = 0
        if len(self.__drawnAtoms) != 0:
            xmin = self.__drawnAtoms[0].getPropertyValue('atomX')
            xmax = self.__drawnAtoms[0].getPropertyValue('atomX')
            ymin = self.__drawnAtoms[0].getPropertyValue('atomY')
            ymax = self.__drawnAtoms[0].getPropertyValue('atomY')
            zmin = self.__drawnAtoms[0].getPropertyValue('atomZ')
            zmax = self.__drawnAtoms[0].getPropertyValue('atomZ')
            for atom in self.__drawnAtoms:
                dx = atom.getPropertyValue('atomX')
                if dx > xmax:
                    xmax = dx
                if dx < xmin:
                    xmin = dx
                dy = atom.getPropertyValue('atomY')
                if dy > ymax:
                    ymax = dy
                if dx < xmin:
                    ymin = dy
                dz = atom.getPropertyValue('atomZ')
                if dz > zmax:
                    zmax = dz
                if dz < zmin:
                    zmin = dz
                #print('ds.cs', dx, dy, dz)
        else:
            print('ERROR, ds.calculataScale():',
                  'len(self.__drawnAtoms) == 0',
                  'maybe drawn system is not set')
            import sys
            sys.exit()
        #print(xmax, xmin, ymax, ymin, zmax, zmin)
        #print('ds.calculateScale', self.__drawnAtoms[0].getPropertyValue('atomX'))
        lx = xmax - xmin
        ly = ymax - ymin
        lz = zmax - zmin
        if min(lx, ly, lz) < 0:
            import sys
            print('ERROR in ds:',
                  'incorrect box lengths')
            sys.exit()
        lmax = max(lx, ly, lz)
        if lmax == 0:
            print('ERROR, ds.__calculateScale():',
                  'lmax is zero',
                  'maybe drawn system is not set')
            return
        self.__setProperties['scale'] = 500 / lmax
        self.__setProperties['scalePolicy'] = 'united'
