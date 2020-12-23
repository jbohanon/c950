import datetime

from ReadCSV import init_distance_data, init_location_data, init_pkg_data


class DataCache:
    def __init__(self):
        self.distances = init_distance_data()
        self.locations = init_location_data(self.distances)
        self.packages = init_pkg_data(self.locations)
        self.trucks = {}

    # print_all_packages runs in O(n) for space and time.
    def print_all_packages(self, check_time: datetime.time):
        print("Printing package status report for " + check_time.strftime("%X"))
        print("ID".ljust(2), "| Status".ljust(35), "| Address".ljust(41), "| Deadline".ljust(9),
              "| Weight (lb)".ljust(12), "| Notes")
        for i in range(1, self.packages.len() + 1):
            import Package
            pkg: Package.Package = self.packages.get(i)
            pkg.print(check_time, self.trucks[pkg.truck_assignment].start_time)
