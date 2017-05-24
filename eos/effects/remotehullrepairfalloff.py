# remoteHullRepairFalloff
#
# Used by:
# Modules from group: Remote Hull Repairer (8 of 8)
effectType = "projected", "active"
runTime = "late"


def handler(fit, container, context):
    if "projected" not in context:
        return
    bonus = container.getModifiedItemAttr("structureDamageAmount")
    duration = container.cycleTime / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
