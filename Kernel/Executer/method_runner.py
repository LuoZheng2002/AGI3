from Kernel.Struct.object import AGIObject, AGIList
from Kernel.Struct.bytecode_format import *
from Kernel.Struct.system_functions import *
from Kernel.Struct.system_types import *
from Kernel.Managers.resource_manager import ResourceManager
from ExceptionAndDebug.exception import AGIException
import Kernel.global_resource as gr
from copy import deepcopy


class CodeIterator:
    def __init__(self, method_code):
        self.list_codes = method_code
        self.line_count = len(method_code)
        self.current_line = None
        self.next_line_index = 0  # line is also counted from 0

    def get_next_line(self):
        self.current_line = self.list_codes[self.next_line_index]
        self.next_line_index += 1

    def end_of_code(self) -> bool:
        return self.next_line_index >= self.line_count


def get_agi_list(agi_object: AGIObject) -> AGIList:
    if len(agi_object.attributes) != 1:
        raise AGIException('Trying to get list from AGIObject but AGIObject has more than one attribute',
                           special_name='Concept id', special_str=str(agi_object.concept_id))
    for i in agi_object.attributes.values():
        if type(i) != AGIList:
            raise AGIException('Target type is not AGIList', special_name='type', special_str=str(type(i)))
        return i


def solve_expression(expr: list,
                     rsc_mng: ResourceManager,
                     ) -> AGIObject or AGIList:
    if type(expr) != list or len(expr) == 0:
        raise AGIException('An expression can\'t be of zero size.', special_name='expr', special_str=str(expr))
    # constexpr:
    if len(expr) == 1:
        return expr[0]
    head = expr[0]
    if head == r['input']:
        # format: [input, index_of_input]
        return rsc_mng.input_params[expr[1]]
    elif head == r['reg']:
        # format: [reg, index_of_reg, [expr1, expr2, ...]]
        child_index = []
        for i in expr[2]:
            child_index.append(solve_expression(i, rsc_mng))
        child_index = tuple(child_index)
        return rsc_mng.get_reg_value(expr[1], child_index)
    elif head == r['iterator']:
        # format: [iterator, index_of_iterator]
        return rsc_mng.get_iterator_value(expr[1])
    elif head == r['system_call']:
        # format: [system_call, function_id, [expr1, expr2, ...]]
        function_id = expr[1]
        params = expr[2]
        """if function_id == sc['and'] or function_id == sc['or']:
            first_result = solve_expression(expr[2][0], rsc_mng)
            if function_id == sc['and'] and not first_result:
                return False
            elif function_id == sc['or'] and first_result:
                return True"""
        if function_id == sc['and']:
            for param in params:
                single_result = solve_expression(param, rsc_mng)
                if type(single_result) != bool:
                    raise AGIException('Params in and function should be bool.')
                if not single_result:
                    return False
            return True
        elif function_id == sc['or']:
            for param in params:
                single_result = solve_expression(param, rsc_mng)
                if type(single_result) != bool:
                    raise AGIException('Params in or function should be bool.')
                if single_result:
                    return True
            return False
        function_params = []
        for i in params:
            function_params.append(solve_expression(i, rsc_mng))
        result = system_call[function_id](function_params)
        assert result is not None
        return result
    elif head == r['call']:
        # format: [call, method_id, [expr1, expr2, ...]]
        method_id = expr[1]
        method_params = []
        for i in expr[2]:
            method_params.append(solve_expression(i, rsc_mng))
        result = run_method(method_id, method_params, rsc_mng.proc_id)
        assert type(result) == AGIObject
        return result
    elif head == r['system_type']:
        # system_type type_id
        type_id = expr[1]
        return st[type_id]()
    elif head == r['concept_instance']:
        # concept_type, type_id
        type_id = expr[1]
        return gr.kd.create_concept_instance(type_id)
    elif head == r['size']:
        # size, expr
        result = solve_expression(expr[1], rsc_mng)
        if type(result) == AGIObject:
            return get_agi_list(result).size()
        else:
            assert type(result) == AGIList
            return result.size()
    elif head == r['at'] or head == r['at_reverse']:
        # at/at_reverse, target, index
        target = solve_expression(expr[1], rsc_mng)
        index = solve_expression(expr[2], rsc_mng)
        if type(target) == AGIObject:
            if head == r['at']:
                return get_agi_list(target).get_element(index)
            else:  # head == r['at_reverse']
                return get_agi_list(target).get_element_reverse(index)
        else:
            if type(target) != AGIList:
                raise AGIException('target is supposed to be AGIList or AGIObject',
                                   special_name='type of target', special_str=str(type(target)))
            if head == r['at']:
                return target.get_element(index)
            else:  # head == r['at_reverse']
                return target.get_element_reverse(index)
    elif head == r['get_member']:
        # get_member target member_name
        target = solve_expression(expr[1], rsc_mng)
        member_name = expr[2]
        if type(target) == AGIObject:
            return target.attributes[member_name]
        else:
            assert type(target) == dict
            return target[member_name]
    else:
        raise AGIException('Unexpected word at the beginning of an expression.')


