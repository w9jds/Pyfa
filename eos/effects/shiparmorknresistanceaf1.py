# shipArmorKNResistanceAF1
#
# Used by:
# Ship: Astero
# Ship: Malice
# Ship: Punisher
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorKineticDamageResonance", ship.getModifiedItemAttr("shipBonusAF"),
                           skill="Amarr Frigate")
