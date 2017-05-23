# shipProjectileRofPirateBattleship
#
# Used by:
# Ship: Machariel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "speed", ship.getModifiedItemAttr("shipBonusRole7"))