def process_line(line, rsc_mng: ResourceManager, scope_info: tuple) -> dict:
    # return value: {value_type:None/'break'/'return', value:None/None/[return value]}
    return_value = {'value_type': None, 'value': None}
    head = line[0]
    if head == r['assign']:  # format: [assign, expr, expr]
        lhs_expr = line[1]
        rhs_expr = line[2]
        # because taking an element from a container and modifying it
        # doesn't really modify the element in the container
        # e.g. b = a[1]; b = 1 doesn't make a[1] to be 1
        # so we need to trace the container and the position of the element in the container
        # so that we can do something like a[1] = 2 to modify a[1]
        # lhs = [element's container, at/at_reverse/get_member, index or member name]
        lhs = [None, None, None]
        head_of_lhs = lhs_expr[0]
        reg_id = None  # only for head_of_lhs == r['reg']
        child_index = None  # only for head_of_lhs == r['reg']
        if head_of_lhs == r['reg']:  # format: [reg, index of reg, [expr1, expr2, ...]]
            # modifying register itself, so no need for the tricks above
            reg_id = lhs_expr[1]
            child_expressions = lhs_expr[2]
            # get child_index
            child_index = []
            for expr in child_expressions:
                child_index.append(solve_expression(expr, rsc_mng))
            child_index = tuple(child_index)
            # assert target register hasn't been created
            # because normally we don't want an existing register to be rewritten
            if rsc_mng.has_reg(reg_id, child_index):
                raise AGIException('Try to create a register again.')
            rsc_mng.create_reg(reg_id, scope_info, child_index)
        elif head_of_lhs == r['at'] or head_of_lhs == r['at_reverse']:
            # at, [expr], [expr]
            target = solve_expression(lhs_expr[1], rsc_mng)
            if type(target) == AGIObject:
                lhs[0] = get_agi_list(target)
            else:
                assert type(target) == AGIList
                lhs[0] = target
            lhs[1] = head_of_lhs  # 'at' or 'at_reverse'
            lhs[2] = solve_expression(lhs_expr[2], rsc_mng)
        elif head_of_lhs == r['get_member']:
            # get_member, [expr], constexpr
            target = solve_expression(lhs_expr[1], rsc_mng)
            if type(target) == AGIObject:
                lhs[0] = target.attributes
            else:
                assert type(target) == dict
                lhs[0] = target
            lhs[1] = head_of_lhs
            lhs[2] = lhs_expr[2]
        else:
            raise AGIException(20)
        # solve for rhs:
        rhs = solve_expression(rhs_expr, rsc_mng)
        # assign rhs to lhs:
        if lhs[1] is None:  # lhs[2] is None too, means that lhs[0] is register object
            rsc_mng.set_reg_value(reg_id, child_index, deepcopy(rhs))
        else:
            # if lhs[1] == r['at'] or lhs[1] == r['at_reverse'], then lhs[0] must be an AGIList
            # because lhs[0] is the product of calling get_agi_list when target is an AGIObject
            if lhs[1] == r['at']:
                lhs[0].set_forward(lhs[2], deepcopy(rhs))
            elif lhs[1] == r['at_reverse']:
                lhs[0].set_reverse(lhs[2], deepcopy(rhs))
            else:  # lhs[1] == r['get_member']
                if type(lhs[0]) != AGIObject and type(lhs[0]) != dict:
                    raise AGIException('Can only call "get_member" towards an AGIObject or a dict.')
                lhs[0][lhs[2]] = deepcopy(rhs)
    elif head == r['return']:
        result = solve_expression(line[1], rsc_mng)
        return_value = {'value_type': 'return', 'value': result}
    elif head == r['for']:
        # for, iter_id, end_value, [line1, line2, ...]
        iter_id = line[1]
        end_value = solve_expression(line[2], rsc_mng)
        for_lines = line[3]
        rsc_mng.create_iterator(iter_id)
        scope_in_for = list(scope_info)
        scope_in_for.append(iter_id)
        scope_in_for = tuple(scope_in_for)
        is_break = False
        while rsc_mng.get_iterator_value(iter_id) < end_value:
            for for_line in for_lines:
                return_value_in_for = process_line(for_line, rsc_mng, scope_in_for)
                if return_value_in_for['value_type'] == 'return':
                    return_value = return_value_in_for
                    is_break = True
                    break
                elif return_value_in_for['value_type'] == 'break':
                    is_break = True
                    break
            if is_break:
                break
            rsc_mng.update_iterator(iter_id)
    elif head == r['while']:
        # format: [while, statement, [line1, line2, line3, ...]]
        statement = line[1]
        while_lines = line[2]
        is_break = False
        while True:
            result = solve_expression(statement, rsc_mng)
            assert type(result) == bool
            if not result:
                break
            for while_line in while_lines:
                return_value_in_while = process_line(while_line, rsc_mng, scope_info)
                if return_value_in_while['value_type'] == 'return':
                    return_value = return_value_in_while
                    is_break = True
                    break
                elif return_value_in_while['value_type'] == 'break':
                    is_break = True
                    break
            if is_break:
                break
    elif head == r['break']:
        return_value = {'value_type': 'break', 'value': None}
    elif head == r['if']:
        # format: [if, statement, [line1, line2, ...], [else_if_block1, else_if_block2, ...], else_lines]
        # else_if_blocks: [statement, [line1, line2, ...]]
        # else_block: [line1, line2, ...]
        if_statement = line[1]
        if_lines = line[2]
        else_if_blocks = line[3]
        else_lines = line[4]

        # process if statement
        result = solve_expression(if_statement, rsc_mng)
        if result:
            for if_line in if_lines:
                if_return_value = process_line(if_line, rsc_mng, scope_info)
                if if_return_value['value_type'] == 'break':
                    return_value = {'value_type': 'break', 'value': None}
                    break
                elif if_return_value['value_type'] == 'return':
                    return_value = if_return_value
                    break
        else:  # if "if" statement fails, else if and else statements have an opportunity to be executed
            executed = False
            for else_if_block in else_if_blocks:
                else_if_statement = else_if_block[0]
                else_if_lines = else_if_block[1]
                result = solve_expression(else_if_statement, rsc_mng)
                if result:
                    executed = True
                    # execute the else_if lines
                    for else_if_line in else_if_lines:
                        elif_return_value = process_line(else_if_line, rsc_mng, scope_info)
                        if elif_return_value['value_type'] == 'break':
                            return_value = {'value_type': 'break', 'value': None}
                            break
                        elif elif_return_value['value_type'] == 'return':
                            return_value = elif_return_value
                            break
                    # this else_if block is executed, meaning that other else_if block should not be executed
                    break
            # execute else block
            if not executed:
                for else_line in else_lines:
                    else_return_value = process_line(else_line, rsc_mng, scope_info)
                    if else_return_value['value_type'] == 'break':
                        return_value = {'value_type': 'break', 'value': None}
                        break
                    elif else_return_value['value_type'] == 'return':
                        return_value = else_return_value
                        break
    else:
        raise AGIException('Unexpected word at the beginning of a line.')
    return return_value


def run_method(method_id, input_params: list, caller_id) -> AGIObject or None:
    # process registration
    proc_id = gr.proc_mng.create_process(caller_id, method_id, input_params)
    # local resource manager creation
    rsc_mng = ResourceManager(input_params, proc_id)
    method_code = gr.kd.get_method_code(method_id)
    # CodeIterator creation
    ci = CodeIterator(method_code)
    # start processing
    while not ci.end_of_code():
        ci.get_next_line()
        line_return_value = process_line(ci.current_line, rsc_mng, tuple())
        if line_return_value['value_type'] == 'return':
            # doing all the cleanups right before exiting the method
            gr.proc_mng.destroy_process(proc_id)
            return line_return_value['value']
        elif line_return_value['value_type'] == 'break':
            raise AGIException('Try to break without being in a for or while loop.')
        else:
            if line_return_value['value_type'] is not None:
                raise AGIException('Unexpected value type for a return value of a line.')
    raise AGIException('Method exits without return.')
