import collections
import math
from abc import ABC

from Package import Package


class HashTable:
    # def __iter__(self):
    #     return HTI(self)

    def __init__(self):
        self.collision_safety = 10
        self.array = [[] for i in range(100)]

    def put(self, key, value):

        if key <= 0:
            raise ValueError
        try:
            loc = math.floor(self._hash_mid_square(key))
            if len(self.array[loc]) + 1 > self.collision_safety:
                self.resize()
                loc = int(self._hash_mid_square(key))
        except ValueError as ve:
            raise ve

        for i in range(0, len(self.array[loc])):
            p: Package = self.array[loc][i]
            # print(p)
            if p.pkgid == key:
                self.array[loc][i] = value
                break

        (self.array[loc]).append(value)

    def get(self, key):
        try:
            for pkg in self.array[self._hash_mid_square(key)]:
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

    # def _hash_func_deprecated(self, key_seed):
    #     try:
    #         return ((math.e ** key_seed) % key_seed) % len(self.array)
    #     except():
    #         raise ValueError("key_seed not a number")

    def _hash_mid_square(self, key):
        try:
            squared_key = (key + 100) ** 2

            bits = math.ceil(math.log(len(self.array), 2))

            low_bits_to_remove = (32 - bits) // 2
            extracted_bits = squared_key >> low_bits_to_remove
            extracted_bits = extracted_bits & (0xFFFFFFFF >> (32 - bits))

            return extracted_bits % len(self.array)
        except():
            raise ValueError("key not a number")

    def resize(self):
        tmp_arr = self.array
        self.array = [[] for i in range(len(tmp_arr) * 2)]
        for location in tmp_arr:
            for item in location:
                p: Package = item
                self.put(p.pkgid, p)


# class HTI:
#     def __init__(self, ht):
#         self._ht = ht
#         self._array_index = 0
#         self._list_index = 0
#
#     def __next__(self):
#         if self._array_index < (len(self._ht.array)):
#             if self._list_index < len(self._ht.array[self._array_index]):
#                 result = self._ht.array[self._array_index][self._list_index]
#                 self._list_index += 1
#                 return result
#             else:
#                 self._array_index += 1
#
#         raise StopIteration
