# shipArmorEMResistanceAF1
#
# Used by:
# Ship: Astero
# Ship: Malice
# Ship: Punisher
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("armorEmDamageResonance", ship.getModifiedItemAttr("shipBonusAF"), skill="Amarr Frigate")
