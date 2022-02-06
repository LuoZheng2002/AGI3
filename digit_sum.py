from Kernel.Struct.bytecode_format import r
from Kernel.Struct.system_functions import sc
from test_method_codes import cc

digit_sum = [
    [r['assign'], [r['reg'], 0, []], [r['concept_instance'], 2]],
    [r['if'],
        [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
        [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]],
        [
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['0']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['1']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['2']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['3']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['4']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['5']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['6']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['7']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['8']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['9']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['0']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['9']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['1']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['0']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['2']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['1']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['3']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['2']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['4']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['3']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['5']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['4']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['6']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['5']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['7']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['6']]]]
            ],
            [
                [r['system_call'], sc['and'], [[r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 0], 0], [r['concept_instance'], cc['9']]]], [r['system_call'], sc['=='], [[r['at_reverse'], [r['input'], 1], 0], [r['concept_instance'], cc['8']]]]]],
                [[r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
                [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['7']]]]
            ]
        ],
        [
            [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [1]], [r['concept_instance'], cc['1']]],
            [r['assign'], [r['at_reverse'], [r['reg'], 0, []], [0]], [r['concept_instance'], cc['8']]]
        ]
    ],
    [r['return'], [r['reg'], 0, []]]
]