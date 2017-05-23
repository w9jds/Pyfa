# shipBonusExplosiveMissileDmgMD1
#
# Used by:
# Ship: Bifrost
effectType = "passive"


def handler(fit, src, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "explosiveDamage", src.getModifiedItemAttr("shipBonusMD1"),
                                    skill="Minmatar Destroyer")
