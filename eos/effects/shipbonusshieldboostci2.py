# shipBonusShieldBoostCI2
#
# Used by:
# Ship: Bustard
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Operation"),
                                  "shieldBonus", ship.getModifiedItemAttr("shipBonusCI2"), skill="Caldari Industrial")
