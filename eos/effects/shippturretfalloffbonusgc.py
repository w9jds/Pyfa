# shipPTurretFalloffBonusGC
#
# Used by:
# Ship: Cynabal
# Ship: Moracha
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Medium Projectile Turret"),
                                  "falloff", ship.getModifiedItemAttr("shipBonusGC"), skill="Gallente Cruiser")
