# shipBonusHAMVelocityEliteBonusHeavyGunship1
#
# Used by:
# Ship: Sacrilege
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("eliteBonusHeavyGunship1"),
                                    skill="Heavy Assault Cruisers")
