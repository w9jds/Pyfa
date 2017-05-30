# shipHeavyAssaultMissileAOECloudSizeCBC1
#
# Used by:
# Ship: Drake Navy Issue
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "aoeCloudSize", ship.getModifiedItemAttr("shipBonusCBC1"),
                                    skill="Caldari Battlecruiser")
