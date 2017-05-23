# fueledArmorRepair
#
# Used by:
# Modules from group: Ancillary Armor Repairer (4 of 4)
runTime = "late"
effectType = "active"


def handler(fit, module, context):
    amount = module.getModifiedItemAttr("armorDamageAmount") * module.fueledMultiplier
    speed = module.cycleTime / 1000.0
    fit.extraAttributes.increase("armorRepair", amount / speed)
