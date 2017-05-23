# shipBonusArmorResistAB
#
# Used by:
# Ship: Abaddon
# Ship: Nestor
effectType = "passive"


def handler(fit, ship, context):
    for resist_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("armor{0}DamageResonance".format(resist_type), ship.getModifiedItemAttr("shipBonusAB"),
                               skill="Amarr Battleship")
