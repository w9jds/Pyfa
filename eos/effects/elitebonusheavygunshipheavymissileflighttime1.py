# eliteBonusHeavyGunshipHeavyMissileFlightTime1
#
# Used by:
# Ship: Cerberus
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusHeavyGunship1"),
                                    skill="Heavy Assault Cruisers")
