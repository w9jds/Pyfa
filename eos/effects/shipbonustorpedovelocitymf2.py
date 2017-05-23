# shipBonusTorpedoVelocityMF2
#
# Used by:
# Ship: Hound
effectType = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Torpedoes"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusMF2"), skill="Minmatar Frigate")
