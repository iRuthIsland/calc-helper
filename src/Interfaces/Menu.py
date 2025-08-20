from Components import logger, View

from .Add_Sub_Mul_Div import Addition, Subtraction, Multiplication, Division

import flet as ft



class Menu(View):
    def __init__(self, page: ft.Page):
        logger.addLog(f'{__name__}.__init__')

        # layout
        # buttons
        self.__button_addition = None
        self.__button_subtraction = None
        self.__button_multiplication = None
        self.__button_division = None
        self.__button_exit = None

        super().__init__(page=page, name='Menu')
        pass


    @property
    def _layout(self):
        logger.addLog(f'{__name__}._layout')

        # buttons ######################################################################################################
        buttons_height = 50
        buttons_width = 150

        # buttons/button.addition --------------------------------------------------------------------------------------
        self.__button_addition = ft.Button(
            text='Adunare', bgcolor='#99ccff',  # blue
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_addition)
        )

        # buttons/button.subtraction -----------------------------------------------------------------------------------
        self.__button_subtraction = ft.Button(
            text='Scădere', bgcolor='#99ccff',  # blue
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_subtraction)
        )

        # buttons/button.multiplication --------------------------------------------------------------------------------
        self.__button_multiplication = ft.Button(
            text='Înmulţire', bgcolor='#99ccff',  # blue
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_multiplication)
        )

        # buttons/button.division --------------------------------------------------------------------------------------
        self.__button_division = ft.Button(
            text='Împărţire', bgcolor='#99ccff',  # blue
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_division)
        )

        # buttons/button.exit ------------------------------------------------------------------------------------------
        self.__button_exit = ft.Button(
            text='Ieșire', bgcolor='#cccccc',  # grey
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_exit)
        )

        # layout
        return (
            ft.Column([
                self.__button_addition,
                self.__button_subtraction,
                self.__button_multiplication,
                self.__button_division,
                self.__button_exit
            ])
        )


    def __button_clicked(self, button):
        logger.addLog(f'{__name__}.__button_clicked: button={button.text}')

        if button == self.__button_exit:
            self._close()
        else:
            self._hide()
            {
                self.__button_addition: Addition,
                self.__button_subtraction: Subtraction,
                self.__button_multiplication: Multiplication,
                self.__button_division: Division
            }[button](page=self._page, callback=self._show)
        pass


    pass
