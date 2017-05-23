# shipBonusPTFalloffMB1
#
# Used by:
# Ship: Vargur
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusMB"), skill="Minmatar Battleship")
