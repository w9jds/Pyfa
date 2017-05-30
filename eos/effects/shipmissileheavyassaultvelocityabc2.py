# shipMissileHeavyAssaultVelocityABC2
#
# Used by:
# Ship: Damnation
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusABC2"),
                                    skill="Amarr Battlecruiser")
