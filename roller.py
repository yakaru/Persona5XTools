from random import random

def CalculatePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, recycleCognigems):
    chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls = CalculateChancePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, recycleCognigems)
    targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls = CalculateTargetPulls(numPulls, numStandardAwarenessRemaining, fourStarChance, recycleCognigems)
    return chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls, targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls

def CalculateChancePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, recycleCognigems):
    numCognigems, numTargetFiveStar, numStandardFiveStar, numFourStars, numPityPulls, numGuaranteePulls,numLuckyPulls, fullPity, fourStarPity = CalculateChancePullsInternal(numPulls, numStandardAwarenessRemaining, fourStarChance, 0, 0)
    totalCognigems = numCognigems
    rollCount = numPulls - 1
    numStandardAwarenessRemaining = numStandardAwarenessRemaining - numStandardFiveStar
    # are we recycling?
    spentCogniGems = 0
    if (recycleCognigems):
        newGems = 0
        while (numCognigems >= 10):
            newGemInstances = numCognigems // 10
            spentCogniGems += newGemInstances * 10
            newGems = newGems + newGemInstances * 100
            numCognigems = numCognigems % 10
            newRolls = newGems // 150
            newGems = newGems % 150
            extraCognigems, extraTargetFiveStar, extraStandardFiveStar, extraFourStars, extraPityPulls, extraGuranteePulls, extraLuckyPulls, fullPity, fourStarPity = CalculateChancePulls(newRolls + 1, numStandardAwarenessRemaining, fourStarChance, recycleCognigems)
            numFourStars += extraFourStars
            numPityPulls += extraPityPulls
            numGuaranteePulls += extraGuranteePulls
            numLuckyPulls += extraLuckyPulls
            totalCognigems += extraCognigems
            rollCount += newRolls
            numStandardAwarenessRemaining -= extraStandardFiveStar
            numCognigems += extraCognigems
            numTargetFiveStar += extraTargetFiveStar
            numStandardFiveStar += extraStandardFiveStar

    return numTargetFiveStar, numStandardFiveStar, numFourStars, totalCognigems, spentCogniGems, rollCount, numPityPulls, numGuaranteePulls, numLuckyPulls

def CalculateChancePullsInternal(numPulls, numStandardAwarenessRemaining, fourStarChance, fullPity, fourStarPity):
    # do 80 banner
    TARGETRAWCHANCE = 0.008
    TARGETFOURSTARCHANCE = TARGETRAWCHANCE + fourStarChance
    finishedRolls = 0
    targetCounter = 0
    numCognigems = 0
    lastFourStar = 0
    numTargetFiveStar = 0
    numStandardFiveStar = 0
    guarantee = False
    numTimesGotPity = 0
    numTimesGotGuaranteedTarget = 0
    numTimesGotLuckyTarget = 0
    numFourStars = 0
    for x in range(1, numPulls):
        fullPity += 1;
        fourStarPity += 1
        roll = random()
        if (roll < TARGETRAWCHANCE or fullPity == 80):
            if (fullPity == 80):
                numTimesGotPity += 1
            fullPity = 0
            gotFiveStar = random()
            if (gotFiveStar > .5 or guarantee):
                if (guarantee):
                    numTimesGotGuaranteedTarget += 1
                else:
                    numTimesGotLuckyTarget += 1
                guarantee = False
                numTargetFiveStar += 1
                targetCounter += 1
                if (targetCounter > 1):  # not first pull
                    numCognigems += 30
                    if (targetCounter == 7):
                        targetCounter = 0;
            else:
                guarantee = True
                numStandardFiveStar += 1
                if (numStandardAwarenessRemaining >= 0):
                    numCognigems += 75
                else:
                    numCognigems += 30
                    numStandardAwarenessRemaining -= 1
        elif (roll < TARGETFOURSTARCHANCE or fourStarPity >= 10):
            numCognigems += 15
            fourStarPity = 0
            numFourStars += 1
    return numCognigems, numTargetFiveStar, numStandardFiveStar, numFourStars, numTimesGotPity, numTimesGotGuaranteedTarget, numTimesGotLuckyTarget, fullPity, fourStarPity

