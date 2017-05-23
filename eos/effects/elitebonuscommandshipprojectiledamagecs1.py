# eliteBonusCommandShipProjectileDamageCS1
#
# Used by:
# Ship: Sleipnir
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "damageMultiplier", ship.getModifiedItemAttr("eliteBonusCommandShips1"),
                                  skill="Command Ships")
