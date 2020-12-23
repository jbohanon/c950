import datetime
from enum import Enum
import Address


class Status(Enum):
    HUB = "At the Hub"
    ENROUTE = "En route"
    DELIVERED = "Delivered"
    DELAYED = "Delayed"


class Priority(Enum):
    HIGH = "900"
    MED = "1030"
    LOW = "EOD"


class Package:

    def with_status(self, status):
        return Package(self.pkgid, self.addr, self.priority, self.weight, self.notes, self.pairings, self.truck, status)

    def with_address(self, addr):
        return Package(self.pkgid, addr, self.priority, self.weight, self.notes, self.pairings, self.truck, self.status)

    def __init__(self, pkgid, addr: Address.Address, priority, weight, notes, pairings=None, truck=-1, status=Status.HUB):
        self.pkgid = pkgid
        self.addr = addr
        self.priority = priority
        self.weight = weight
        self.notes = notes
        self.pairings = (list() if pairings is None else pairings)
        self.truck = truck
        self.status = status
        self.delivery_time: datetime.time = datetime.time(11, 59, 59)
        self.truck_assignment = 0
        
    def print(self, check_time, truck_start_time):
        if check_time > self.delivery_time:
            self.status = Status.DELIVERED
        elif check_time > truck_start_time:
            self.status = Status.ENROUTE
        elif check_time < datetime.time(9, 5) and "Delayed on flight" in self.notes:
            self.status = Status.DELAYED
        else:
            self.status = Status.HUB

        if self.status == Status.DELIVERED:
            print(str(self.pkgid).ljust(3) + "| " + str(
                self.status.value + " at " + self.delivery_time.strftime("%X")).ljust(23) + "| " + str(
                self.addr.addr).ljust(48) + "| " + str(self.priority.value).ljust(9) + "| " + str(self.weight).ljust(
                12) + "| " + self.notes)
        else:
            print(
                str(self.pkgid).ljust(3) + "| " + str(self.status.value).ljust(23) + "| " + str(self.addr.addr).ljust(
                    48) + "| " + str(self.priority.value).ljust(9) + "| " + str(self.weight).ljust(
                    12) + "| " + self.notes)
