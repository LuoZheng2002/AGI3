from ExceptionAndDebug.exception import *
from Kernel.Struct.object import AGIObject


def equal(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) == int:
        if type(params[1]) == int:
            if params[0] == params[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        if not (type(params[0]) == AGIObject and type(params[1]) == AGIObject):
            raise AGIException('Input is neither integer nor AGIObject', special_name='type', special_str=str(type(params[0])))
        if params[0].concept_id == params[1].concept_id:
            return True
        else:
            return False


def greater(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) != int or type(params[1]) != int:
        raise AGIException(16)
    return params[0] > params[1]


def greater_or_equal(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) != int or type(params[1]) != int:
        raise AGIException(16)
    return params[0] >= params[1]


def less(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) != int or type(params[1]) != int:
        raise AGIException(16)
    return params[0] < params[1]


def less_or_equal(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) != int or type(params[1]) != int:
        raise AGIException(16)
    return params[0] <= params[1]


def and_(params: list) -> bool:
    for param in params:
        if type(param) != bool:
            raise AGIException('Parameters in and function should be bool')
        if not param:
            return False
    return True


def or_(params: list) -> bool:
    for param in params:
        if type(param) != bool:
            raise AGIException('Parameters in or function should be bool')
        if param:
            return True
    return False


def max_(params: list) -> bool:
    max_value = -0x80000000
    for value in params:
        if type(value) != int:
            raise AGIException('Params in max function should be int.')
        if value > max_value:
            max_value = value
    return max_value


def min_(params: list) -> bool:
    min_value = 0xffffffff
    for value in params:
        if type(value) != int:
            raise AGIException('Params in min function should be int.')
        if value < min_value:
            min_value = value
    return min_value


def offset(params: list) -> bool:
    if len(params) != 2:
        raise AGIException(15)
    if type(params[0]) != int or type(params[1]) != int:
        raise AGIException(16)
    return params[0] + params[1]


sc = {
    '==': 1,
    '>': 2,
    '>=': 3,
    '<': 4,
    '<=': 5,
    'and': 6,
    'or': 7,
    'max': 8,
    'min': 9,
    'offset': 10,
    '2DMap': {'add_element': 11, 'add_pos': 12}
}

system_call = {
    1: equal,  # '=='
    2: greater,  # '>'
    3: greater_or_equal,  # '>='
    4: less,  # '<'
    5: less_or_equal,  # '<='
    6: and_,  # 'and'
    7: or_,  # 'or'
    8: max_,  # 'max'
    9: min_,  # 'min'
    10: offset  # 'offset'
}

# rsc = {v: k for k, v in sc.items()}
