# shipBonusMedMissileFlightTimeCC2
#
# Used by:
# Ship: Enforcer
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "explosionDelay", src.getModifiedItemAttr("shipBonusCC2"), skill="Caldari Cruiser")
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "explosionDelay", src.getModifiedItemAttr("shipBonusCC2"), skill="Caldari Cruiser")
