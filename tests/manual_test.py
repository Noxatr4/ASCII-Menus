import string
from os import system
from pprint import pprint

from src.ASCII_Menus import Menu

TEST_LIST = []
TEST_LIST.extend(string.ascii_lowercase)
#print(TEST_LIST)

def sum_01():
    return 1 + 1

def sum_01():
    return 1 + 2


def sum_02():
    return 1 + 3


def sum_03():
    return 1 + 4


def sum_04():
    return 1 + 5

def main():
    functions_list = [
        sum_01,
        sum_02,
        sum_03,
        sum_04,
    ]

    test_menu = Menu("test_menu", 2, 3, 5, TEST_LIST)
    test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [1, 0, 0]
    #test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [2, 0, 0]
    #test_menu.show_frame_menu()
    #test_menu[[0, 0, 0]] = "a"
    test_menu._add_function_to_menu(functions_list)

    while True:
        input_u = input("...")
        test_menu.control_menu(input_u)
        test_menu.show_frame_menu()
        if input_u.upper() == "M":
            pprint(test_menu.__dict__)
            exit("finished")

if __name__ == "__main__":
    main()