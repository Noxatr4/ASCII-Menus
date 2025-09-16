import string
from os import system
from pprint import pprint

from ASCII_Menus import Menu

TEST_LIST = []
TEST_LIST.extend(string.ascii_lowercase)
print(TEST_LIST)


def main():
    test_menu = Menu("test_menu", 1, 5, 5, TEST_LIST)

    while True:
        system("cls")
        pprint(test_menu.menu_crafter())
        test_menu.change_coordinate_cursor(input("..."))



if __name__ == "__main__":
    main()