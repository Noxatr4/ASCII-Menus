import string
from os import system
from pprint import pprint

import ASCII_Menus

TEST_LIST = []
TEST_LIST.extend(string.ascii_lowercase)
print(TEST_LIST)

def main():
    test_menu = ASCII_Menus.Menu("test_menu", 1, 5, 5, TEST_LIST)

    while True:
        system("cls")
        pprint(test_menu.menu_crafter())
        test_menu.change_coordinate_cursor(input("..."))



if __name__ == "__main__":
    main()