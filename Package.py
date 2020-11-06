from enum import Enum
import Address


class Package:

    class Status(Enum):
        HUB = "At the Hub"
        ENROUTE = "En route"
        DELIVERED = "Delivered"

    def with_status(self, status):
        return Package(self.pkgid, self.addr, self.deadline, self.weight, self.notes, status)

    def __init__(self, pkgid, addr: Address.Address, deadline, weight, notes, status=Status.HUB):
        self.pkgid = pkgid
        self.addr = addr
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status


