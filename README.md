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

test_menu = Menu("test_menu", 3, 4, 5,
                 [
                     "test", "....", "menu",
                     "test", "....", "menu",
                     "test", "....", "menu",
                     "test", "....", "menu",
                 ])
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
test_menu
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

### Select option

```python
...
input_user = input()

test_menu.control_menu(input_user)
```
Returns a tuple containing the cursor coordinates and the name option string, if `input_user` == `OK_BUTTON`.

```
("test", [0, 1, 0])
```


## 🌎 Real-World Examples

A short application example
```python
from ASCII_Menus import Menu
import readchar

# Create your menu
TEST_MENU = Menu("test_menu", 3, 4, 5,
                 [
                     "test", ":", "menu",
                     "test", ":", "menu",
                     "test", ":", "menu",
                     "test", ":", "menu",
                 ])

SELECT_KEY = "q"
TEST_OPTION = "test"

def options_test():
    ...

def main():
    while True:
        input_user = readchar.readchar()
        select_option = ""
        # If you select the option
        if input_user.lower() == SELECT_KEY:
            select_option = TEST_MENU.select_option()[1]
        
        # Ejecute function associated with the menu
        if select_option == TEST_OPTION:
            options_test()
        
        # Show menu and update cursor coordinates.
        TEST_MENU.menu_crafter()
        TEST_MENU.control_menu(input_user)
        

if __name__ == "__main__":
    main()
```

## 📄 License
This project is licensed under the [MIT License](./LICENSE).

## 📬 Contact
For any inquiries, reach out to me via:

* **GitHub**: [Noxatr4](https://github.com/Noxatr4)