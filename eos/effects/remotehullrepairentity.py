# remoteHullRepairEntity
#
# Used by:
# Drones named like: Hull Maintenance Bot (6 of 6)
effectType = "projected", "active"
runTime = "late"


def handler(fit, container, context):
    if "projected" not in context:
        return
    bonus = container.getModifiedItemAttr("structureDamageAmount")
    duration = container.cycleTime / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
