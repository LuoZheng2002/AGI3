from Kernel.Struct.object import AGIObject, AGIList
from ExceptionAndDebug.exception import *
import pickle
from Kernel.Struct.method_concept import Method, Concept
# get method code/info
# add method


class KnowledgeDriver:
    def __init__(self):
        self.methods = []
        self.concepts = []

    def prepare_method(self, method_id):  # to load the method to cache if not loaded
        for method in self.methods:
            if method.method_id == method_id:
                return
        # load code
        file = open('Library/Knowledge/Method/Code/' + str(method_id) + '.txt', 'rb')
        code = pickle.load(file)
        file.close()
        # load info
        file = open('Library/Knowledge/Method/Info/' + str(method_id) + '.txt', 'rb')
        info = pickle.load(file)
        file.close()
        self.methods.append(Method(method_id, code, info))

    def get_method_code(self, method_id) -> list:
        self.prepare_method(method_id)
        for method in self.methods:
            if method.method_id == method_id:
                return method.code
        raise AGIException('prepare_method doesn\'t work.')

    def get_method_info(self, method_id) -> list:
        self.prepare_method(method_id)
        for method in self.methods:
            if method.method_id == method_id:
                return method.info
        raise AGIException('prepare_method doesn\'t work.')

    def prepare_concept(self, concept_id):
        for concept in self.concepts:
            if concept.id == concept_id:
                return
        # load code
        file = open('Library/Knowledge/Concept/Info/' + str(concept_id) + '.txt', 'rb')
        concept = pickle.load(file)
        file.close()
        self.concepts.append(concept)

    def create_concept_instance(self, concept_id) -> AGIObject:
        self.prepare_concept(concept_id)
        for concept in self.concepts:
            if concept.id == concept_id:
                concept_struct = concept.ci.structure
                attributes = dict()
                for attrib_name in concept_struct:
                    attrib_type = concept_struct[attrib_name]
                    if attrib_type == 'AGIObject':
                        attributes.update({attrib_name: None})
                    elif attrib_type == 'AGIList':
                        attributes.update({attrib_name: AGIList()})
                    else:
                        raise AGIException('Unexpected type in a concept structure.')
                return AGIObject(concept_id, attributes)
        raise AGIException('prepare_concept function not working.')

