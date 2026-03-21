from enum import Enum

class WeaknessLevel(Enum):
    WEAK_RESIST = 1
    WEAK_NORMAL = 2
    WEAK_WEAK = 3
    WEAK_NAVIWEAK = 4

def doDamageCalculation(baseAttack, damageMult, elementMult, increasedDamage, defenseConstant, defenseScalar, pierceValue, defReduction, isWindswept, critChanceRaw, criticalMult, hasA6WindVast, skillCoefficient, weaknessLevel, finalDamageCoefficient, otherDamageCoefficient):


    multiplier = 1.0 + damageMult + elementMult + increasedDamage

    # 1 - {Enemy Defense Value × [(100% + Additional Defense Coefficient) × (100% - Pierce) - Defense Reduction] × (100% - Windswept 12%)}
    # ÷ {Enemy Defense Value × [(100% + Additional Defense Coefficient) × (100% - Pierce) - Defense Reduction] × (100% - Windswept 12%) + 1400}

    PierceScalar = max(0.0, 1.0 - pierceValue)
    enemyBasicDefense = max((defenseConstant * (defenseScalar * PierceScalar - defReduction)), 0.0)
    enemyDenominator = enemyBasicDefense
    if (isWindswept):
        enemyBasicDefense *= .88
        enemyDenominator *= .88
    enemyDenominator += 1400

    defenseScalar = 1.0 - enemyBasicDefense / enemyDenominator

    criticalChance = max(1.0, critChanceRaw)
    if (hasA6WindVast):
        criticalMult += min(0.0, criticalChance - 1.0) * 2

    critDamage = criticalChance * criticalMult

    lookup_table = {WeaknessLevel.WEAK_RESIST: 0.5, WeaknessLevel.WEAK_NORMAL: 1.0, WeaknessLevel.WEAK_WEAK: 1.2, WeaknessLevel.WEAK_NAVIWEAK: 1.45}
    weaknessCoefficient = lookup_table.get(weaknessLevel)  # Returns 1


    finalCalculation = baseAttack * multiplier * defenseScalar * critDamage * skillCoefficient * weaknessCoefficient * finalDamageCoefficient * otherDamageCoefficient
    finalCalculationMax = finalCalculation * 1.05
    finalCalculationMin = finalCalculation * 0.95

    return finalCalculation, finalCalculationMax, finalCalculationMin