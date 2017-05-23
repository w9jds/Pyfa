# shipHybridRangeBonusCBC1
#
# Used by:
# Ship: Naga
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "maxRange", ship.getModifiedItemAttr("shipBonusCBC1"), skill="Caldari Battlecruiser")
