import datetime
import string

from DataCache import DataCache
import Package


def core_loop(dc: DataCache):
    while True:
        print("Please make a selection:")
        print("1) Check status of all packages at a given time")
        print("2) Exit")
        print()
        sel = input()
        if sel == "1":
            while True:
                try:
                    hour = input("Enter hour\n")
                    hour_int = int(hour)
                    minute = input("Enter minute\n")
                    minute_int = int(minute)
                except ValueError:
                    print("Must enter a number")
                    continue
                if hour_int and minute_int:
                    break

            print_all_packages(dc, datetime.time(hour_int, minute_int))
        elif sel == "2":
            break
        else:
            print("Invalid selection")


def print_all_packages(dc: DataCache, check_time: datetime.time):

    print("ID".ljust(2), "| Status".ljust(11), "| Address".ljust(49), "| Deadline".ljust(9), "| Weight (lb)".ljust(12), "| Notes")
    for i in range(1, dc.packages.len() + 1):
        pkg: Package.Package = dc.packages.get(i)
        if check_time > pkg.delivery_time:
            pkg.status = Package.Status.DELIVERED
        elif check_time > dc.trucks[pkg.truck_assignment].start_time:
            pkg.status = Package.Status.ENROUTE
        elif check_time < datetime.time(9, 5) and "Delayed on flight" in pkg.notes:
            pkg.status = Package.Status.DELAYED
        else:
            pkg.status = Package.Status.HUB
        print(str(pkg.pkgid).ljust(3) + "| " + str(pkg.status.value).ljust(10) + "| " + str(pkg.addr.addr).ljust(48) + "| " + str(pkg.priority.value).ljust(9) + "| " + str(pkg.weight).ljust(12) + "| " + pkg.notes)
