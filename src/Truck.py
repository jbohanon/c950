class Truck:
    def __init__(self, package_list=None, stops=None):
        if package_list is None:
            self.package_list = []
        if stops is None:
            self.stops = []
