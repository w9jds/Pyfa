# shipBonusExplosiveShieldResistanceMD2
#
# Used by:
# Ship: Bifrost
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("shieldExplosiveDamageResonance", src.getModifiedItemAttr("shipBonusMD2"),
                           skill="Minmatar Destroyer")
