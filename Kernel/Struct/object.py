from ExceptionAndDebug.exception import *
from copy import deepcopy


class AGIObject:
    def __init__(self, concept_id: int, attributes: dict or None):
        self.concept_id = concept_id
        self.attributes = attributes


class AGIList:
    def __init__(self, value: list = None):
        if value is None:
            self.forward = []
            self.reverse = []
            self.value = []
        else:
            self.forward = deepcopy(value)
            self.reverse = []
            self.value = deepcopy(value)

    def update(self):
        reverse = deepcopy(self.reverse)
        reverse.reverse()
        self.value = self.forward + reverse

    def set_forward(self, index, value):
        if len(self.forward) == index:
            self.forward.append(value)
        elif len(self.forward) < index:
            self.forward += [[None] * (index - len(self.forward))]
            self.forward.append(value)
        else:
            if self.forward[index] is not None:
                raise AGIException(19)
            self.forward[index] = value
        self.update()

    def set_reverse(self, index, value):
        if len(self.reverse) == index:
            self.reverse.append(value)
        elif len(self.reverse) < index:
            self.reverse += [None for i in range(index - len(self.reverse))]
            self.reverse.append(value)
        else:
            if self.reverse[index] is not None:
                raise AGIException('Reverse index in AGIList is already occupied.')
            self.reverse[index] = value
        self.update()

    def get_element(self, index) -> any:
        return self.value[index]

    def get_element_reverse(self, index) -> any:
        if len(self.value) - index - 1 < 0:
            print(self.forward)
            print(self.reverse)
            print(self.value)
            raise AGIException('index < 0')
        return self.value[len(self.value) - index - 1]

    def size(self) -> int:
        return len(self.value)

    def get_list(self) -> list:
        return self.value
