# shipHybridDamageBonusGBC2
#
# Used by:
# Ship: Talos
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Hybrid Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusGBC2"),
                                  skill="Gallente Battlecruiser")
