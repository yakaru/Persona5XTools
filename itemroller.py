from random import random

def CalculatePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarStandardChance, fiveStarTargetChance, recycleCognigems):
    chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls = CalculateChancePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarStandardChance, recycleCognigems)
    targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls = CalculateTargetPulls(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarTargetChance, recycleCognigems)
    return chanceTargetFiveStars, chanceStandardFiveStars, chanceFourStars, chanceTotalCognigems, chanceSpentCognigems, chanceRollCount, chancePityPulls, chanceGuaranteePulls, chanceLuckyPulls, targetFiveStars, targetStandardFiveStars, targetFourstars, targetTotalCognigems, targetSpentCognigems, targetRollcount, targetPityPulls

def CalculateChancePulls(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarChance, recycleCognigems):
    numCognigems, numTargetFiveStar, numStandardFiveStar, numFourStars, numPityPulls, numGuaranteePulls,numLuckyPulls, fullPity, fourStarPity = CalculateChancePullsInternal(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarChance, 0, 0)
    ROLLCOST = 100
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
            newRolls = newGems // ROLLCOST
            newGems = newGems % ROLLCOST
            extraCognigems, extraTargetFiveStar, extraStandardFiveStar, extraFourStars, extraPityPulls, extraGuranteePulls, extraLuckyPulls, fullPity, fourStarPity = CalculateChancePullsInternal(newRolls + 1, numStandardAwarenessRemaining, fourStarChance, fiveStarChance, fullPity, fourStarPity)
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

def CalculateChancePullsInternal(numPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarChance, fullPity, fourStarPity):
    # do 70 banner
    PITYAMOUNT = 70
    FIVESTARGEMS = 20
    FOURSTARGEMS = 4
    TARGETFOURSTARCHANCE = fiveStarChance + fourStarChance
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
        fullPity += 1
        fourStarPity += 1
        roll = random()
        if (roll < fiveStarChance or fullPity == PITYAMOUNT):
            if (fullPity == PITYAMOUNT):
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
            else:
                guarantee = True
                numStandardFiveStar += 1
            numCognigems += FIVESTARGEMS
        elif (roll < TARGETFOURSTARCHANCE or fourStarPity >= 10):
            numCognigems += FOURSTARGEMS
            fourStarPity = 0
            numFourStars += 1
    return numCognigems, numTargetFiveStar, numStandardFiveStar, numFourStars, numTimesGotPity, numTimesGotGuaranteedTarget, numTimesGotLuckyTarget, fullPity, fourStarPity

def CalculateTargetPulls(numTargetPulls, numStandardAwarenessRemaining, fourStarChance, fiveStarChance, recycleCognigems):
    ROLLCOST = 100
    FREESTANDARDCOUNT = 150
    spentCogniGems = 0

    numCognigems, numTargetFiveStar, pityFives, fourStarCount, fullPity, fourStarPity = CalculateTargetPullsInternal(numTargetPulls, fourStarChance, fiveStarChance, 0, 0)
    rollCount = numTargetPulls-1
    standardGuaranteeProgress = rollCount
    newStandards = (standardGuaranteeProgress // FREESTANDARDCOUNT)
    standardGuaranteeProgress = standardGuaranteeProgress % FREESTANDARDCOUNT
    numCognigems += newStandards * 20
    standardGuarantees = newStandards
    totalCognigems = numCognigems

    if (recycleCognigems):
        newGems = 0
        while (numCognigems >= 10):
            newGemInstances = numCognigems // 10
            spentCogniGems += newGemInstances * 10
            newGems = newGems + newGemInstances * 100
            numCognigems = numCognigems % 10
            newRolls = newGems // ROLLCOST
            newGems = newGems % ROLLCOST
            extraCognigems, extraTargetFiveStar, extraPityFives, extraFourStars, fullPity, fourStarPity = CalculateTargetPullsInternal(newRolls + 1, fourStarChance, fiveStarChance, fullPity, fourStarPity)
            totalCognigems += extraCognigems
            rollCount += newRolls
            standardGuaranteeProgress += newRolls
            pityFives += extraPityFives
            fourStarCount += extraFourStars
            additionalStandards = (standardGuaranteeProgress // FREESTANDARDCOUNT)
            standardGuaranteeProgress = standardGuaranteeProgress % FREESTANDARDCOUNT
            standardGuarantees += additionalStandards
            numCognigems += additionalStandards * 20
            totalCognigems += additionalStandards * 20
            numCognigems += extraCognigems
            numTargetFiveStar += extraTargetFiveStar
    return numTargetFiveStar, standardGuarantees, fourStarCount, totalCognigems, spentCogniGems, rollCount, pityFives

def CalculateTargetPullsInternal(numPulls, fourStarChance, fiveStarChance, fullPity, fourStarPity):
    # do 95 banner
    TARGETFOURSTARCHANCE = fiveStarChance + fourStarChance
    PITYAMOUNT = 95
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
        if (roll < fiveStarChance or fullPity == 95):
            if (fullPity == 95):
                numTimesGotToPity += 1
            fullPity = 0
            numTargetFiveStar += 1
            numCognigems += 20
        elif (roll < TARGETFOURSTARCHANCE or fourStarPity >= 10):
            numCognigems += 4
            fourStarPity = 0
            numFourStars += 1
    return numCognigems, numTargetFiveStar, numTimesGotToPity, numFourStars, fullPity, fourStarPity