from enum import Enum
import Address


class Status(Enum):
    HUB = "At the Hub"
    ENROUTE = "En route"
    DELIVERED = "Delivered"


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
        # self.manual_load = (True if (notes != '' or pairings != '' or truck != '') else False)


