from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QCheckBox, QRadioButton, QButtonGroup
from PyQt6.QtGui import QIntValidator, QDoubleValidator
import damagecalc

class DamageCalcWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Damage Calculator")

        # # × ⓒ 1 - {Enemy Defense Value × [(100% + Additional Defense Coefficient) × (100% - Pierce) - Defense Reduction] × (100% - Windswept 12%)}
        # # Pierce is lower since it's character not enemy
        # Enemy
        # Defense Constant
        # Defense Percent
        # Defense Reduction
        # Windswept

        self.enemyHeaderLabel = QLabel("<b>Enemy</b>")
        self.enemyHeaderLabel.setTextFormat(Qt.TextFormat.RichText)

        self.genericIntValidator = QIntValidator()
        self.genericIntValidator.setBottom(0)
        self.genericIntValidator.setTop(100000000)

        self.genericUncappedPercentValidator = QDoubleValidator()
        self.genericUncappedPercentValidator.setBottom(0.0)
        self.genericUncappedPercentValidator.setTop(10.0)

        self.enemyDefenseConstantLabel = QLabel("Defense Value")
        self.enemyDefenseConstantData = QLineEdit()
        self.enemyDefenseConstantData.setValidator(self.genericIntValidator)
        self.enemyDefenseConstantData.setText("1280")

        self.enemyDefenseScaleLabel = QLabel("Defense Scaling")
        self.enemyDefenseScaleData = QLineEdit()
        self.enemyDefenseScaleData.setValidator(self.genericUncappedPercentValidator)
        self.enemyDefenseScaleData.setText("2.584")

        self.WindSweptCheckBox = QCheckBox("Windswept")

        self.DefenseReductionAmountLabel = QLabel("Defense Down %")
        self.DefenseReductionAmountData = QLineEdit()
        self.DefenseReductionAmountData.setValidator(self.genericUncappedPercentValidator)
        self.DefenseReductionAmountData.setText("0.0")

        enemyLayout = QVBoxLayout()
        enemyLayout.addWidget(self.enemyHeaderLabel)

        defValueLayout = QHBoxLayout()
        defValueLayout.addWidget(self.enemyDefenseConstantLabel)
        defValueLayout.addWidget(self.enemyDefenseConstantData)
        enemyLayout.addLayout(defValueLayout)

        defPercLayout = QHBoxLayout()
        defPercLayout.addWidget(self.enemyDefenseScaleLabel)
        defPercLayout.addWidget(self.enemyDefenseScaleData)
        enemyLayout.addLayout(defPercLayout)

        enemyLayout.addWidget(self.WindSweptCheckBox)

        defDownLayout = QHBoxLayout()
        defDownLayout.addWidget(self.DefenseReductionAmountLabel)
        defDownLayout.addWidget(self.DefenseReductionAmountData)
        enemyLayout.addLayout(defDownLayout)

        # Character
        # # ⓐ {(Character Attack Value + Weapon Attack Value) × Attack % + Attack Constant}
        # Base Character Attack
        # Base Weapon Attack
        # Attack%
        # Flat Attack
        self.CharacterHeaderLabel = QLabel("<b>Character</b>")
        self.CharacterHeaderLabel.setTextFormat(Qt.TextFormat.RichText)
        self.CharacterBaseLabel = QLabel("<b>Base Values</b>")
        self.CharacterBaseLabel.setTextFormat(Qt.TextFormat.RichText)

        characterLayout = QVBoxLayout()
        characterLayout.addWidget(self.CharacterHeaderLabel)
        characterLayout.addWidget(self.CharacterBaseLabel)

        self.CharacterAttackValueLabel = QLabel("Character Base Attack")
        self.CharacterAttackValueData = QLineEdit()
        self.CharacterAttackValueData.setValidator(self.genericIntValidator)
        self.CharacterAttackValueData.setText("1286")

        self.CharacterWeaponAttackValueLabel = QLabel("Character Weapon Base Attack")
        self.CharacterWeaponAttackValueData = QLineEdit()
        self.CharacterWeaponAttackValueData.setValidator(self.genericIntValidator)
        self.CharacterWeaponAttackValueData.setText("766")

        characterBaseValueLayout = QVBoxLayout()
        characterAttackValueLayout = QHBoxLayout()
        characterAttackValueLayout.addWidget(self.CharacterAttackValueLabel)
        characterAttackValueLayout.addWidget(self.CharacterAttackValueData)
        characterBaseValueLayout.addLayout(characterAttackValueLayout)
        characterWeaponValueLayout = QHBoxLayout()
        characterWeaponValueLayout.addWidget(self.CharacterWeaponAttackValueLabel)
        characterWeaponValueLayout.addWidget(self.CharacterWeaponAttackValueData)
        characterBaseValueLayout.addLayout(characterWeaponValueLayout)
        characterLayout.addLayout(characterBaseValueLayout)

        self.characterTotalAttackLabel = QLabel("Total Attack (Ignores above, this is temp)")
        self.characterTotalAttackData = QLineEdit()
        self.characterTotalAttackData.setValidator(self.genericIntValidator)
        self.characterTotalAttackData.setText("4276")
        characterTotalAttack = QVBoxLayout()
        characterTotalAttack.addWidget(self.characterTotalAttackLabel)
        characterTotalAttack.addWidget(self.characterTotalAttackData)
        characterLayout.addLayout(characterTotalAttack)
        # × ⓑ {100% + Damage Mult + Elemental Damage Bonus + Increased Damage Taken by Enemy}
        # Damage Mult
        # Elemental Damage
        # Dmg Increase

        self.characterMultiplierLabel = QLabel("<b>Character Multiplier</b>")
        self.CharacterHeaderLabel.setTextFormat(Qt.TextFormat.RichText)
        characterLayout.addWidget(self.characterMultiplierLabel)

        self.DamageMultLabel = QLabel("Damage Multiplier")
        self.DamageMultData = QLineEdit()
        self.DamageMultData.setValidator(self.genericUncappedPercentValidator)
        self.DamageMultData.setText("0.0")

        self.ElementalMultLabel = QLabel("Elemental Multiplier")
        self.ElementalMultData = QLineEdit()
        self.ElementalMultData.setValidator(self.genericUncappedPercentValidator)
        self.ElementalMultData.setText("0.0")

        self.IncreasedDamageLabel = QLabel("Increased Damage")
        self.IncreasedDamageData = QLineEdit()
        self.IncreasedDamageData.setValidator(self.genericUncappedPercentValidator)
        self.IncreasedDamageData.setText("0.0")

        characterMultiplierLayout = QVBoxLayout()
        characterMultiplierLayout.addWidget(self.characterMultiplierLabel)
        characterMultiplierInteriorLayout = QVBoxLayout()
        characterDamageMultLayout = QHBoxLayout()
        characterDamageMultLayout.addWidget(self.DamageMultLabel)
        characterDamageMultLayout.addWidget(self.DamageMultData)
        characterElementalMultLayout = QHBoxLayout()
        characterElementalMultLayout.addWidget(self.ElementalMultLabel)
        characterElementalMultLayout.addWidget(self.ElementalMultData)
        damageIncreaseLayout = QHBoxLayout()
        damageIncreaseLayout.addWidget(self.IncreasedDamageLabel)
        damageIncreaseLayout.addWidget(self.IncreasedDamageData)

        characterMultiplierInteriorLayout.addLayout(characterDamageMultLayout)
        characterMultiplierInteriorLayout.addLayout(characterElementalMultLayout)
        characterMultiplierInteriorLayout.addLayout(damageIncreaseLayout)

        characterMultiplierLayout.addLayout(characterMultiplierInteriorLayout)
        characterLayout.addLayout(characterMultiplierLayout)


        # Pierce
        self.PierceLabel = QLabel("Pierce")
        self.PierceData = QLineEdit()
        self.PierceData.setValidator(self.genericUncappedPercentValidator)
        self.PierceData.setText("0.0")

        characterPierceLayout = QHBoxLayout()
        characterPierceLayout.addWidget(self.PierceLabel)
        characterPierceLayout.addWidget(self.PierceData)
        characterLayout.addLayout(characterPierceLayout)

        # × ⓓ {Critical DMG(Mult) (when Critical occurs) or Stable Domain}
        # Crit Chance
        # Crit Mult
        # WindVast A6?

        self.CriticalLabel = QLabel("<b>Critical</b>")
        self.CriticalLabel.setTextFormat(Qt.TextFormat.RichText)
        characterLayout.addWidget(self.CriticalLabel)

        self.CritChanceLabel = QLabel("Critical Chance")
        self.CritChanceData = QLineEdit()
        self.CritChanceData.setValidator(self.genericUncappedPercentValidator)
        self.CritChanceData.setText("0.06")

        self.CritMultiplierLabel = QLabel("Critical Multiplier")
        self.CritMultiplierData = QLineEdit()
        self.CritMultiplierData.setValidator(self.genericUncappedPercentValidator)
        self.CritMultiplierData.setText("1.5")

        self.A6WindVastBox = QCheckBox("A6 Wind Vast")

        characterMultiplierLayout = QVBoxLayout()
        characterMultiplierChanceLayout = QHBoxLayout()
        characterMultiplierChanceLayout.addWidget(self.CritChanceLabel)
        characterMultiplierChanceLayout.addWidget(self.CritChanceData)
        characterMultiplierAmountLayout = QHBoxLayout()
        characterMultiplierAmountLayout.addWidget(self.CritMultiplierLabel)
        characterMultiplierAmountLayout.addWidget(self.CritMultiplierData)
        characterMultiplierLayout.addLayout(characterMultiplierChanceLayout)
        characterMultiplierLayout.addLayout(characterMultiplierAmountLayout)
        characterMultiplierLayout.addWidget(self.A6WindVastBox)
        characterLayout.addLayout(characterMultiplierLayout)

        # × ⓔ Skill Coefficient
        self.characterSkillCoefficentLabel = QLabel("Skill Coefficient")
        self.characterSkillCoefficientData = QLineEdit()
        self.characterSkillCoefficientData.setValidator(self.genericUncappedPercentValidator)
        self.characterSkillCoefficientData.setText("1.0")
        characterSkillCoefficientLayout = QHBoxLayout()
        characterSkillCoefficientLayout.addWidget(self.characterSkillCoefficentLabel)
        characterSkillCoefficientLayout.addWidget(self.characterSkillCoefficientData)
        characterLayout.addLayout(characterSkillCoefficientLayout)

        # × ⓕ Weakness Coefficient (Resistance 50% / Normal 100% / Weakness 120%)
        characterWeaknessLabel = QLabel("<b>Weakness</b>")
        characterWeaknessLabel.setTextFormat(Qt.TextFormat.RichText)

        self.characterWeaknessResistRadio = QRadioButton("Resist")
        self.characterWeaknessNormalRadio = QRadioButton("Normal")
        self.characterWeaknessNormalRadio.setChecked(True)
        self.characterWeaknessWeakRadio = QRadioButton("Weak")
        self.characterWeaknessNaviWeakRadio = QRadioButton("NaviWeak")
        characterWeaknessButtonGroup = QButtonGroup()
        characterWeaknessButtonGroup.addButton(self.characterWeaknessResistRadio)
        characterWeaknessButtonGroup.addButton(self.characterWeaknessNormalRadio)
        characterWeaknessButtonGroup.addButton(self.characterWeaknessWeakRadio)
        characterWeaknessButtonGroup.addButton(self.characterWeaknessNaviWeakRadio)

        characterLayout.addWidget(characterWeaknessLabel)
        characterWeaknessLayout = QVBoxLayout()
        characterWeaknessLayout.addWidget(self.characterWeaknessResistRadio)
        characterWeaknessLayout.addWidget(self.characterWeaknessNormalRadio)
        characterWeaknessLayout.addWidget(self.characterWeaknessWeakRadio)
        characterWeaknessLayout.addWidget(self.characterWeaknessNaviWeakRadio)
        characterLayout.addLayout(characterWeaknessLayout)


        # × ⓖ Final Damage Bonus × ⓗ Other Coefficients
        self.FinalDamageLabel = QLabel("Final Damage Multiplier")
        self.FinalDamageData = QLineEdit()
        self.FinalDamageData.setValidator(self.genericUncappedPercentValidator)
        self.FinalDamageData.setText("1.0")
        self.OtherModifierLabel = QLabel("Other Multiplier")
        self.OtherModifierData = QLineEdit()
        self.OtherModifierData.setValidator(self.genericUncappedPercentValidator)
        self.OtherModifierData.setText("1.0")

        FinalModifiers = QVBoxLayout()
        FinalDamageLayout = QHBoxLayout()
        FinalDamageLayout.addWidget(self.FinalDamageLabel)
        FinalDamageLayout.addWidget(self.FinalDamageData)
        FinalModifiers.addLayout(FinalDamageLayout)
        OtherDamageLayout = QHBoxLayout()
        OtherDamageLayout.addWidget(self.OtherModifierLabel)
        OtherDamageLayout.addWidget(self.OtherModifierData)
        FinalModifiers.addLayout(OtherDamageLayout)
        characterLayout.addLayout(FinalModifiers)
        # × ⓘ Random Range Coefficient (0.95~1.05)

        CalculateButton = QPushButton("Calculate")
        characterLayout.addWidget(CalculateButton)
        CalculateButton.clicked.connect(self.DoCalculate)

        self.FinalDamageBaseLabel = QLabel("Final Damage:")
        self.FinalDamageBase = QLabel("")

        self.FinalDamageMaxLabel = QLabel("Max Damage:")
        self.FinalDamageMax = QLabel("")
        self.FinalDamageMinLabel = QLabel("Min Damage:")
        self.FinalDamageMin = QLabel("")

        resultsLayout = QVBoxLayout()
        resultsLayoutFinalBase = QHBoxLayout()
        resultsLayoutFinalMax = QHBoxLayout()
        resultsLayoutFinalMin = QHBoxLayout()
        resultsLayoutFinalBase.addWidget(self.FinalDamageBaseLabel)
        resultsLayoutFinalBase.addWidget(self.FinalDamageBase)
        resultsLayoutFinalMin.addWidget(self.FinalDamageMinLabel)
        resultsLayoutFinalMin.addWidget(self.FinalDamageMin)
        resultsLayoutFinalMax.addWidget(self.FinalDamageMaxLabel)
        resultsLayoutFinalMax.addWidget(self.FinalDamageMax)
        resultsLayout.addLayout(resultsLayoutFinalBase)
        resultsLayout.addLayout(resultsLayoutFinalMin)
        resultsLayout.addLayout(resultsLayoutFinalMax)
        characterLayout.addLayout(resultsLayout)

        totalLayout = QHBoxLayout()

        outerLayout = QVBoxLayout()
        outerLayout.addLayout(enemyLayout)
        outerLayout.addLayout(characterLayout)

        totalLayout.addLayout(outerLayout)
        container = QWidget()
        container.setLayout(totalLayout)
        self.setCentralWidget(container)

    def DoCalculate(self):
        # def doDamageCalculation(baseAttack, damageMult, elementMult, increasedDamage, defenseConst, defenseScale, pierceValue, defReduction, isWindswept, critChance, critMult, hasA6WindVast, skillCoeff, weaknessLevel, finalModifier, otherModifier):
        baseAttack = (int)(self.characterTotalAttackData.text())
        damageMult = (float)(self.DamageMultData.text())
        elementMult = (float)(self.ElementalMultData.text())
        incDamageMult = (float)(self.IncreasedDamageData.text())
        defenseConstant = (float)(self.enemyDefenseConstantData.text())
        defenseScalar = (float)(self.enemyDefenseScaleData.text())
        pierceValue = (float)(self.PierceData.text())
        defReduction = (float)(self.DefenseReductionAmountData.text())
        isWindswept = self.WindSweptCheckBox.isChecked()
        critChance = (float)(self.CritChanceData.text())
        critMult = (float)(self.CritMultiplierData.text())
        skillCoefficient = (float)(self.characterSkillCoefficientData.text())
        hasA6WindVast = self.A6WindVastBox.isChecked()
        weaknessLevel = damagecalc.WeaknessLevel.WEAK_NORMAL

        # TODO: make this a lookup table or something
        if (self.characterWeaknessResistRadio.isChecked()):
            weaknessLevel = damagecalc.WeaknessLevel.WEAK_RESIST
        if (self.characterWeaknessWeakRadio.isChecked()):
            weaknessLevel = damagecalc.WeaknessLevel.WEAK_WEAK
        if (self.characterWeaknessNaviWeakRadio.isChecked()):
            weaknessLevel = damagecalc.WeaknessLevel.WEAK_NAVIWEAK
        finalDamageCoefficient = (float)(self.FinalDamageData.text())
        otherDamageCoefficient = (float)(self.OtherModifierData.text())

        finalBase, finalMax, finalMin = damagecalc.doDamageCalculation(baseAttack, damageMult, elementMult, incDamageMult, defenseConstant, defenseScalar, pierceValue, defReduction, isWindswept, critChance, critMult, hasA6WindVast, skillCoefficient, weaknessLevel, finalDamageCoefficient, otherDamageCoefficient )
        self.FinalDamageBase.setText(str(finalBase))
        self.FinalDamageMax.setText((str(finalMax)))
        self.FinalDamageMin.setText((str(finalMin)))

# TODO: Navi A6 Weakness/Damage Bonus