from config import config
from Components import logger, View, Timer

from ..Types import Types
from .Results import Results

import flet as ft
from random import randint



class Repeat(View):
    def __init__(self, page: ft.Page, callback, selected, minLevel, maxLevel):
        logger.addLog(f'{__name__}.__init__: {selected}({minLevel}..{maxLevel})')

        # vars -----
        self.__selected = selected
        self.__minLevel = minLevel
        self.__maxLevel = maxLevel

        self.__timing = (
            config.values[
                {
                    Types.add: 'add_sub',
                    Types.sub: 'add_sub',
                    Types.mul: 'mul_div',
                    Types.div: 'mul_div'
                }[self.__selected]
            ]['repeat']['timing']
        )
        self.__timer = Timer()

        self.__exercises = []
        self.__ok = 0
        self.__fail = 0

        # view -----
        # statistics
        self.__timer_text = None
        self.__result_total_text = None
        self.__result_ok_text = None
        self.__result_fail_text = None
        # exercises
        self.__exercise_text = None
        self.__result_textField = None
        self.__result_text = None
        self.__button_ok = None
        self.__button_next = None
        # buttons
        self.__button_back = None

        super().__init__(page=page, name='Repeat', callback=callback)
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
            end_callback=lambda: self.__button_clicked(button=self.__button_ok)
        )

        # statistics/result-total --------------------------------------------------------------------------------------
        self.__result_total_text = ft.Text(
            value=f'Total: {self.__ok + self.__fail}',
            size=20, color='#1a8cff',  # blue
            text_align=ft.TextAlign.LEFT
        )

        # statistics/result-ok -----------------------------------------------------------------------------------------
        self.__result_ok_text = ft.Text(
            value=f'Corect: {self.__ok}',
            size=20, color='#39ac73',  # dark-green
            text_align=ft.TextAlign.LEFT
        )

        # statistics/result-fail ---------------------------------------------------------------------------------------
        self.__result_fail_text = ft.Text(
            value=f'Greşit: {self.__fail}',
            size=20, color='#c85151',  # dark-red
            text_align=ft.TextAlign.LEFT
        )

        # exercises ####################################################################################################

        # exercises/exercise -> prepare
        exercise, result = self.__exercise_prepare()

        # exercises/exercise -------------------------------------------------------------------------------------------
        self.__exercise_text = ft.Text(
            value=f'{exercise}=',
            size=120, color='#0066cc',  # dark-blue
            text_align=ft.TextAlign.LEFT
        )

        # exercises/result-input ----------------------
        self.__result_textField = ft.CupertinoTextField(
            text_size=120, color='#0066cc',  # dark-blue
            height=175, width=200,
            text_align=ft.TextAlign.CENTER,
            autofocus=True,
            on_submit=lambda e: self.__button_clicked(button=self.__button_ok)
        )

        # exercises/result-text ----------------------
        self.__result_text = ft.Text(
            value='',
            size=20, color='#0066cc',  # dark-blue
            text_align=ft.TextAlign.CENTER
        )

        # exercises/buttons ============================================================================================

        # exercises/button.ok ------------------------------------------------------------------------------------------
        self.__button_ok = ft.Button(
            text='Ok',
            height=50, width=50, color='#39ac73',  # dark-green
            on_click=lambda e: self.__button_clicked(button=self.__button_ok)
        )

        # exercises/button.next ----------------------------------------------------------------------------------------
        self.__button_next = ft.Button(
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
                ft.Stack([
                    ft.Row(
                        [
                            self.__timer_text
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            self.__result_total_text,
                            self.__result_ok_text,
                            self.__result_fail_text
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ]),
                ft.Row(
                    [
                        self.__exercise_text,
                        self.__result_textField,
                        ft.Stack([
                            ft.Container(
                                content=ft.Row(
                                    [
                                        self.__button_ok,
                                        self.__button_next
                                    ]
                                ),
                                height=175, alignment=ft.alignment.center
                            ),
                            ft.Container(
                                content=self.__result_text,
                                height=175, alignment=ft.alignment.bottom_center
                            )
                        ])
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
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
            if button == self.__button_ok:
                self.__timer.stop()

                self.__result_textField.read_only = True

                self.__button_ok.disabled = True
                self.__button_ok.color = '#999999'  # grey
                self.__button_ok.update()

                self.__button_next.disabled = False
                self.__button_next.color = '#39ac73'  # dark-green
                self.__button_next.update()

                # generated -----
                last = len(self.__exercises) - 1
                exercise = self.__exercises[last][0]
                result = self.__exercises[last][1]

                # entered -----
                result_input = self.__result_textField.value
                try:
                    result_input = int(result_input)
                except:
                    pass

                # log results -----
                logger.addLog(f'\t\t\t#> ex[{last}]:\t{exercise}\t{result} >> {result_input}')

                # view update
                self.__result_text.value = f'{result}'
                self.__result_text.color = '#009900'  # green
                self.__result_text.update()

                if result_input == result:
                    result_bgcolor = '#b3ffb3'  # light-green
                    self.__ok += 1
                    self.__result_ok_text.value = f'Corect: {self.__ok}'
                    self.__result_ok_text.update()

                else:
                    result_bgcolor = '#ff6666'  # light-red
                    self.__fail += 1
                    self.__result_fail_text.value = f'Greşit: {self.__fail}'
                    self.__result_fail_text.update()

                self.__result_total_text.value = f'Total: {self.__ok + self.__fail}'
                self.__result_total_text.update()

                self.__result_textField.bgcolor = result_bgcolor
                self.__result_textField.update()

            elif button == self.__button_next:
                if self.__ok + self.__fail < (
                        config.values[
                            {
                                Types.add: 'add_sub',
                                Types.sub: 'add_sub',
                                Types.mul: 'mul_div',
                                Types.div: 'mul_div'
                            }[self.__selected]
                        ]['repeat']['qty']
                ):
                    self._refresh()
                else:
                    self._hide()
                    Results(
                        page=self._page, callback=self._callback,
                        passed=self.__ok, failed=self.__fail
                    )

            else:
                raise Exception(f'Unknown button {button}')

        pass


    def __timer_refresh(self):
        logger.addLog(f'{__name__}.__timer_refresh')

        try:
            remain = self.__timer.remain

            if remain >= 0:
                if remain > 0.75 * self.__timing:
                    timer_color = '#1f7a1f'  # timer/green
                elif remain > 0.5 * self.__timing:
                    timer_color = '#e6b800'  # timer/yellow
                elif remain > 0.25 * self.__timing:
                    timer_color = '#ff9933'  # timer/orange
                else:
                    timer_color = '#b32d00'  # timer/red

                self.__timer_text.value = f'Timp: {remain}'
                self.__timer_text.color = timer_color
                self.__timer_text.update()

        except Exception as error:
            logger.addLog(f'{__name__}.__timer_refresh: err={error}')
            self.__timer.stop()
        pass


    def __exercise_prepare(self):
        logger.addLog(f'{__name__}.__exercise_prepare')

        def generate_exercise():
            n1 = randint(
                a=self.__minLevel,
                b=self.__maxLevel
            )
            n2 = randint(
                a=self.__minLevel,
                b=self.__maxLevel
            )
            logger.addLog(f'{__name__}.__exercise_prepare: ({n1},{n2})')

            return {
                # Types.add:(f'{n2     }+{n1}', n2 + n1),
                # Types.sub:(f'{n2 + n1}-{n1}', n2     ),
                # Types.mul:(f'{n2     }x{n1}', n2 * n1),
                # Types.div:(f'{n2 * n1}:{n1}', n2     )
                Types.add:  (f'{n1     }+{n2}', n1 + n2),
                Types.sub:  (f'{n1 + n2}-{n1}',      n2),
                Types.mul:  (f'{n1     }x{n2}', n1 * n2),
                Types.div:  (f'{n1 * n2}:{n1}',      n2)
            }[self.__selected]


        # init -----
        exercise, result = generate_exercise()

        i = 0
        while (exercise, result) in self.__exercises and i < 5:
            exercise, result = generate_exercise()
            i += 1

        self.__exercises.append((exercise, result))
        return exercise, result


    pass
