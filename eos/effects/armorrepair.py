# armorRepair
#
# Used by:
# Modules from group: Armor Repair Unit (105 of 105)
runTime = "late"
effectType = "active"


def handler(fit, module, context):
    amount = module.getModifiedItemAttr("armorDamageAmount")
    speed = module.cycleTime / 1000.0
    fit.extraAttributes.increase("armorRepair", amount / speed)
