import string
from os import system
from pprint import pprint

from src.ASCII_Menus import Menu

TEST_LIST = []
TEST_LIST.extend(string.ascii_lowercase)
print(TEST_LIST)

def main():
    test_menu = Menu("test_menu", 2, 5, 5, TEST_LIST)
    test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [1, 0, 0]
    #test_menu.show_frame_menu()
    #test_menu._cursor_coordinates = [2, 0, 0]
    #test_menu.show_frame_menu()


    while True:
        test_menu.control_menu(input("..."))
        test_menu.show_frame_menu()


if __name__ == "__main__":
    main()