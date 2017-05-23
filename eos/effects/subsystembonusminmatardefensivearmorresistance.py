# subsystemBonusMinmatarDefensiveArmorResistance
#
# Used by:
# Subsystem: Loki Defensive - Adaptive Augmenter
effectType = "passive"


def handler(fit, module, context):
    for damage_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("armor{0}DamageResonance".format(damage_type),
                               module.getModifiedItemAttr("subsystemBonusMinmatarDefensive"),
                               skill="Minmatar Defensive Systems")
