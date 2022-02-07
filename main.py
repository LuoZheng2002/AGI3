from Kernel.Executer.method_runner import *
from test_concepts import *

d = {
    0: AGIObject(100, dict()),
    1: AGIObject(101, dict()),
    2: AGIObject(102, dict()),
    3: AGIObject(103, dict()),
    4: AGIObject(104, dict()),
    5: AGIObject(105, dict()),
    6: AGIObject(106, dict()),
    7: AGIObject(107, dict()),
    8: AGIObject(108, dict()),
    9: AGIObject(109, dict())
}


def main():
    try:
        number1 = AGIObject(2, {an['value']: AGIList([d[1], d[3], d[1], d[9]])})
        number2 = AGIObject(2, {an['value']: AGIList([d[4], d[6]])})
        result = run_method(1, [number1, number2], None)
        print(result)
        str_result = ''
        for digit in result.attributes[an['value']].get_list():
            str_result += str(digit.concept_id - 100)
        print('The final result is: ' + str_result)
    except AGIException as e:
        e.show()


if __name__ == '__main__':
    main()
