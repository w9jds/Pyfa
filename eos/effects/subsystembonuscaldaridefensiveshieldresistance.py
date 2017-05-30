# subsystemBonusCaldariDefensiveShieldResistance
#
# Used by:
# Subsystem: Tengu Defensive - Adaptive Shielding
effectType = "passive"


def handler(fit, container, context):
    for damage_type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("shield{0}DamageResonance".format(damage_type),
                               container.getModifiedItemAttr("subsystemBonusCaldariDefensive"),
                               skill="Caldari Defensive Systems")
