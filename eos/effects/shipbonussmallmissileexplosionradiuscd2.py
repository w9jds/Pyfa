# shipBonusSmallMissileExplosionRadiusCD2
#
# Used by:
# Ship: Flycatcher
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(
            lambda mod: mod.charge.requiresSkill("Rockets") or mod.charge.requiresSkill("Light Missiles"),
            "aoeCloudSize", ship.getModifiedItemAttr("shipBonusCD2"), skill="Caldari Destroyer")
