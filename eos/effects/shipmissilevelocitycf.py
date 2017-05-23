# shipMissileVelocityCF
#
# Used by:
# Ship: Caldari Navy Hookbill
# Ship: Crow
# Ship: Kestrel
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCF"), skill="Caldari Frigate")
