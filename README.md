# ASCII-Menus

ASCII_Menus is a simple library for creating different interactive menus


## 🚀 Features
* **Simple and legible menus**: Menus with options in cell format, title and displayed through the terminal.
* **Custom size menu**: Customizable size based on the number of options required, both in rows and columns.
* **Custom size options**: Customize the number of characters per option.
* **Support for multiple pages of options**
* **Simple Scroll-Bar system**
* **Two interaction modes**: *Dynamic* <--> *Static*.
* **With Cursor**


## 🛠 Installation

```bash
 $ pip install ASCII-Menus
```


## 📖 Quick Start

### Generate basic menu and show it

```python
from ASCII_Menus import Menu

options_list = [
    "test", "....", "menu",
    "test", "....", "menu",
    "test", "....", "menu",
    "test", "....", "menu"
]

test_menu = Menu("test_menu", 3, 4, 5, options_list)
test_menu.show_frame_menu()
```
```
+-------------------------+
|        test_menu        |
|-------------------------|
|                         |
| > test    ....    menu  |
|                         |
|   test    ....    menu  |
|                         |
|   test    ....    menu  |
|                         |
|   test    ....    menu  |
+-------------------------+
```


### Move cursor

```python
...
input_user = MOVE_DOWN
test_menu.control_menu(input_user)
```
```
+-------------------------+
|        test_menu        |
|-------------------------|
|                         |
|   test    ....    menu  |
|                         |
| > test    ....    menu  |
|                         |
|   test    ....    menu  |
|                         |
|   test    ....    menu  |
+-------------------------+
```

### Select option
Returns a str containing the option name, if the option contained a function, executes them.
```python
...
input_user = OK_BUTTON
name_option = test_menu.control_menu(input_user)
print(name_option)
```
```
"test"
```


## 🌎 Real-World Examples

A short application example
```python
from os import system
from src.ASCII_Menus import Menu

# Create the options
TEST_LIST = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
# To generate the Menu called "test_menu"
TEST_MENU = Menu("test_menu", 2, 3, 10, TEST_LIST)

# Functions you want to add to the menu
def f_01(x: int, y: int):...    
def f_02(x: int, y: int):...
def f_03(x: int, y: int):...
def f_04(x: int, y: int):...
def f_05(x: int, y: int):...    
def f_06(x: int, y: int):...    
def f_07(x: int, y: int):...
def f_08(x: int, y: int):...
def f_09(x: int, y: int):...
def f_10(x: int, y: int):...
def f_11(x: int, y: int):...
def f_12(x: int, y: int):...


def main():
    # List to be able to incorporate a function by positional order to each menu option
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

    # Adds all the functions to menu
    TEST_MENU.add_function_to_menu(functions_list)

    # Shows the first frame
    TEST_MENU.show_frame_menu()

    while True:
        # Catches the user input
        input_u = input("...")
        # Clean the terminal
        system("cls")
        # Checks if the input generates a valid action and executes it
        TEST_MENU.control_menu(input_u)
        # Shows the frame changed
        TEST_MENU.show_frame_menu()
        

if __name__ == "__main__":
    main()
```

## 📄 License
This project is licensed under the [MIT License](./LICENSE).

## 📬 Contact
For any inquiries, reach out to me via:

* **GitHub**: [Noxatr4](https://github.com/Noxatr4)