"""
This module allows the creation of different interactive menus

Example:
    Shortest way to print the interactive menu in the terminal.
    For the three int entered as args
    (3, 4, 5) (Option per Column, Options Rows, Number char per option).

    >>> test_menu = Menu("test_menu", 3, 4, 5,
    ...                  [
    ...                      "test", ":", "menu",
    ...                      "test", ":", "menu",
    ...                      "test", ":", "menu",
    ...                      "test", ":", "menu",
    ...                  ])
    >>> test_menu.menu_crafter()
    +-------------------------+
    |        test_menu        |
    |-------------------------|
    |                         |
    | > test    :       menu  |
    |                         |
    |   test    :       menu  |
    |                         |
    |   test    :       menu  |
    |                         |
    |   test    :       menu  |
    +-------------------------+
"""
from math import ceil

DEFAULT_CHARACTERS = {
    "cursor_values": ("   ", " > "),
    "BodyEmptyRow": " ",
    "RowLimit": "|",
    "MenuLimitRowBody": "-",
    "MenuCorner": "+",
    "CharacterOverflow": "...",
    "SpaceCharacter": " ",
    "ScrollBarValues": ("\x1b[48;5;0m\x1b[0m ", "\x1b[48;5;255m \x1b[0m")
}


# HotKeys
MOVE_UP = "W"
MOVE_DOWN = "S"
MOVE_LEFT = "A"
MOVE_RIGHT = "D"


