# armorRepair
#
# Used by:
# Modules from group: Armor Repair Unit (105 of 105)
runTime = "late"
effectType = "active"


def handler(fit, container, context):
    amount = container.getModifiedItemAttr("armorDamageAmount")
    speed = container.cycleTime / 1000.0
    fit.extraAttributes.increase("armorRepair", amount / speed)
