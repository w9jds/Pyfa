# shipBonusEMArmorResistanceAD2
#
# Used by:
# Ship: Pontifex
effectType = "passive"


def handler(fit, src, context):
    fit.ship.boostItemAttr("armorEmDamageResonance", src.getModifiedItemAttr("shipBonusAD2"), skill="Amarr Destroyer")
