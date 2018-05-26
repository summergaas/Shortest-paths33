class edge():
    def __init__( self, u, v, capacity, flow=0):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = flow
   
    def get_u(self):
        return self.u

    def get_v(self):
        return self.v

    def get_capacity(self):
        return self.capacity

    def get_flow(self):
        return self.flow

    def set_flow(self, new_flow):
        self.flow = new_flow
