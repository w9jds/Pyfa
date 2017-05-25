# modifyShieldResonancePostPercent
#
# Used by:
# Modules from group: Shield Resistance Amplifier (88 of 88)
effectType = "passive"


def handler(fit, container, context):
    for resist_type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("shield%sDamageResonance" % resist_type.capitalize(),
                               container.getModifiedItemAttr("%sDamageResistanceBonus" % resist_type),
                               stackingPenalties=True)
