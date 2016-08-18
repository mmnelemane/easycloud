# Parent module for generic API declarations
class Manager(object):
    # All API classes inherit from this class and re-implement or reuse the APIs
    def __init__(self):
        pass

    def create(self):
        pass

    def destroy(self):
        pass

    def list(self):
        pass

    def update(self):
        pass
