from Kernel.Learner.Struct.Learnables import Stage0, Stage0Instance, Stage0Step
from Kernel.Struct.bytecode_format import r
from Kernel.Struct.object import AGIObject, AGIList
from Kernel.Struct.system_functions import sc
from Kernel.Struct.system_types import st
from concept_instance_code import ci
from main import d
from test_concepts import an
from test_method_codes import cc


def stage0_sample() -> Stage0:
    sample = Stage0()
    sample.origin = \
        '''
        The following is how to find the sum of two numbers.
        For example, to find the sum of 1319 and 46, we do the following actions.
        First, write the two numbers in the following format:
        
        1319
          46
        
        Then you find the sum of 9 and 6.
        If you don't know how to do it,
        you should first learn how to find the sum of two single digit numbers.
        The sum of 9 and 6 is 15, so you write down the two digits like this:
        
        1319
          46
          1
           5
        
        Then you find the sum of 1 and 4, and you get 5.
        Because there is a '1' under 1 and 4, you need to find the sum of 1 and 5, and you get 6.
        Then you write down 6 like this:
        
        1319
          46
          1
          65
        
        Because there's no number under '3', you write down 3 directly like this:
        
        1319
          46
          1
         365
        
        The same reason applies to '1':
        
        1319
          46
          1
        1365
        
        And 1365 is the final result.
        '''
    sample.input_params = [cc['number'], cc['number']]
    sample.input_roles = [cc['addend'], cc['addend']]
    sample.output = [cc['number']]
    sample.output_roles = [cc['sum']]
    sample.debug_desc = 'Find the sum of two numbers'
    instance1 = Stage0Instance()
    instance1.input_params = [
        AGIObject(2, {an['value']: AGIList([d[1], d[3], d[1], d[9]])}),
        AGIObject(2, {an['value']: AGIList([d[4], d[6]])})]
    instance1.output = [AGIObject(2, {an['value']: AGIList([d[1], d[3], d[6], d[5]])})]
    instance1.steps = []  # to do

    sample.instances = [instance1]
    return sample
