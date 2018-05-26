class matrix():
    def __init__( self, iteration, parent=None, data=None):
        self.iteration = iteration
        self.parent = parent
        self.data = data


    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_iteration(self):
        return self.iteration

    def set_iteration(self, new_iteration):
        self.iteration = new_iteration

    def get_parent(self):
        return self.parent

    def set_parent(self, new_parent):
        self.parent = new_parent
