# shipMissileVelocityCD1
#
# Used by:
# Ship: Flycatcher
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCD1"), skill="Caldari Destroyer")
