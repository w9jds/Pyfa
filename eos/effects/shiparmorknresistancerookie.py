# shipArmorKNResistanceRookie
#
# Used by:
# Ship: Devoter
# Ship: Gold Magnate
# Ship: Impairor
# Ship: Phobos
# Ship: Silver Magnate
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("rookieArmorResistanceBonus"))
