from types import FunctionType
import string
from os import system
from pprint import pprint

from src.ASCII_Menus import Menu

TEST_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
#TEST_LIST.extend(string.ascii_lowercase[0:12])
TEST_MENU = Menu("test_menu", 2, 3, 10, TEST_LIST)


def f_01(x: int, y: int):
    print(x + y)

def f_02(x: int, y: int):
    print(x + y)


def f_03(x: int, y: int):
    print(x + y)


def f_04(x: int, y: int):
    print(x + y)


def f_05(x: int, y: int):
    print(x + y)

def f_06(x: int, y: int):
    print(x + y)

def f_07(x: int, y: int):
    print(x + y)


def f_08(x: int, y: int):
    print(x + y)


def f_09(x: int, y: int):
    print(x + y)


def f_10(x: int, y: int):
    print(x + y)


def f_11(x: int, y: int):
    print(x + y)


def f_12(x: int, y: int):
    print(x + y)


def main():
    functions_list = [
        (f_01, {"x": 1,"y": 10}),
        (f_02, {"x": 2,"y": 11}),
        (f_03, {"x": 3,"y": 12}),
        (f_04, {"x": 4,"y": 13}),
        (f_05, {"x": 5,"y": 14}),
        (f_06, {"x": 6, "y": 15}),
        (f_07, {"x": 7, "y": 16}),
        (f_08, {"x": 8, "y": 17}),
        (f_09, {"x": 9, "y": 18}),
        (f_10, {"x": 10, "y": 19}),
        (f_11, {"x": 11, "y": 20}),
        (f_12, {"x": 12, "y": 21}),
    ]

    TEST_MENU.add_function_to_menu(functions_list)

    TEST_MENU.show_frame_menu()

    while True:
        input_u = input("...")
        system("cls")
        TEST_MENU.control_menu(input_u)
        TEST_MENU.show_frame_menu()

if __name__ == "__main__":
    main()