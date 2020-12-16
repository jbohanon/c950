import datetime


class Stop:
    def __init__(self, num, time, addr):
        self.num = num
        self.time = time
        self.addr = addr

    @staticmethod
    def hub(time=datetime.time(8, 0, 0)):
        return Stop(0, time, "4001 South 700 East")