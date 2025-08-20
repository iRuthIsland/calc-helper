from flet.core.image import Image

from Components import logger, View


import flet as ft



class Results(View):
    def __init__(self, page: ft.Page, callback, passed, failed):
        logger.addLog(f'{__name__}.__init__: +{passed} <=> -{failed})')

        # vars -----
        self.__passed = passed
        self.__failed = failed

        # view -----
        # ok
        self.__button_ok = None

        super().__init__(page=page, name='Results', callback=callback)
        pass


    @property
    def stars(self):
        logger.addLog(f'{__name__}.stars')
        stars = 5  # max qty of stars
        tot_stars = self.__passed / (self.__passed + self.__failed) * stars  # stars
        int_stars = int(tot_stars)
        rem_stars = tot_stars - int_stars
        sign = ''
        if rem_stars > 0.75:  # (0.75 .. 1.00)
            int_stars += 1
        elif rem_stars > 0.25:  # (0.25 .. 0.75]
            sign = '+'
        return f'{int_stars}{sign}'


    @property
    def _layout(self):
        logger.addLog(f'{__name__}._layout')

        # results ##################################################################################################
        result_color = {
            '0': '#ff0d0d',  # red (Candy Apple Red)
            '0+': '#ff0d0d',  # red (Candy Apple Red)
            #
            '1': '#ff4e11',  # red/orange (Orioles Orange)
            '1+': '#ff4e11',  # red/orange (Orioles Orange)
            #
            '2': '#ff8e15',  # orange (Beer)
            '2+': '#ff8e15',  # orange (Beer)
            #
            '3': '#fab733',  # yellow (Saffron)
            '3+': '#fab733',  # yellow (Saffron)
            #
            '4': '#acb334',  # light green (Brass)
            '4+': '#69b34c',  # green (Apple)
            #
            '5': '#0D5B11'  # dark green (Royal Green)
        }[self.stars]

        # buttons ######################################################################################################

        # buttons/button.back ------------------------------------------------------------------------------------------
        self.__button_ok = ft.Button(
            text='Ok',
            height=50, width=150, bgcolor='#cccccc',  # light-grey
            on_click=lambda e: self.__button_clicked(button=self.__button_ok)
        )

        # layout #######################################################################################################
        return (
            ft.Column([
                ft.Row(
                    [
                        ft.Text(
                            value='Rezultat',
                            size=25, weight=ft.FontWeight.BOLD, color=result_color,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Image(
                                    src=f"/images/total.png",
                                    height=100
                                ),
                                ft.Text(
                                    value=f'{self.__passed + self.__failed}',
                                    size=40, color='#1a8cff',  # blue
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Column(
                            [
                                ft.Image(
                                    src=f"/images/passed.png",
                                    height=100
                                ),
                                ft.Text(
                                    value=f'{self.__passed}',
                                    size=40, color='#39ac73',  # dark-green
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Column(
                            [
                                ft.Image(
                                    src=f"/images/failed.png",
                                    height=100
                                ),
                                ft.Text(
                                    value=f'{self.__failed}',
                                    size=40, color='#c85151',  # dark-red
                                    text_align=ft.TextAlign.CENTER
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        ft.Column(
                            [
                                ft.Stack(
                                    [
                                        Image(
                                            src="/images/star.png",
                                            height=190
                                        ),
                                        ft.Text(
                                            value=self.stars,
                                            size=75, color=result_color,
                                            style=ft.TextStyle(
                                                shadow=ft.BoxShadow(
                                                    spread_radius=1,
                                                    blur_radius=15,
                                                    color=ft.Colors.BLUE_GREY_300,
                                                    offset=ft.Offset(0, 0),
                                                    blur_style=ft.ShadowBlurStyle.OUTER,
                                                )
                                            ),
                                            text_align=ft.TextAlign.CENTER
                                        )
                                    ],
                                    alignment=ft.alignment.center
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND
                ),
                ft.Row(
                    [
                        self.__button_ok
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ])
        )


    def __button_clicked(self, button):
        logger.addLog(f'{__name__}.__button_clicked: button={button.text}')

        if button == self.__button_ok:
            self._hide()
            self._callback()
        else:
            raise Exception(f'Unknown button {button}')

        pass


    pass
