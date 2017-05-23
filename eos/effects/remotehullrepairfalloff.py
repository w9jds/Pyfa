# remoteHullRepairFalloff
#
# Used by:
# Modules from group: Remote Hull Repairer (8 of 8)
effectType = "projected", "active"
runTime = "late"


def handler(fit, module, context):
    if "projected" not in context:
        return
    bonus = module.getModifiedItemAttr("structureDamageAmount")
    duration = module.cycleTime / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
