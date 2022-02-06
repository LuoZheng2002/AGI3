from Kernel.Struct.bytecode_format import r
from Kernel.Struct.system_functions import sc

test_method = [
    [r['if'], [r['system_call'], sc['=='], [[101], [100]]],
        [
           [r['return'], [r['concept_instance'], 100]]
        ],
        [
            [[r['system_call'], sc['=='], [[1], [2]]], [[r['return'], [r['concept_instance'], 101]]]],
            [[r['system_call'], sc['>'], [[2], [2]]], [[r['return'], [r['concept_instance'], 102]]]],
            [[r['system_call'], sc['<='], [[1], [0]]], [[r['return'], [r['concept_instance'], 103]]]],
        ],
        [
            [r['return'], [r['concept_instance'], 104]]
        ]
    ]
]
