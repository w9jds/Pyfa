# subsystemBonusGallenteDefensiveArmorResistance
#
# Used by:
# Subsystem: Proteus Defensive - Adaptive Augmenter
effectType = "passive"


def handler(fit, container, context):
    for damage_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("armor{0}DamageResonance".format(damage_type),
                               container.getModifiedItemAttr("subsystemBonusGallenteDefensive"),
                               skill="Gallente Defensive Systems")
