#!/usr/bin/env python3
#coding=utf-8


# standart modules imports
import sys

# pyqt imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class AtomicWidget(QLineEdit):
    def __init__(self):
        super.__init__()
