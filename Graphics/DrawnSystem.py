class DrawnSystem:
    def __init__(self,
                 boundaries,
                 drawnAtoms,
                 drawnBonds):
        self.__boundaries = boundaries
        self.__drawnAtoms = drawnAtoms
        self.__drawnBonds = drawnBonds
      # Default system contains atoms, bonds and boundaries,
      # but does not draw them.
      # It must be done a lot to set the system in the proper state/
        self.__setProperties = dict() # some properties that one can specify
        self.__setProperties['drawAxesFlag'] = True#False
        self.__setProperties['drawBoundariesFlag'] = True#False
        self.__setProperties['drawAtomsFlag'] = True#False
        self.__setProperties['drawBondsFlag'] = True#False
        self.__setProperties['axes'] = 'XY'

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
        self.__setProperties['offsetX'] = -x
        self.__setProperties['offsetY'] = -y
        self.__setProperties['offsetZ'] = -z

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
        lx = xmax - xmin
        ly = ymax - ymin
        lz = zmax - zmin
        if min(lx, ly, lz) < 0:
            import sys
            print('ERROR in ds:',
                  'incorrect box lengths')
            sys.exit()
        lmax = max(lx, ly, lz)
        self.__setProperties['scale'] = 500 / lmax
        self.__setProperties['scalePolicy'] = 'united'
