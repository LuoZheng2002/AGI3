from Kernel.Executer.method_runner import *


def main():
    result = run_method(4, [], None)
    print(result)
    print(result.concept_id)


if __name__ == '__main__':
    main()
