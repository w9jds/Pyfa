# Not used by any item
effectType = "projected", "active"
runTime = "late"


def handler(fit, module, context):
    if "projected" not in context:
        return
    bonus = module.getModifiedItemAttr("structureDamageAmount")
    duration = module.cycleTime / 1000.0
    fit.extraAttributes.increase("hullRepair", bonus / duration)
