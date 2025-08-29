import math

CURSOR_VALUES = ("   ", " > ")
DEFAULT_CHARACTERS = {
    "BodyEmptyRow": " ",
    "RowLimit": "|",
    "MenuLimitRowBody": "-",
    "MenuCorner": "+",
    "CharacterOverflow": "...",
    "SpaceCharacter": " ",
    "ScrollBarValues": ("\x1b[48;5;0m\x1b[0m ", "\x1b[48;5;255m \x1b[0m")
}

OK_BUTTON = "E"

TEST_LIST = ["aaaaaaaaaaaaaaaa", "a", "b", "c", "d", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r"]


class Menu:
    def __init__(self, title_menu: str, option_per_column: int, rows_per_page: int, max_character_per_option: int, options_list: list[str], dynamic_static_menu=True):
        # Características principales del menú
        self.type_menu = dynamic_static_menu
        self.activated: bool = False
        self.title_menu = title_menu
        self.cursor_coordinates = [0, 0, 0]

        # Estructura del menú
        self.option_per_column = option_per_column
        self.rows_per_page = rows_per_page
        self.max_character_per_option = max_character_per_option
        self.number_pages = math.ceil(len(options_list) / (option_per_column * rows_per_page))
        self.max_index = option_per_column * rows_per_page * self.number_pages
        self.character_per_column = len(CURSOR_VALUES[False]) * option_per_column + max_character_per_option * option_per_column + 1
        self.option_cutoff_point = max_character_per_option - len(DEFAULT_CHARACTERS["CharacterOverflow"])
        self.options_list = self.options_list_processing(options_list)


    def options_list_processing(self, input_option_list: list[str]):
        # Ajuste del tamaño de la lista para que no alla coordenadas sin referenciar a opciones y
        # Ajuste del largo de las opciones para que la cuadrícula del menú quede ordenada
        adjust_list_options = []
        list_size = len(input_option_list)
        for n in range(self.max_index):
            if n < list_size:
                option = input_option_list[n]
            else:
                option = ""

            size_option = len(option)
            if size_option <= self.max_character_per_option:
                adjust_list_options.append(option +
                                              DEFAULT_CHARACTERS["SpaceCharacter"] *
                                              (self.max_character_per_option - size_option))
            else:
                adjust_list_options.append(option[:self.option_cutoff_point] +
                                              DEFAULT_CHARACTERS["CharacterOverflow"])

        # Procesado de lista para que la indexación de esta se apegue más el sistema de coordenadas implementado
        options_list_processed = []
        i = 0
        for page in range(self.number_pages):
            options_list_processed.append([])
            for row in range(self.rows_per_page):
                options_list_processed[page].append([])

                # Limite de fila
                options_list_processed[page][row].append(DEFAULT_CHARACTERS["RowLimit"])

                # Ingresa el cursor y las opciones de una fila
                for column in range(self.option_per_column):
                    options_list_processed[page][row].append(CURSOR_VALUES[False])
                    options_list_processed[page][row].append(adjust_list_options[i])
                    i += 1

                # Ingresa la Scroll-Bar a la fila
                options_list_processed[page][row].append(DEFAULT_CHARACTERS["ScrollBarValues"][True])
                # Limite de fila
                options_list_processed[page][row].append(DEFAULT_CHARACTERS["RowLimit"])


        return options_list_processed


    # Funciones de construcción de menú
    def menu_crafter(self, mode="solo"):
        def mode_menu_crafter(input_row: str):
            if mode == "solo":
                print(input_row)
            elif mode == "display":
                menu_list.append(input_row)
            else:
                print("ERROR: En la función menu_crafter; Modo no válido")
        def menu_limit_row_crafter():
            return (DEFAULT_CHARACTERS["MenuCorner"] +
                    DEFAULT_CHARACTERS["MenuLimitRowBody"] * self.character_per_column +
                    DEFAULT_CHARACTERS["MenuCorner"])
        def separator_row_crafter():
            return (DEFAULT_CHARACTERS["RowLimit"] +
                    DEFAULT_CHARACTERS["MenuLimitRowBody"] * self.character_per_column +
                    DEFAULT_CHARACTERS["RowLimit"])
        def empty_row_crafter():
            return (DEFAULT_CHARACTERS["RowLimit"] +
                    DEFAULT_CHARACTERS["BodyEmptyRow"] * (self.character_per_column - 1) +
                    DEFAULT_CHARACTERS["ScrollBarValues"][True] +
                    DEFAULT_CHARACTERS["RowLimit"])
        def title_row_crafter():
            return (DEFAULT_CHARACTERS["RowLimit"] +
                    self.title_menu.center(self.character_per_column) +
                    DEFAULT_CHARACTERS["RowLimit"])


        menu_list = []
        coord_page = self.cursor_coordinates[0]
        coord_row = self.cursor_coordinates[1]

        for n in range(5):
            if n == 1:
                mode_menu_crafter(title_row_crafter())
            elif n == 2:
                mode_menu_crafter(separator_row_crafter())
            elif n == 3:
                for row in range(self.rows_per_page):
                    show_list_options = self.options_list[coord_page][row].copy()

                    mode_menu_crafter(empty_row_crafter())
                    if self.activated and self.type_menu and row == coord_row:
                        show_list_options[self.column_object_index(mode="cursor")] = CURSOR_VALUES[True]

                    mode_menu_crafter("".join(show_list_options))

            else:
                mode_menu_crafter(menu_limit_row_crafter())

        if mode == "solo":
            return None
        elif mode == "display":
            return menu_list
        else:
            return print("ERROR: En la función menu_crafter; Modo no válido")


    def change_coordinate_cursor(self, input_user: str):
        def coordinate_system(last_coord: list[int], limit_coord: list[int]):
            coord_z = 0
            coord_y = 1
            coord_x = 2

            if input_user.upper() == "W":
                add_coord = (0, -1, 0)
            elif input_user.upper() == "S":
                add_coord = (0, 1, 0)
            elif input_user.upper() == "A":
                add_coord = (0, 0, -1)
            elif input_user.upper() == "D":
                add_coord = (0, 0, 1)
            else:
                coord_add = last_coord
                return coord_add

            for n in range(len(last_coord)):
                last_coord[n] += add_coord[n]

            last_coord[coord_x] %= limit_coord[coord_x]

            if last_coord[coord_y] < 0 or last_coord[coord_y] >= limit_coord[coord_y]:
                last_coord[coord_z] += add_coord[coord_y]

            last_coord[coord_y] %= limit_coord[coord_y]
            last_coord[coord_z] %= limit_coord[coord_z]

            return last_coord

        self.cursor_coordinates = coordinate_system(self.cursor_coordinates,
                                                    [self.number_pages, self.rows_per_page,
                                                     self.option_per_column])


    def column_object_index(self, mode="option"):
        match mode:
            case "cursor": return 2 * (self.cursor_coordinates[2] + 1) - 1
            case "option": return 2 * (self.cursor_coordinates[2] + 1)
            case "ScrollBar": return 2 * self.option_per_column + 1
            case _: return -1


    def select_option(self):
        coord_page = self.cursor_coordinates[0]
        coord_row = self.cursor_coordinates[1]
        return self.cursor_coordinates, self.options_list[coord_page][coord_row][self.column_object_index()]


