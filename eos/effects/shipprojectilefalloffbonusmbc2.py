# shipProjectileFalloffBonusMBC2
#
# Used by:
# Ship: Tornado
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusMBC2"), skill="Minmatar Battlecruiser")
