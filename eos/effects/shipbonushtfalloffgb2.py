# shipBonusHTFalloffGB2
#
# Used by:
# Ship: Kronos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusGB2"), skill="Gallente Battleship")
