# shipProjectileDamageMD1
#
# Used by:
# Variations of ship: Thrasher (2 of 2)
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Small Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusMD1"),
                                  skill="Minmatar Destroyer")
