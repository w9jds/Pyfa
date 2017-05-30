# shipShieldBoostRookie
#
# Used by:
# Ship: Immolator
# Ship: Reaper
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", ship.getModifiedItemAttr("rookieShieldBoostBonus"))
