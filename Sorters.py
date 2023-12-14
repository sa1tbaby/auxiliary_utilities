import random
import sys


class SortingMethods:


    @staticmethod
    def bubble(
            list_: list[int]
    ):

        list_size = len(list_) - 1

        while list_size != 0:
            for index, value in enumerate(list_):

                if index == list_size:
                    list_size -= 1
                    break

                if value > list_[index + 1]:
                    list_[index] = list_[index + 1]
                    list_[index + 1] = value

        return list_
    @staticmethod
    def sheiker(
            list_: list[int]
    ):

        list_size = len(list_) - 1
        list_size_reverse = 0
        direction = False

        while list_size != list_size_reverse:

            direction = bool(abs(direction - 1))

            for index, _ in enumerate(list_):
                if direction:
                    index = index + list_size_reverse
                    value = list_[index]

                    if index == list_size:
                        list_size -= 1
                        break

                    if value > list_[index + 1]:
                        list_[index] = list_[index + 1]
                        list_[index + 1] = value

                else:
                    index = list_size - index
                    value = list_[index]

                    if index == list_size_reverse:
                        list_size_reverse += 1
                        break

                    if value < list_[index - 1]:
                        list_[index] = list_[index - 1]
                        list_[index - 1] = value

        return list_
        
    @staticmethod
    def fast(
            list_: list[int]
    ):

        def sort(list_: list[int]):

            if len(list_) <= 1:
                return list_

            support_element = list_[0]
            list_least = list()
            list_largest = list()

            for value in list_[1:]:
                if value >= support_element:
                    list_largest.append(value)
                else:
                    list_least.append(value)

            return sort(list_least) + [support_element] + sort(list_largest)

        return sort(list_)

    @staticmethod
    def merge(
            list_: list[int]
    ):
        list_left = list_[:int(len(list_) / 2)]
        list_right = list_[int(len(list_) / 2):]




