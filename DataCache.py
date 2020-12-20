
from ReadCSV import init_distance_data, init_location_data, init_pkg_data


class DataCache:
    def __init__(self):
        self.distances = init_distance_data()
        self.locations = init_location_data(self.distances)
        self.packages = init_pkg_data(self.locations)
        self.trucks = {}
