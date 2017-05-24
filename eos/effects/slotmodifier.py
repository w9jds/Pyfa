# slotModifier
#
# Used by:
# Items from category: Subsystem (80 of 80)
effectType = "passive"


def handler(fit, container, context):
    fit.ship.increaseItemAttr("hiSlots", container.getModifiedItemAttr("hiSlotModifier"))
    fit.ship.increaseItemAttr("medSlots", container.getModifiedItemAttr("medSlotModifier"))
    fit.ship.increaseItemAttr("lowSlots", container.getModifiedItemAttr("lowSlotModifier"))
