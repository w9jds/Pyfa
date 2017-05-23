# shipLargeHybridTurretRofGB
#
# Used by:
# Ship: Megathron
# Ship: Megathron Navy Issue
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusGB"), skill="Gallente Battleship")
