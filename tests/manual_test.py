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
    test_menu._cursor_coordinates = [1, 0, 0]
    test_menu.show_frame_menu()
    test_menu._cursor_coordinates = [2, 0, 0]
    test_menu.show_frame_menu()

    """
    while True:
        x = test_menu._column_object_index(coord=(1, 1, 1), mode="Option")
        print(x)
        #pprint(test_menu._options_list)
        test_menu.change_coordinate_cursor(input("..."))
    """


if __name__ == "__main__":
    main()