from types import FunctionType
import string
from os import system
from pprint import pprint

from src.ASCII_Menus import Menu

TEST_LIST = []
TEST_LIST.extend(string.ascii_lowercase)
#print(TEST_LIST)

def sum_01(x: int, y: int):
    return x + y

def sum_02(x: int, y: int):
    return x + y


def sum_03(x: int, y: int):
    return x + y


def sum_04(x: int, y: int):
    return x + y


def sum_05(x: int, y: int):
    return x + y

def main():
    functions_list = [
        (sum_01, {"x": 1,"y": 10}),
        (sum_02, {"x": 2,"y": 11}),
        (sum_03, {"x": 3,"y": 12}),
        (sum_04, {"x": 4,"y": 13}),
        (sum_05, {"x": 5,"y": 14})
    ]

    test_menu = Menu("test_menu", 2, 3, 5, TEST_LIST)
    test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [1, 0, 0]
    #test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [2, 0, 0]
    #test_menu.show_frame_menu()
    #test_menu[[0, 0, 0]] = "a"
    #test_menu.add_function_to_menu(functions_list)

    #a = test_menu._functions_dictionary[(0, 2, 0)]["function"](**test_menu._functions_dictionary[(0, 2, 0)]["kwargs"])
    #print(a)
    #test_menu._input_validator(lambda a: (a == "a"), "...")
    test_menu.add_function_to_menu((sum_01, functions_list[0][1]))


    print("a")
    """
    while True:
        input_u = input("...")
        test_menu.control_menu(input_u)
        test_menu.show_frame_menu()
        if input_u.upper() == "M":
            pprint(test_menu.__dict__)
            exit("finished")"""

if __name__ == "__main__":
    main()