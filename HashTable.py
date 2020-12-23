import math
from Package import Package


class HashTable:

    def __init__(self):
        self.collision_safety = 10
        self.array = [[] for i in range(100)]
        self.length = 0

    def put(self, key: int, value, is_resize=False):

        if key <= 0 or value is not Package:
            raise ValueError
        try:
            # _hash_mid_square is O(1)
            loc = math.floor(self._hash_mid_square(key))
            if len(self.array[loc]) + 1 > self.collision_safety:
                # self.resize is O(n) average.
                # If resizes chain off of each other, time complexity gets much worse
                # This is not likely with doubling the size of the table and the hash
                # function self-adjusting as n increases.
                self.resize()
                loc = int(self._hash_mid_square(key))
        except ValueError as ve:
            raise ve

        # Collision safety = 10 so this is O(1)
        for i in range(0, len(self.array[loc])):
            p: Package = self.array[loc][i]
            if p.pkgid == key:
                self.array[loc][i] = value
                return

        (self.array[loc]).append(value)
        if not is_resize:
            self.length += 1

    def get(self, key):
        try:
            list_loc: list = self.array[self._hash_mid_square(key)]
            for pkg in list_loc:
                if pkg.pkgid == key:
                    return pkg
        except ValueError as ve:
            raise ve

    def contains_key(self, key):
        try:
            for item in self.array[self._hash_mid_square(key)]:
                if item == key:
                    return True
        except():
            raise ValueError
        finally:
            return False

    # All operations in _hash_mid_square are constant time, therefore the method is as well.
    def _hash_mid_square(self, key):
        # Using Mid-Square hash function as taught in class material Figure 7.6.2
        try:
            # self-adjust to make number of bits more appropriate as n increases
            # in order to improve collision rate
            num_bits = 20
            hex_representation = 0xFFFFF
            if self.length < 1000:
                num_bits = 32
                hex_representation = 0xFFFFFFFF

            squared_key = (key + 100) ** 2

            bits = math.ceil(math.log(len(self.array), 2))

            low_bits_to_remove = (num_bits - bits) // 2
            extracted_bits = squared_key >> low_bits_to_remove
            extracted_bits = extracted_bits & (hex_representation >> (num_bits - bits))

            return extracted_bits % len(self.array)
        except():
            raise ValueError("key not a number")

    # resize copies the existing elements into a temporary list, then creates a new list for
    # self.array that is twice the previous size. It then iterates through the list of buckets
    # and iterates through the list at each bucket calling self.put on each element
    # to place it in the new array.
    #
    # resize runs in O(n) average with the assumption that the hash function above
    # distributes packages reasonably evenly
    def resize(self):
        tmp_arr = self.array
        self.array = [[] for i in range(len(tmp_arr) * 2)]
        for location in tmp_arr:
            for item in location:
                p: Package = item
                self.put(p.pkgid, p, True)

    def len(self):
        return self.length
