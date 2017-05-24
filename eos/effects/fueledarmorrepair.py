# fueledArmorRepair
#
# Used by:
# Modules from group: Ancillary Armor Repairer (4 of 4)
runTime = "late"
effectType = "active"


def handler(fit, container, context):
    amount = container.getModifiedItemAttr("armorDamageAmount") * container.fueledMultiplier
    speed = container.cycleTime / 1000.0
    fit.extraAttributes.increase("armorRepair", amount / speed)
