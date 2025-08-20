# -*- coding: utf-8 -*-
from .Logger import logger

from threading import Thread
from time import sleep



class Timer:
    def __init__(self):
        logger.addLog(f'{__name__}.__init__')

        self.__timing = None
        self.__step_callback = None
        self.__end_callback = None

        self.__thread = None
        self.__isActive = False
        self.__remain = None
        pass


    @property
    def remain(self):
        return self.__remain


    def start(self, timing=None, step_callback=None, end_callback=None):
        logger.addLog(f'{__name__}.start: timing={timing})')

        # params -> default -----
        if timing is None:
            timing = 0

        def none(): pass

        if step_callback is None:
            step_callback = none

        if end_callback is None:
            end_callback = none

        # params -> set -----
        self.__timing = timing
        self.__step_callback = step_callback
        self.__end_callback = end_callback

        # init -----
        self.__isActive = True
        self.__thread = Thread(target=self.__step)
        self.__thread.start()
        pass


    def stop(self):
        logger.addLog(f'{__name__}.stop')

        self.__isActive = False
        pass


    def restart(self):
        logger.addLog(f'{__name__}.restart')

        self.stop()
        self.start(
            timing=self.__timing,
            step_callback=self.__step_callback,
            end_callback=self.__end_callback
        )
        pass


    def __step(self):
        logger.addLog(f'{__name__}.__step')

        self.__remain = self.__timing

        while self.__remain > 0 and self.__isActive:
            logger.addLog(f'{__name__}.__step: {self.__remain}')
            sleep(1)
            self.__remain -= 1
            self.__step_callback()

        logger.addLog(f'{__name__}.__step: {self.__remain} - time expired!')

        logger.addLog(f'{__name__}.__step: act={self.__isActive}')
        if self.__isActive:
            self.__end_callback()

        pass


    def __del__(self):
        logger.addLog(f'{__name__}.__del__')

        self.stop()
        pass

    pass
