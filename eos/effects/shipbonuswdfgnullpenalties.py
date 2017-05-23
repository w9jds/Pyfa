# shipBonusWDFGnullPenalties
#
# Used by:
# Ship: Fiend
runTime = "early"
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Propulsion Jamming"),
                                  "speedFactorBonus", ship.getModifiedItemAttr("shipBonusAT"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Propulsion Jamming"),
                                  "speedBoostFactorBonus", ship.getModifiedItemAttr("shipBonusAT"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Propulsion Jamming"),
                                  "massBonusPercentage", ship.getModifiedItemAttr("shipBonusAT"))
