from Components import logger
from Interfaces import Menu

import flet as ft
import logging



def app(page: ft.Page):
    page.title = 'Calc-Helper'
    page.window.width = 800
    page.window.height = 360
    page.window.center()

    Menu(page=page)
    pass



if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    logger.open()
    ft.app(target=app)
    logger.close()
