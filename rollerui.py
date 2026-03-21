from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QCheckBox
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from random import random # TODO: Remove
import roller

class RollerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rolling Simulator")
        self.numRollslabel = QLabel("Number of Rolls")

        self.numRolls = QLineEdit()
        self.numRollsValidator = QIntValidator()
        self.numRollsValidator.setBottom(0)
        self.numRollsValidator.setTop(1000000000)
        self.numRolls.setValidator(self.numRollsValidator)
        self.numRolls.setText("1000")

        self.numA6NeededLabel = QLabel("Number of Standard Awareness Needed to A6")
        self.numA6Needed = QLineEdit()
        self.numA6Needed.setValidator(QIntValidator())
        self.numA6Needed.setText("0")

        self.chanceOfFourStarLabel = QLabel("Chance of Four Star")
        self.FourStarChanceValidator = QDoubleValidator()
        self.FourStarChanceValidator.setBottom(0.0)
        self.FourStarChanceValidator.setTop(0.5)
        self.chanceOfFourStar = QLineEdit()
        self.chanceOfFourStar.setValidator(self.FourStarChanceValidator)
        self.chanceOfFourStar.setText("0.062")

        self.recycleCheck = QCheckBox("Recycle Cognigems?")

        self.RollButton = QPushButton()
        self.RollButton.setText("ROLL!")
        self.RollButton.clicked.connect(self.DoRoll)

        self.EightyBannerLabel = QLabel("80 Banner", alignment=Qt.AlignmentFlag.AlignCenter)
        self.EightyBannerNumTargetRolledLabel = QLabel("Number of Target Characters Rolled")
        self.EightyBannerNumTargetRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.EightyBannerNumStandardRolledLabel = QLabel("Number of Standard Characters Rolled")
        self.EightyBannerNumStandardRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.OneTenBannerLabel = QLabel("110 Banner",alignment=Qt.AlignmentFlag.AlignCenter)
        self.OneTenBannerNumTargetRolledLabel = QLabel("Number of Target Characters Rolled")
        self.OneTenBannerNumTargetRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.OneTenBannerNumStandardRolledLabel = QLabel("Number of Standard Characters Rolled")
        self.OneTenBannerNumStandardRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)

        self.StatusLabel = QLabel("")

        totalLayout = QVBoxLayout()
        outerLayout = QHBoxLayout()
        totalLayout.addLayout(outerLayout)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,50,0)
        layout.addWidget(self.numRollslabel)
        layout.addWidget(self.numRolls)
        layout.addWidget(self.numA6NeededLabel)
        layout.addWidget(self.numA6Needed)
        layout.addWidget(self.chanceOfFourStarLabel)
        layout.addWidget(self.chanceOfFourStar)
        layout.addWidget(self.recycleCheck)
        layout.addWidget(self.RollButton)

        resultsLayout = QVBoxLayout()
        resultsLayout.addWidget(self.EightyBannerLabel)
        resultsLayout.addWidget(self.EightyBannerNumTargetRolledLabel)
        resultsLayout.addWidget(self.EightyBannerNumTargetRolledResult)
        resultsLayout.addWidget(self.EightyBannerNumStandardRolledLabel)
        resultsLayout.addWidget(self.EightyBannerNumStandardRolledResult)
        resultsLayout.addWidget(self.OneTenBannerLabel)
        resultsLayout.addWidget(self.OneTenBannerNumTargetRolledLabel)
        resultsLayout.addWidget(self.OneTenBannerNumTargetRolledResult)
        resultsLayout.addWidget(self.OneTenBannerNumStandardRolledLabel)
        resultsLayout.addWidget(self.OneTenBannerNumStandardRolledResult)


        outerLayout.addLayout(layout)
        outerLayout.addLayout(resultsLayout)

        statusLayout = QHBoxLayout()
        statusLayout.addWidget(self.StatusLabel)
        totalLayout.addLayout(statusLayout)


        container = QWidget()
        container.setLayout(totalLayout)

        self.setCentralWidget(container)

    def DoRoll(self):
        numRolls = int(self.numRolls.text())+1
        numStandardsNeededRemaining = int(self.numA6Needed.text())
        fourStarChance = float(self.chanceOfFourStar.text())
        recycleCognigems = self.recycleCheck.isChecked()

        chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls, targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls = roller.CalculatePulls(numRolls, numStandardsNeededRemaining, fourStarChance, recycleCognigems)
        self.StatusLabel.setText(f"Rolled {chanceRollCount} Times on 80, Pitied {chancePityPulls} times, Guaranteed Target {chanceGuaranteePulls} times, Lucky Draw {chanceLuckyPulls} times.\nGot {chanceFourStars} Four Stars\nSpent {chanceSpentCognigems} out of {chanceTotalCognigems} purple cognigems\nRolled {targetRollcount} Times on 110, Got Target {targetFiveStars} times, pitied {targetPityPulls} times, plus {targetStandardFiveStars} standards.\nGot {targetFourstars} Four Stars\nSpent {targetSpentCognigems} out of {targetTotalCognigems} purple cognigems")
        self.EightyBannerNumTargetRolledResult.setText(f"{chanceTargetFiveStars}")
        self.EightyBannerNumStandardRolledResult.setText(f"{chanceStandardFiveStars}")
        self.OneTenBannerNumTargetRolledResult.setText(f"{targetFiveStars}")
        self.OneTenBannerNumStandardRolledResult.setText(f"{targetStandardFiveStars}")