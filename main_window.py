#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from image_button import *

import sys
import resources

class MainWindow(QMainWindow):
    '''this class creates a main window to show the menu'''

    def __init__(self):
        super().__init__()

    def create_main_window_layout(self):

        #set QWidget class
        self.main_window_widget = QWidget()

        #set background picture by QLabel
        self.main_background_pixmap = QPixmap(':/main_background.png')
        self.main_background_pixmap.setDevicePixelRatio(2)
        self.main_background = QLabel(self.main_window_widget)
        self.main_background.setPixmap(self.main_background_pixmap)
        self.main_background.setGeometry(0, 0, 960, 540)

        #set the background label of main button
        self.main_button_background_pixmap = QPixmap(':/main_button_background.png')
        self.main_button_background_pixmap.setDevicePixelRatio(2)
        self.main_button_background = QLabel(self.main_window_widget)
        self.main_button_background.setPixmap(self.main_button_background_pixmap)
        self.main_button_background.setGeometry(710, 0, 250, 540)

        #create all the buttons
        #create a strat button
        self.main_start_button = ImageButton('main_start', self.main_window_widget)
        self.main_start_button.setGeometry(755, 45, 160, 55)

        #create a load button
        self.main_load_button = ImageButton('main_load', self.main_window_widget)
        self.main_load_button.setGeometry(755, 145, 160, 55)

        #create a extra button
        self.main_extra_button = ImageButton('main_extra', self.main_window_widget)
        self.main_extra_button.setGeometry(755, 245, 160, 55)

        #create a config button
        self.main_config_button = ImageButton('main_config', self.main_window_widget)
        self.main_config_button.setGeometry(755, 345, 160, 55)

        #create a exit button
        self.main_exit_button = ImageButton('main_exit', self.main_window_widget)
        self.main_exit_button.setGeometry(755, 445, 160, 55)