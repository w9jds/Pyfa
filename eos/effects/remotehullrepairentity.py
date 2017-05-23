# remoteHullRepairEntity
#
# Used by:
# Drones named like: Hull Maintenance Bot (6 of 6)
effectType = "projected", "active"
runTime = "late"


def handler(fit, module, context):
    if "projected" not in context:
        return
    bonus = module.getModifiedItemAttr("structureDamageAmount")
    duration = module.cycleTime / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
