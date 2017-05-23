# roleBonusJustScramblerStrength
#
# Used by:
# Ship: Maulus Navy Issue
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemIncrease(lambda mod: mod.item.requiresSkill("Navigation"),
                                     "warpScrambleStrength", ship.getModifiedItemAttr("roleBonus"))
