# shipArmorThermalResistanceAC2
#
# Used by:
# Ship: Maller
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("shipBonusAC2"),
                           skill="Amarr Cruiser")
