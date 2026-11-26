from random import random

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QCheckBox
from PyQt6.QtGui import QIntValidator, QDoubleValidator

import sys
import rollerui
import itemrollerui
import damagecalcui


class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P5X Tools")

        self.theRollerWindow = rollerui.RollerWindow()
        self.RollerSelect = QPushButton()
        self.RollerSelect.setText("Character Roll Simulator")
        self.RollerSelect.clicked.connect(self.openRollerWindow)

        self.theRollerItemWindow = itemrollerui.ItemRollerWindow()
        self.RollerItemSelect = QPushButton()
        self.RollerItemSelect.setText("Weapon Roll Simulator")
        self.RollerItemSelect.clicked.connect(self.openItemRollerWindow)

        self.theDamageWindow = damagecalcui.DamageCalcWindow()
        self.DamageSelect = QPushButton()
        self.DamageSelect.setText("Damage Calculator (Not Accurate)")
        self.DamageSelect.clicked.connect(self.openDamageWindow)

        #self.input = QLineEdit()
        #self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.RollerSelect)
        layout.addWidget(self.RollerItemSelect)
        layout.addWidget(self.DamageSelect)
        #layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def openRollerWindow(self):
        self.theRollerWindow.show()

    def openDamageWindow(self):
        self.theDamageWindow.show()

    def openItemRollerWindow(self):
        self.theRollerItemWindow.show()


app = QApplication(sys.argv)

window = MainMenuWindow()
window.show()

app.exec()