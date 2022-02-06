from Kernel.Struct.bytecode_format import r
from test_method_codes import cc
digit_to_number = [
    [r['assign'], [r['reg'], 0, []], [r['concept_instance'], cc['number']]],
    [r['assign'], [r['at'], [r['reg'], 0, []], [0]], [r['input'], 0]],
    [r['return'], [r['reg'], 0, []]]
]
