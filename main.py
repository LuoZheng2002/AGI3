from Kernel.Executer.method_runner import *
from test_concepts import an


def main():
    number1 = AGIObject(2, {an['value']: AGIList([1, 2, 3, 4])})
    number2 = AGIObject(2, {an['value']: AGIList([5, 6, 7])})
    result = run_method(1, [number1, number2], None)
    print(result)
    str_result = ''
    for digit in result.attributes[an['value']]:
        str_result += str(digit.concept_id - 100)
    print('The final result is: ' + str_result)


if __name__ == '__main__':
    main()
