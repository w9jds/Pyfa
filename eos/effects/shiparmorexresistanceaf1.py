# shipArmorEXResistanceAF1
#
# Used by:
# Ship: Astero
# Ship: Malice
# Ship: Punisher
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorExplosiveDamageResonance", ship.getModifiedItemAttr("shipBonusAF"),
                           skill="Amarr Frigate")
