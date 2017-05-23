# moduleBonusAncillaryRemoteShieldBooster
#
# Used by:
# Modules from group: Ancillary Remote Shield Booster (4 of 4)
runTime = "late"
effectType = "projected", "active"


def handler(fit, module, context, **kwargs):
    if "projected" not in context:
        return
    amount = module.getModifiedItemAttr("shieldBonus")
    speed = module.cycleTime / 1000.0
    fit.extraAttributes.increase("shieldRepair", amount / speed, **kwargs)
