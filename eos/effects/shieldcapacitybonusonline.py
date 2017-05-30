# shieldCapacityBonusOnline
#
# Used by:
# Modules from group: Shield Extender (33 of 33)
# Modules from group: Shield Resistance Amplifier (88 of 88)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("shieldCapacity", container.getModifiedItemAttr("capacityBonus"))