class Menu:
    """
    Class that provides methods for creating and interacting with the menu.

    Attributes:
        _type_menu : bool
                    If you'd want a menu dynamic (True) or static (False)
        activated : bool
                    Allows interaction with the menu when True.
        _title_menu : str
        _cursor_coordinates : list[int, int, int]
                             It saves the cursor position.
        _option_per_column : int
        _options_rows_per_page : int
        _character_per_option : int
        _number_pages : int
        _max_index : int
                    The maximum options number that complete the menu.
        _characters_per_row : int
                             Rows size in char number.
        _option_cutoff_point : int
                              Cutoff point of an option exceeds the maximum char number.
        _options_list : list[str]
                       Post-processed list of an input list.
    """


    def __init__(self, title_menu: str, option_per_column: int,
                 rows_per_page: int, character_per_option: int,
                 options_list: list[str], dynamic_static_menu: bool = True):
        """
        Instance initialization

        Parameters:
            title_menu : str
            option_per_column : int
            rows_per_page : int
            character_per_option : int
            options_list : list[str]
                           List with all the options in str format for the menu.
            dynamic_static_menu : bool, default=True
        """
        def _options_list_processing(input_options_list: list[str]):
            """
            Process the ``input_options_list``, so that useful in class

            This adds empty options to the input list for complete the menu,
            adjusts the char width of the options
            and changes the indexing of the list to fit the coordinate system this class.
            """

            def check_width_options(str_option):
                size_option = len(str_option)
                if size_option <= self._character_per_option:
                    return (str_option
                            + " "
                            + DEFAULT_CHARACTERS["SpaceCharacter"]
                            * (self._character_per_option - size_option))
                else:
                    return (str_option[:self._option_cutoff_point]
                            + DEFAULT_CHARACTERS["CharacterOverflow"]
                            + " ")


            list_size = len(input_options_list)
            # Fill the entire menu with options.
            adjust_list_options = input_options_list + [""] * (self._max_index - list_size)

            # Create columns
            options_list_processed = []
            for option in adjust_list_options:
                # Add cursor
                options_list_processed.append(DEFAULT_CHARACTERS["cursor_values"][False])
                # Adjust the width of the options.
                options_list_processed.append(check_width_options(option))


            # Structural change of list to approach the coord system.
            # Create rows
            create_rows = []
            for i in range(0, len(options_list_processed), self._option_per_column * 2):
                # Add Row Options
                row_list = options_list_processed[i : i + self._option_per_column * 2]
                # Add BorderRow
                row_list.insert(0, DEFAULT_CHARACTERS["RowLimit"])
                # Add ScrollBar
                row_list.append(DEFAULT_CHARACTERS["ScrollBarValues"][True])
                # Add BorderRow
                row_list.append(DEFAULT_CHARACTERS["RowLimit"])
                # Row
                create_rows.append(row_list)

            # Add Rows to Menu
            options_list_processed = create_rows.copy()

            del adjust_list_options, list_size, create_rows, row_list, i


            # Create Pages
            create_pages = []
            for i in range(0, len(options_list_processed), self._options_rows_per_page):
                create_pages.append(options_list_processed[i : i + self._options_rows_per_page])

            return create_pages


        # Verifications
        assert option_per_column > 0, "option_per_column must be greater than 0"
        assert rows_per_page > 0, "rows_per_page must be greater than 0"
        assert character_per_option > len(DEFAULT_CHARACTERS["CharacterOverflow"]), (
            "character_per_option must be greater than {}"
            .format(len(DEFAULT_CHARACTERS["CharacterOverflow"])))

        assert options_list != [], "The list cannot be empty"


        # Menu main features
        self._type_menu = dynamic_static_menu
        self.activated: bool = True
        self._title_menu = title_menu
        self._cursor_coordinates: list[int] = [0, 0, 0]

        # Menu structure
        self._option_per_column = option_per_column
        self._options_rows_per_page = rows_per_page
        self._character_per_option = character_per_option
        self._number_pages = ceil((len(options_list)
                                  / (option_per_column * rows_per_page))
                                 )
        self._max_index = option_per_column * rows_per_page * self._number_pages
        self._characters_per_row = (len(DEFAULT_CHARACTERS["cursor_values"][False])
                                    * option_per_column
                                    + (character_per_option + 1)
                                    * option_per_column
                                    + 1)
        self._option_cutoff_point = (character_per_option
                                     - len(DEFAULT_CHARACTERS["CharacterOverflow"]))
        self._options_list: list = _options_list_processing(options_list)


    def menu_crafter(self, mode: str = "solo"):
        """
        Generate `Frame Menu`.

        Parameters:
            mode: str
                  You want a return in list or None with print in terminal.
        Return:
            list | None
                It depends on the value of ``mode``.

        Examples:
            - ``mode="solo"``: Return None; Print in terminal.
            - ``mode="display"``: Return list with menu rows.

        """

        def _mode_menu_generate(input_row: str | tuple[str, ...]):
            """It generate output dependent to you  select mode"""

            if mode == "solo":
                print(input_row)
            elif mode == "display":
                menu_list.append(input_row)
            else:
                pass

        def _set_scrollbar():
            """Create groups of rows that represent the pages for the scrollbar"""

            scrollbar_groups = []
            # How many options rows represents each page? (Total Rows / Total Page)
            # Total Rows = "options rows" + "spaces row"
            # As each type of row is interleaved, the result can be obtained
            # Total Rows = "options rows" * 2
            # rows_group is the size complete group
            # module is the surplus
            rows_group = int(self._options_rows_per_page * 2 / self._number_pages)
            module = self._options_rows_per_page * 2 % self._number_pages

            # Obtain the size of the rows groups by adding the surplus
            n_rows_groups = [rows_group + 1 if page < module else rows_group
                          for page in range(self._number_pages)]

            # Assign the index of the rows that corresponds to each group
            ii = 0
            for page in range(self._number_pages):
                scrollbar_groups.append([])
                for n_rows in range(n_rows_groups[page]):
                    scrollbar_groups[page].append(ii)
                    ii += 1

            return scrollbar_groups

        def _create_row(type_row: str, index_options_row: int = 0):
            """Generate a standard row type"""

            match type_row:
                case "limit":
                    return (DEFAULT_CHARACTERS["MenuCorner"]
                            + DEFAULT_CHARACTERS["MenuLimitRowBody"] * self._characters_per_row
                            + DEFAULT_CHARACTERS["MenuCorner"])
                case "separator":
                    return (DEFAULT_CHARACTERS["RowLimit"]
                            + DEFAULT_CHARACTERS["MenuLimitRowBody"] * self._characters_per_row
                            + DEFAULT_CHARACTERS["RowLimit"])
                case "title":
                    return (DEFAULT_CHARACTERS["RowLimit"]
                            +self._title_menu.center(self._characters_per_row)
                            +DEFAULT_CHARACTERS["RowLimit"])
                case "options":
                    odd = index_options_row % 2

                    # If you are in the row that corresponds to the active page of the scroll-bar
                    scrollbar_value = True if index_options_row in active_scrollbar else False

                    if odd:
                        # Obtain the option row you need
                        row = int(  (index_options_row - 1) / 2  )
                        show_list_options = self._options_list[coord_page][row].copy()

                        # Set the Scroll-Bar value
                        show_list_options[self._column_object_index(mode="ScrollBar")] = \
                            DEFAULT_CHARACTERS["ScrollBarValues"][scrollbar_value]

                        # Set the cursor Value
                        if self.activated and self._type_menu and row == coord_row:
                            show_list_options[self._column_object_index(mode="cursor")] = \
                                DEFAULT_CHARACTERS["cursor_values"][True]

                        return "".join(show_list_options)

                    else:
                        return (DEFAULT_CHARACTERS["RowLimit"]
                                + DEFAULT_CHARACTERS["BodyEmptyRow"] * (self._characters_per_row - 1)
                                + DEFAULT_CHARACTERS["ScrollBarValues"][scrollbar_value]
                                + DEFAULT_CHARACTERS["RowLimit"])

                case _:
                    raise ValueError("Invalid type row")


        steps_to_create_menu = 5
        menu_list = []
        coord_page = self._cursor_coordinates[0]
        coord_row = self._cursor_coordinates[1]

        # Generate menu parts
        for n in range(steps_to_create_menu):
            if n == 1:
                title = _create_row("title")
                _mode_menu_generate(title)
            elif n == 2:
                separator_row = _create_row("separator")
                _mode_menu_generate(separator_row)
            elif n == 3:
                active_scrollbar = _set_scrollbar()[coord_page]
                for c in range(self._options_rows_per_page * 2):
                    options_row = _create_row("options", index_options_row=c)
                    _mode_menu_generate(options_row)

            else:
                limit_row = _create_row("limit")
                _mode_menu_generate(limit_row)

        # Generate Returns
        if mode == "solo":
            return None
        elif mode == "display":
            return menu_list
        else:
            raise ValueError("Invalid mode")


    def change_coordinate_cursor(self, input_user: str):
        """
        Update coord with ``input_user``

        Parameters:
             input_user : str
        """

        limit_coord = [self._number_pages,
                       self._options_rows_per_page,
                       self._option_per_column]

        coord_z = 0
        coord_y = 1
        coord_x = 2

        # Obtain the coord value change
        if input_user.upper() == MOVE_UP:
            add_coord = (0, -1, 0)
        elif input_user.upper() == MOVE_DOWN:
            add_coord = (0, 1, 0)
        elif input_user.upper() == MOVE_LEFT:
            add_coord = (0, 0, -1)
        elif input_user.upper() == MOVE_RIGHT:
            add_coord = (0, 0, 1)
        else:
            return

        # sum the last coord
        self._cursor_coordinates = list(
            map(lambda x, y: x + y, self._cursor_coordinates, add_coord)
        )

        # Refactor with the coord limit
        self._cursor_coordinates[coord_x] %= limit_coord[coord_x]

        if self._cursor_coordinates[coord_y] < 0 or self._cursor_coordinates[coord_y] >= limit_coord[coord_y]:
            self._cursor_coordinates[coord_z] += add_coord[coord_y]

        self._cursor_coordinates[coord_y] %= limit_coord[coord_y]
        self._cursor_coordinates[coord_z] %= limit_coord[coord_z]


    def _column_object_index(self, mode="option"):
        """
        You access to element into the column, selected by coord number.

        Parameters:
            mode : str, default="option"

        Return:
            int
                this is the column index of the menu.

        Examples:
            - ``mode="cursor"``: Return index `Cursor` selected by coord number.
            - ``mode="option"``: Return index `Option` selected by coord number.
            - ``mode="ScrollBar"``: Return index `ScrollBar in the row.
        """

        match mode:
            case "cursor": return 2 * (self._cursor_coordinates[2] + 1) - 1
            case "option": return 2 * (self._cursor_coordinates[2] + 1)
            case "ScrollBar": return 2 * self._option_per_column + 1
            case _:
                example_doc = self._column_object_index.__doc__
                example_doc = example_doc[example_doc.find("Examples") - 1:]
                raise ValueError("You select a valid mode." + "\n" +  example_doc)


    def select_option(self):
        """Return the coord and the name of the option"""

        coord_page = self._cursor_coordinates[0]
        coord_row = self._cursor_coordinates[1]
        return self._cursor_coordinates, self._options_list[coord_page][coord_row][self._column_object_index()]

