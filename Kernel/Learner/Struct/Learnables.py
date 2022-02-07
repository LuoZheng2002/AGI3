from Kernel.Struct.bytecode_format import r
from Kernel.Struct.object import AGIObject, AGIList
from Kernel.Struct.system_functions import sc
from Kernel.Struct.system_types import st
from concept_instance_code import ci
from main import d
from test_concepts import an
from test_method_codes import cc


class Stage0:
    def __init__(self):
        self.origin = None
        self.input_params = None
        self.input_roles = None
        self.output = None
        self.output_roles = None
        self.debug_desc = None
        self.instances = None


class Stage0Instance:
    def __init__(self):
        self.input_params = None
        self.output = None
        self.steps = None


class Stage0Step:
    def __init__(self):
        self.action = None
        self.action_origin = None
        self.reason = None
        self.reason_origin = None
