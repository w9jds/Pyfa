# shipLargeHybridTrackingBonusGBC1
#
# Used by:
# Ship: Talos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "trackingSpeed", ship.getModifiedItemAttr("shipBonusGBC1"),
                                  skill="Gallente Battlecruiser")
