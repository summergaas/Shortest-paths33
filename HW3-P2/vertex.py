class vertex():
    def __init__( self, data, neighbors=[], distance=float("inf"), parent=None, matrixPos = None, seen = False):
        self.data = data
        self.neighbors = neighbors
        self.distance = distance
        self.parent = parent
        self.matrixPos = matrixPos
        self.seen = seen
   
    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_neighbors(self):
        return self.neighbors

    def set_neighbors(self, new_neighbors):
        self.neighbors = new_neighbors

    def get_distance(self):
        return self.distance

    def set_distance(self, new_distance):
        self.distance = new_distance

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent

    def get_matrixPos(self):
        return self.matrixPos

    def set_matrixPos(self, new_matrixPos):
        self.matrixPos = new_matrixPos

    def get_seen(self):
        return self.seen

    def set_seen(self, new_seen):
        self.seen = new_seen

   