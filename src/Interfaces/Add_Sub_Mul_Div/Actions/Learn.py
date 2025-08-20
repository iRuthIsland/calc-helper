from config import config
from Components import logger, View, Timer

from ..Types import Types

import flet as ft



class Learn(View):
    def __init__(self, page: ft.Page, callback, selected, level):
        logger.addLog(f'{__name__}.__init__: {selected}({level})')

        # vars -----
        self.__selected = selected
        self.__level = level

        self.__timing = (
            config.values[
                {
                    Types.add: 'add_sub',
                    Types.sub: 'add_sub',
                    Types.mul: 'mul_div',
                    Types.div: 'mul_div'
                }[self.__selected]
            ]['learn']['timing']
        )
        self.__timer = Timer()

        self.__index = 0

        # view -----
        # statistics
        self.__timer_text = None
        # exercises
        self.__button_prev = None
        self.__exercise_text = None
        self.__button_next = None
        # buttons
        self.__button_back = None

        super().__init__(page=page, name='Learn', callback=callback)
        pass


    @property
    def _layout(self):
        logger.addLog(f'{__name__}({self.__selected})._layout')

        # statistics ###################################################################################################

        # statistics/timer ---------------------------------------------------------------------------------------------
        self.__timer_text = ft.Text(
            value=f'Timp: {self.__timing}',
            size=20, color='#1a8cff',  # blue
            text_align=ft.TextAlign.LEFT
        )

        # statistics/timer -> start
        self.__timer.start(
            timing=self.__timing,
            step_callback=lambda: self.__timer_refresh(),
            end_callback=lambda: self.__button_next_enable()
        )

        # exercises ####################################################################################################

        # exercises/button.prev ----------------------------------------------------------------------------------------
        self.__button_prev = ft.ElevatedButton(
            text='<<',
            height=50, width=50, color='#999999' if self.__index == 0 else '#c85151',  # grey or dark-red
            on_click=lambda e: self.__button_clicked(button=self.__button_prev),
            disabled=True if self.__index == 0 else False
        )

        # exercises/exercise -> prepare
        exercise, result = self.__exercise_prepare()

        # exercises/exercise -------------------------------------------------------------------------------------------
        self.__exercise_text = ft.Text(
            value=f'{exercise}={result}',
            size=120, color='#0066cc',  # dark-blue
            text_align=ft.TextAlign.CENTER
        )

        # exercises/button.next ----------------------------------------------------------------------------------------
        self.__button_next = ft.ElevatedButton(
            text='>>',
            height=50, width=50, color='#999999',  # grey
            disabled=True,
            on_click=lambda e: self.__button_clicked(button=self.__button_next)
        )

        # buttons ######################################################################################################

        # buttons/button.back ------------------------------------------------------------------------------------------
        self.__button_back = ft.Button(
            text='Înapoi',
            height=50, width=150, bgcolor='#cccccc',  # light-grey
            on_click=lambda e: self.__button_clicked(button=self.__button_back)
        )

        # layout #######################################################################################################
        return (
            ft.Column([
                ft.Row(
                    [
                        self.__timer_text
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Stack(
                    [
                        ft.Row(
                            [
                                self.__button_prev
                            ],
                            alignment=ft.MainAxisAlignment.START
                        ),
                        ft.Row(
                            [
                                self.__exercise_text
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Row(
                            [
                                self.__button_next
                            ],
                            alignment=ft.MainAxisAlignment.END
                        )
                    ],
                    alignment=ft.alignment.center
                ),
                ft.Row(
                    [
                        self.__button_back
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ])
        )


    def __button_clicked(self, button):
        logger.addLog(f'{__name__}.__button_clicked: button={button.text}')

        if button == self.__button_back:
            self.__timer.stop()
            self._hide()
            self._callback()
        else:
            if button == self.__button_prev:
                self.__timer.stop()

                if self.__index > 0:
                    self.__index -= 1

                if self.__index > 0:
                    if self.__button_prev.disabled:
                        self.__button_prev.disabled = False
                else:
                    if not self.__button_prev.disabled:
                        self.__button_prev.disabled = True

                self._refresh()

            elif button == self.__button_next:
                if self.__index + 1 < (
                    config.values[
                        {
                            Types.add: 'add_sub',
                            Types.sub: 'add_sub',
                            Types.mul: 'mul_div',
                            Types.div: 'mul_div'
                        }[self.__selected]
                    ]['learn']['qty']
                ):
                    self.__index += 1
                    self._refresh()
                else:
                    self._hide()
                    self._callback()

            else:
                raise Exception(f'Unknown button {button}')

        pass


    def __timer_refresh(self):
        logger.addLog(f'{__name__}.__timer_refresh')

        try:
            remain = self.__timer.remain

            if remain >= 0:
                if remain > 0.75 * self.__timing:
                    timer_color = '#b32d00'  # timer/red
                elif remain > 0.5 * self.__timing:
                    timer_color = '#ff9933'  # timer/orange
                elif remain > 0.25 * self.__timing:
                    timer_color = '#e6b800'  # timer/yellow
                else:
                    timer_color = '#1f7a1f'  # timer/green

                self.__timer_text.value = f'Timp: {remain}'
                self.__timer_text.color = timer_color
                self.__timer_text.update()

        except Exception as error:
            logger.addLog(f'{__name__}.__timer_refresh: err={error}')
            self.__timer.stop()
        pass


    def __button_next_enable(self):
        logger.addLog(f'{__name__}.__button_next_enabled')

        if self.__button_next.disabled:
            self.__button_next.disabled = False
            self.__button_next.color = '#39ac73'  # dark-green
            self.__button_next.update()
        pass

    pass


    def __exercise_prepare(self):
        logger.addLog(f'{__name__}.__exercise_prepare')

        n1 = self.__level
        n2 = self.__index
        logger.addLog(f'{__name__}.__exercise_prepare: ({n1},{n2})')

        exercise, result = {
            #Types.add:(f'{n2     }+{n1}', n2 + n1),
            #Types.sub:(f'{n2 + n1}-{n1}', n2     ),
            #Types.mul:(f'{n2     }x{n1}', n2 * n1),
            #Types.div:(f'{n2 * n1}:{n1}', n2     )
            Types.add: (f'{n1     }+{n2}', n1 + n2),
            Types.sub: (f'{n1 + n2}-{n1}', n2     ),
            Types.mul: (f'{n1     }x{n2}', n1 * n2),
            Types.div: (f'{n1 * n2}:{n1}', n2     )
        }[self.__selected]

        return exercise, result


    pass
