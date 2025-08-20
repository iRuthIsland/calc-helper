from flet.core.control import Control
from flet.core.control_event import ControlEvent
from flet.core.types import ControlEventType

from config import config
from Components import logger, View

from .Types import Types
from .Actions import Check, Learn, Repeat

import flet as ft



class Add_Sub_Mul_Div(View):
    def __init__(self, page: ft.Page, callback, selected):
        logger.addLog(f'{__name__}({selected}).__init__')

        # validate -----
        if selected not in (Types.add, Types.sub, Types.mul, Types.div):
            raise Exception(f'Unknown parameter value selected={selected}')

        # vars -----
        self.__selected = selected

        # layout -----
        # learn & check =====
        self.__button_learn = None
        self.__button_check = None
        # levels/level
        self.__level_slider = None
        # repeat =====
        self.__button_repeat = None
        # levels/min-max
        self.__level_rangeSlider = None
        # buttons =====
        self.__button_back = None

        super().__init__(page=page, name='Add_Sub_Mul_Div', callback=callback)
        pass


    @property
    def _layout(self):
        logger.addLog(f'{__name__}({self.__selected})._layout')

        # sec:learn&check ##############################################################################################
        buttons_height = 50
        buttons_width = 150

        # sec:learn&check/button.learn ---------------------------------------------------------------------------------
        self.__button_learn = ft.Button(
            text='Învăţare', bgcolor='#ff9999',  # red
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_learn)
        )

        # sec:learn&check/button.check ---------------------------------------------------------------------------------
        self.__button_check = ft.Button(
            text='Verificare', bgcolor='#ffffb3',  # yellow
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_check)
        )

        # lvl:level ----------------------------------------------------------------------------------------------------
        self.__level_slider = ft.Slider(
            min=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['min']
            ),
            max=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['max']
            ),
            divisions=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['max']
                - config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['min']
            ),
            value=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['default']['level']
            ),
            label='{value}', round=0,
            #active_color='#e0e0e0', inactive_color='#e0e0e0',
            width=450,
            on_change=lambda e: self.__slider_value_changed(slider=self.__level_slider)
        )

        # sec:repeat ###################################################################################################
        buttons_height = 50
        buttons_width = 150

        # sec:repeat/button.repeat -------------------------------------------------------------------------------------
        self.__button_repeat = ft.Button(
            text='Repetare', bgcolor='#adebad',  # green
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_repeat)
        )

        # lvl:min-max --------------------------------------------------------------------------------------------------
        self.__level_rangeSlider = ft.RangeSlider(
            min=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['min']
            ),
            max=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['max']
            ),
            divisions=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['max']
                - config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['min']
            ),
            start_value=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['default']['min']
            ),
            end_value=(
                config.values[
                    {
                        Types.add: 'add_sub',
                        Types.sub: 'add_sub',
                        Types.mul: 'mul_div',
                        Types.div: 'mul_div'
                    }[self.__selected]
                ]['levels']['default']['max']
            ),
            label='{value}', round=0,
            width=450,
            on_change=lambda e: self.__slider_value_changed(slider=self.__level_rangeSlider)
        )

        # sec:back #####################################################################################################
        buttons_height = 50
        buttons_width = 150

        # sec:back/button.back -----------------------------------------------------------------------------------------
        self.__button_back = ft.Button(
            text='Înapoi', bgcolor='#cccccc',
            height=buttons_height, width=buttons_width,
            on_click=lambda e: self.__button_clicked(button=self.__button_back)
        )

        # layout
        return (
            ft.Column([
                ft.Row([
                    ft.Column([
                        self.__button_learn,
                        self.__button_check
                    ]),
                    self.__level_slider
                ]),
                ft.Row([
                    self.__button_repeat,
                    self.__level_rangeSlider
                ]),
                self.__button_back
            ])
        )


    def __button_clicked(self, button):
        logger.addLog(f'{__name__}({self.__selected}).__button_clicked: button={button.text}')

        self._hide()

        if button == self.__button_back:
            self._callback()
        else:
            if button == self.__button_learn:
                Learn(
                    page=self._page,
                    callback=self._show,
                    selected=self.__selected,
                    level=self.__level_slider.value
                )
            elif button == self.__button_check:
                Check(
                    page=self._page,
                    callback=self._show,
                    selected=self.__selected,
                    level=self.__level_slider.value
                )
            elif button == self.__button_repeat:
                Repeat(
                    page=self._page,
                    callback=self._show,
                    selected=self.__selected,
                    minLevel=self.__level_rangeSlider.start_value,
                    maxLevel=self.__level_rangeSlider.end_value
                )
            else:
                raise Exception(f'Unknown button {button}')

        pass


    def __slider_value_changed(self, slider):
        if slider == self.__level_slider:
            slider.value = round(slider.value)

        elif slider == self.__level_rangeSlider:
            slider.start_value = round(slider.start_value)
            slider.end_value = round(slider.end_value)

        else:
            raise Exception(f'Unknown slider {slider}')

    pass
