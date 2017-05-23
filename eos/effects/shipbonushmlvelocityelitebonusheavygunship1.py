# shipBonusHMLVelocityEliteBonusHeavyGunship1
#
# Used by:
# Ship: Sacrilege
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusHeavyGunship1"),
                                    skill="Heavy Assault Cruisers")