def CalculateTargetPulls(numTargetPulls, numStandardAwarenessRemaining, fourStarChance, recycleCognigems):
    spentCogniGems = 0

    numCognigems, numTargetFiveStar, pityFives, fourStarCount, fullPity, fourStarPity = CalculateTargetPullsInternal(numTargetPulls, fourStarChance, 0, 0)
    rollCount = numTargetPulls-1
    standardGuaranteeProgress = rollCount
    newStandards = (standardGuaranteeProgress // 165)
    standardGuaranteeProgress = standardGuaranteeProgress % 165
    if (numStandardAwarenessRemaining >= newStandards):
        numStandardAwarenessRemaining -= newStandards
        numCognigems += newStandards * 30
    else:
        numCognigems += numStandardAwarenessRemaining * 30
        newStandards -= numStandardAwarenessRemaining
        numStandardAwarenessRemaining = 0
        numCognigems += newStandards * 75
    standardGuarantees = newStandards
    totalCognigems = numCognigems

    if (recycleCognigems):
        newGems = 0
        while (numCognigems >= 10):
            newGemInstances = numCognigems // 10
            spentCogniGems += newGemInstances * 10
            newGems = newGems + newGemInstances * 100
            numCognigems = numCognigems % 10
            newRolls = newGems // 150
            newGems = newGems % 150
            extraCognigems, extraTargetFiveStar, extraPityFives, extraFourStars, fullPity, fourStarPity = CalculateTargetPullsInternal(newRolls + 1, fourStarChance, fullPity, fourStarPity)
            totalCognigems += extraCognigems
            rollCount += newRolls
            standardGuaranteeProgress += newRolls
            pityFives += extraPityFives
            fourStarCount += extraFourStars
            additionalStandards = (standardGuaranteeProgress // 165)
            standardGuaranteeProgress = standardGuaranteeProgress % 165
            standardGuarantees += additionalStandards
            if (numStandardAwarenessRemaining >= additionalStandards):
                numStandardAwarenessRemaining -= additionalStandards
                numCognigems += additionalStandards * 30
                totalCognigems += additionalStandards * 30
            else:
                numCognigems += numStandardAwarenessRemaining * 30
                additionalStandards -= numStandardAwarenessRemaining
                numStandardAwarenessRemaining = 0
                numCognigems += additionalStandards * 75
                totalCognigems += additionalStandards * 75
            numCognigems += extraCognigems
            numTargetFiveStar += extraTargetFiveStar
    return numTargetFiveStar, standardGuarantees, fourStarCount, totalCognigems, spentCogniGems, rollCount, pityFives

def CalculateTargetPullsInternal(numPulls, fourStarChance, fullPity, fourStarPity):
    # do 110 banner
    TARGETRAWCHANCE = 0.00406
    TARGETFOURSTARCHANCE = TARGETRAWCHANCE +  fourStarChance
    finishedRolls = 0
    targetCounter = 0
    numCognigems = 0
    lastFourStar = 0
    numTargetFiveStar = 0
    numTimesGotToPity = 0
    numFourStars = 0

    for x in range(1, numPulls):
        fullPity += 1
        fourStarPity += 1
        roll = random()
        if (roll < TARGETRAWCHANCE or fullPity == 110):
            if (fullPity == 110):
                numTimesGotToPity += 1
            fullPity = 0
            numTargetFiveStar += 1
            targetCounter += 1
            if (targetCounter > 1):  # not first pull
                numCognigems += 30
                if (targetCounter == 7):
                    targetCounter = 0
        elif (roll < TARGETFOURSTARCHANCE or fourStarPity >= 10):
            numCognigems += 15
            fourStarPity = 0
            numFourStars += 1
    return numCognigems, numTargetFiveStar, numTimesGotToPity, numFourStars, fullPity, fourStarPity