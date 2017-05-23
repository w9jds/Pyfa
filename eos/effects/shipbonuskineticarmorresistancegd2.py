# shipBonusKineticArmorResistanceGD2
#
# Used by:
# Ship: Magus
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("armorKineticDamageResonance", src.getModifiedItemAttr("shipBonusGD2"),
                           skill="Gallente Destroyer")
