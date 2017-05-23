# shipBonusShieldTransferBoostAmountCC2
#
# Used by:
# Ship: Osprey
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Emission Systems"),
                                  "shieldBonus", ship.getModifiedItemAttr("shipBonusCC2"), skill="Caldari Cruiser")
