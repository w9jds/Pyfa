# subsystemBonusMinmatarDefensiveShieldResistance
#
# Used by:
# Subsystem: Loki Defensive - Adaptive Shielding
effectType = "passive"


def handler(fit, container, context):
    for damage_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("shield{0}DamageResonance".format(damage_type),
                               container.getModifiedItemAttr("subsystemBonusMinmatarDefensive"),
                               skill="Minmatar Defensive Systems")
