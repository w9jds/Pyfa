# overloadSelfArmorDamageAmountDurationBonus
#
# Used by:
# Modules from group: Ancillary Armor Repairer (4 of 4)
# Modules from group: Armor Repair Unit (105 of 105)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("duration", container.getModifiedItemAttr("overloadSelfDurationBonus"))
    container.boostItemAttr("armorDamageAmount", container.getModifiedItemAttr("overloadArmorDamageAmount"),
                            stackingPenalties=True)
