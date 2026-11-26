from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QCheckBox
from PyQt6.QtGui import QIntValidator, QDoubleValidator
from random import random # TODO: Remove
import itemroller

class ItemRollerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Item Rolling Simulator")
        self.numRollslabel = QLabel("Number of Rolls")

        self.numRolls = QLineEdit()
        self.numRollsValidator = QIntValidator()
        self.numRollsValidator.setBottom(0)
        self.numRollsValidator.setTop(1000000000)
        self.numRolls.setValidator(self.numRollsValidator)
        self.numRolls.setText("1000")

        self.chanceOfFiveStarChanceLabel = QLabel("Chance of Five Star (Chance)")
        self.FiveStarValidator = QDoubleValidator()
        self.FiveStarValidator.setBottom(0.0)
        self.FiveStarValidator.setTop(0.5)
        self.chanceOfFiveStarChance = QLineEdit()
        self.chanceOfFiveStarChance.setValidator(self.FiveStarValidator)
        self.chanceOfFiveStarChance.setText("0.008")

        self.chanceOfFiveStarTargetLabel = QLabel("Chance of Five Star (Target)")
        self.chanceOfFiveStarTarget = QLineEdit()
        self.chanceOfFiveStarTarget.setValidator(self.FiveStarValidator)
        self.chanceOfFiveStarTarget.setText("0.00358")

        self.chanceOfFourStarLabel = QLabel("Chance of Four Star")
        self.FourStarChanceValidator = QDoubleValidator()
        self.FourStarChanceValidator.setBottom(0.0)
        self.FourStarChanceValidator.setTop(0.5)
        self.chanceOfFourStar = QLineEdit()
        self.chanceOfFourStar.setValidator(self.FourStarChanceValidator)
        self.chanceOfFourStar.setText("0.08")

        self.recycleCheck = QCheckBox("Recycle Cognigems?")

        self.RollButton = QPushButton()
        self.RollButton.setText("ROLL!")
        self.RollButton.clicked.connect(self.DoRoll)

        self.EightyBannerLabel = QLabel("70 Banner", alignment=Qt.AlignmentFlag.AlignCenter)
        self.EightyBannerNumTargetRolledLabel = QLabel("Number of Target Items Rolled")
        self.EightyBannerNumTargetRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.EightyBannerNumStandardRolledLabel = QLabel("Number of Standard Items Rolled")
        self.EightyBannerNumStandardRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.OneTenBannerLabel = QLabel("95 Banner",alignment=Qt.AlignmentFlag.AlignCenter)
        self.OneTenBannerNumTargetRolledLabel = QLabel("Number of Target Items Rolled")
        self.OneTenBannerNumTargetRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)
        self.OneTenBannerNumStandardRolledLabel = QLabel("Number of Standard Items Rolled")
        self.OneTenBannerNumStandardRolledResult = QLabel("N/A",alignment=Qt.AlignmentFlag.AlignRight)

        self.StatusLabel = QLabel("")

        totalLayout = QVBoxLayout()
        outerLayout = QHBoxLayout()
        totalLayout.addLayout(outerLayout)
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,50,0)
        layout.addWidget(self.numRollslabel)
        layout.addWidget(self.numRolls)
        layout.addWidget(self.chanceOfFourStarLabel)
        layout.addWidget(self.chanceOfFourStar)
        layout.addWidget(self.chanceOfFiveStarChanceLabel)
        layout.addWidget(self.chanceOfFiveStarChance)
        layout.addWidget(self.chanceOfFiveStarTargetLabel)
        layout.addWidget(self.chanceOfFiveStarTarget)
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
        fourStarChance = float(self.chanceOfFourStar.text())
        fiveStarStandardChance = float(self.chanceOfFiveStarChance.text())
        fiveStarTargetChance = float(self.chanceOfFiveStarTarget.text())
        recycleCognigems = self.recycleCheck.isChecked()

        chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls, targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls = itemroller.CalculatePulls(numRolls, 0, fourStarChance, fiveStarStandardChance, fiveStarTargetChance, recycleCognigems)
        self.StatusLabel.setText(f"Rolled {chanceRollCount} Times on 70, Pitied {chancePityPulls} times, Guaranteed Target {chanceGuaranteePulls} times, Lucky Draw {chanceLuckyPulls} times.\nGot {chanceFourStars} Four Stars\nSpent {chanceSpentCognigems} out of {chanceTotalCognigems} purple cognigems\nRolled {targetRollcount} Times on 95, Got Target {targetFiveStars} times, pitied {targetPityPulls} times, plus {targetStandardFiveStars} standards.\nGot {targetFourstars} Four Stars\nSpent {targetSpentCognigems} out of {targetTotalCognigems} purple cognigems")
        self.EightyBannerNumTargetRolledResult.setText(f"{chanceTargetFiveStars}")
        self.EightyBannerNumStandardRolledResult.setText(f"{chanceStandardFiveStars}")
        self.OneTenBannerNumTargetRolledResult.setText(f"{targetFiveStars}")
        self.OneTenBannerNumStandardRolledResult.setText(f"{targetStandardFiveStars}")