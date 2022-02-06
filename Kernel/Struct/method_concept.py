class MethodInfo:
    pass


class Method:
    def __init__(self, method_id, code, info):
        self.method_id = method_id
        self.code = code
        self.info = info


class ConceptInfo:
    def __init__(self, concept_type, structure):
        self.type = concept_type
        self.structure = structure


class Concept:
    def __init__(self, concept_id, ci: ConceptInfo):
        self.id = concept_id
        self.ci = ci

