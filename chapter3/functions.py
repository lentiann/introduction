def emri_function():
    print("Hello from a function")
    print("Hello from a function")
    print("Hello from a function")


def sum_internal(numrat: list) -> float:
    total = 0
    for numri in numrat:
        total += numri
    return total


def add_two_numbers(num1: float = 0.00, num2: float = 0.00) -> float:
    """This function adds two numbers and returns the sum

    Args:
        num1 (float, optional): _description_. Defaults to 0.00.
        num2 (float, optional): _description_. Defaults to 0.00.

    Returns:
        float: sum of two numbers
    """
    return num1 + num2


def function_args(*args):
    for arg in args:
        print(arg)

    print("Total arguments: ", len(args))


def function_kwargs(**kwargs):
    for arg in kwargs:
        print(arg)

    print("Total arguments: ", len(kwargs))


if __name__ == "__main__":
    # emri_function()

    # total_sum = sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # total_sum_internal = sum_internal([1.2, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # sum_of_two_numbers = add_two_numbers()

    # print("Total sum is: ", total_sum)

    # print("Total sum internal  is: ", total_sum_internal)

    # print("Sum of two numbers is: ", sum_of_two_numbers)
    # function_kwargs(test1="test", test2="test2", test3="test3")
    # function_args("1","2","3")

    two_numbers_sum = lambda num1, num2: num1 + num2
    print(two_numbers_sum(10, 20))
