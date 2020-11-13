class Truck:
    def __init__(self, truck_num, package_list=None, stops=None):
        self.truck_num = truck_num

        if package_list is None:
            self.package_list = []
        if stops is None:
            self.stops = []
