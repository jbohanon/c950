import datetime
from DataCache import DataCache


def core_loop(dc: DataCache):
    while True:
        print("Please make a selection:\n1) Check status of all packages at a given time\n2) Exit")
        sel = input()
        if sel == "1":
            hour_int = 8
            minute_int = 0
            while True:
                try:
                    hour = input("Enter hour\n")
                    hour_int: int = int(hour)
                    minute = input("Enter minute\n")
                    minute_int: int = int(minute)
                except ValueError:
                    print("Must enter a number")
                    continue
                if hour_int >= 0 and minute_int >= 0:
                    break

            dc.print_all_packages(datetime.time(hour_int, minute_int))
        elif sel == "2":
            break
        else:
            print("Invalid selection")
