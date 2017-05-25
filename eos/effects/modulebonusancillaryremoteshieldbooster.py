# moduleBonusAncillaryRemoteShieldBooster
#
# Used by:
# Modules from group: Ancillary Remote Shield Booster (4 of 4)
runTime = "late"
effectType = "projected", "active"


def handler(fit, container, context, **kwargs):
    if "projected" not in context:
        return
    amount = container.getModifiedItemAttr("shieldBonus")
    speed = container.cycleTime / 1000.0
    fit.extraAttributes.increase("shieldRepair", amount / speed, **kwargs)
