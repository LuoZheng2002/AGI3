from Kernel.Learner.Struct.Learnables import Stage0Step
from Kernel.Struct.bytecode_format import r
from Kernel.Struct.system_functions import sc
from Kernel.Struct.system_types import st
from concept_instance_code import ci
from test_method_codes import mc


def step1():
    step = Stage0Step()
    step.action_origin = \
        '''
        First, write the two numbers in the following format:

        1319
          46

        '''
    step.action = [
        [r['assign'], [r['reg'], 0, []], [r['system_type'], st['2DMap']]],
        [r['assign'], [r['reg'], 1, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['1']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 2, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['3']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 3, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['1']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 4, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['9']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 5, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['4']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 6, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['6']]
                ]
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 2, []],
                [r['reg'], 1, []],
                ['right']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 3, []],
                [r['reg'], 2, []],
                ['right']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 4, []],
                [r['reg'], 3, []],
                ['right']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 6, []],
                [r['reg'], 5, []],
                ['right']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 5, []],
                [r['reg'], 3, []],
                ['down']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 6, []],
                [r['reg'], 4, []],
                ['down']
            ]
        ],
    ]
    step.reason_origin = None
    step.reason = None
    return step


def step2():
    step = Stage0Step()
    step.action_origin = \
        '''
        Then you find the sum of 9 and 6.
        If you don't know how to do it,
        you should first learn how to find the sum of two single digit numbers.
        The sum of 9 and 6 is 15
        '''
    step.action = [
        [r['assign'],
            [r['reg'], 7, []],
            [
                r['call'], mc['digit sum'],
                [
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['9']]]],
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['6']]]]
                ]
            ]
        ],
        [r['assert'], [r['system_call'], sc['and'],
            [
                [r['system_call'], sc['=='], [[r['size'], [r['reg'], 7, []]], [2]]],
                [r['system_call'], sc['=='], [[r['at'], [r['reg'], 7, []], [0]], [r['concept_instance'], ci['1']]]],
                [r['system_call'], sc['=='], [[r['at'], [r['reg'], 7, []], [1]], [r['concept_instance'], ci['5']]]]
            ]
        ]]
    ]
    step.reason_origin = None
    step.reason = None
    return step


def step3():
    step = Stage0Step()
    step.action_origin = \
        '''
        so you write down the two digits like this:

        1319
          46
          1
           5

        '''
    step.action = [
        [r['assign'], [r['reg'], 8, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['1']]
                ]
            ]
        ],
        [r['assign'], [r['reg'], 9, []],
            [r['system_call'], sc['2DMap']['add_element'],
                [
                    [r['reg'], 0, []],
                    [r['concept_instance'], ci['5']]
                ]
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 8, []],
                [r['reg'], 5, []],
                ['down']
            ]
        ],
        [r['system_call'], sc['2DMap']['add_pos'],
            [
                [r['reg'], 0, []],
                [r['reg'], 9, []],
                [r['reg'], 6, []],
                ['down']
            ]
        ]
    ]
    step.reason_origin = None
    step.reason = None
    return step


def step4():
    step = Stage0Step()
    step.action_origin = \
        '''
        Then you find the sum of 1 and 4, and you get 5.
        '''
    step.action = [
        [r['assign'],
            [r['reg'], 10, []],
            [
                r['call'], mc['digit sum'],
                [
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['1']]]],
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['4']]]]
                ]
            ]
        ]
    ]
    step.reason_origin = None
    step.reason = None
    return step


def step5():
    step = Stage0Step()
    step.action_origin = \
        '''
        Because there is a '1' under 1 and 4, you need to find the sum of 1 and 5, and you get 6.
        '''
    step.action = [
        [r['assign'],
            [r['reg'], 11, []],
            [
                r['call'], mc['digit sum'],
                [
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['1']]]],
                    [r['call'], mc['digit to number'], [[r['concept_instance'], ci['5']]]]
                ]
            ]
        ],
        [r['assert'], [r['system_call'], sc['and'],
            [
                [r['system_call'], sc['=='], [[r['size'], [r['reg'], 11, []]], [1]]],
                [r['system_call'], sc['=='], [[r['at'], [r['reg'], 11, []], [0]], [r['concept_instance'], ci['6']]]]
            ]
        ]]
    ]
    step.reason_origin = \
        '''
        Because there is a '1' under 1 and 4
        '''
    step.reason = [

    ]