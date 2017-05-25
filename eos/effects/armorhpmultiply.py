# armorHPMultiply
#
# Used by:
# Modules from group: Armor Coating (202 of 202)
# Modules from group: Armor Plating Energized (187 of 187)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("armorHP", container.getModifiedItemAttr("armorHPMultiplier"))
