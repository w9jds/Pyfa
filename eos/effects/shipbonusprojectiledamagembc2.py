# shipBonusProjectileDamageMBC2
#
# Used by:
# Ship: Sleipnir
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("shipBonusMBC2"),
                                  skill="Minmatar Battlecruiser")
