# subsystemBonusAmarrDefensiveArmorResistance
#
# Used by:
# Subsystem: Legion Defensive - Adaptive Augmenter
effectType = "passive"


def handler(fit, container, context):
    for damage_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("armor{0}DamageResonance".format(damage_type),
                               container.getModifiedItemAttr("subsystemBonusAmarrDefensive"),
                               skill="Amarr Defensive Systems")
