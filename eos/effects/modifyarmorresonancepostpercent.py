# modifyArmorResonancePostPercent
#
# Used by:
# Modules from group: Armor Coating (202 of 202)
# Modules from group: Armor Plating Energized (187 of 187)
effectType = "passive"


def handler(fit, container, context):
    for resist_type in ("kinetic", "thermal", "explosive", "em"):
        fit.ship.boostItemAttr("armor%sDamageResonance" % resist_type.capitalize(),
                               container.getModifiedItemAttr("%sDamageResistanceBonus" % resist_type),
                               stackingPenalties=True)
