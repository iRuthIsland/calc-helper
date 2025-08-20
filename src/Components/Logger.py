# -*- coding: utf-8 -*-
from config import config
from datetime import datetime



class Logger:
    __slots__ = ('__file', '__isOpen', '__logFile')

    def __init__(self, file=None):
        if file is None:
            file = config.logger.file
        self.__file = file
        self.__isOpen = False
        self.__logFile = None
        pass


    @property
    def isOpen(self):
        return self.__isOpen


    def open(self):
        if not self.isOpen:
            self.__isOpen = True
            self.__logFile = open(file=self.__file, mode='w', encoding="utf-8")
        pass


    def addLog(self, message=None):
        if message is None:
            message = ''

        if self.isOpen and config.logger.debug:
            self.__logFile.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} {message}\n')
            self.__logFile.flush()
        pass


    def close(self):
        if self.isOpen:
            self.__logFile.close()
            self.__isOpen = False
        pass


    pass


logger = Logger()
