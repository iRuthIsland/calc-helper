from .Logger import logger

import flet as ft



class View:
    def __init__(self, page: ft.Page, name=None, callback=None):
        logger.addLog(f'{__name__}({name}).__init__')

        # default -----
        if name is None:
            name = 'unknown'

        if callback is None:
            def none(): pass
            callback = none

        # vars -----
        self.__page = page
        self.__callback = callback
        self.__name = name

        # layout -----
        # layout components to be declared here

        self._show()
        pass


    @property
    def _page(self):
        logger.addLog(f'{__name__}({self.__name})._page')
        return self.__page


    @property
    def _callback(self):
        logger.addLog(f'{__name__}({self.__name})._callback')
        return self.__callback


    @property
    def _layout(self):
        logger.addLog(f'{__name__}({self.__name})._layout')
        # layout components to be coded here
        return ft.View()


    def _show(self):
        logger.addLog(f'{__name__}({self.__name})._show')
        self.__page.add(
            self._layout
        )
        self.__page.update()
        pass


    def _hide(self):
        logger.addLog(f'{__name__}({self.__name})._hide')
        self.__page.clean()
        pass


    def _refresh(self):
        logger.addLog(f'{__name__}({self.__name})._refresh')
        self._hide()
        self._show()
        pass


    def _close(self):
        logger.addLog(f'{__name__}({self.__name})._close')
        self.__page.window.close()


    pass
