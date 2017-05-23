# eliteBonusGunshipArmorThermalResistance1
#
# Used by:
# Ship: Vengeance
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("eliteBonusGunship1"),
                           skill="Assault Frigates")
