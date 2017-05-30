# shipBonusHybridOptimalCB
#
# Used by:
# Ship: Rokh
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusCB"), skill="Caldari Battleship")
