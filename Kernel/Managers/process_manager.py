from ExceptionAndDebug.exception import *


class Process:
    next_id = 0

    def __init__(self, parent_id, method_id, input_params):
        self.parent_id = parent_id
        self.method_id = method_id
        self.input_params = input_params
        self.children_id = []
        self.registers = []
        self.id = Process.next_id
        self.terminated = False
        Process.next_id += 1


class ProcessManager:

    def __init__(self):
        self.processes = []
        self.current_proc = None

    def create_process(self, caller_id, method_id, input_params) -> int:
        self.processes.append(Process(caller_id, method_id, input_params))
        self.current_proc = self.processes[-1]
        return Process.next_id - 1

    def destroy_process(self, proc_id):
        for proc in self.processes:
            if proc.id == proc_id:
                proc.terminated = True
                if proc.parent_id is not None:
                    found = False
                    for parent in self.processes:
                        if parent.id == proc.parent_id:
                            self.current_proc = parent
                            found = True
                    if not found:
                        raise AGIException('Can\'t find parent.')
                else:
                    self.current_proc = None
                return
        raise AGIException('Can\'t find target process.')
