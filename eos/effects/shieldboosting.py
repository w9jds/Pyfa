# shieldBoosting
#
# Used by:
# Modules from group: Shield Booster (93 of 93)
runTime = "late"
effectType = "active"


def handler(fit, container, context):
    amount = container.getModifiedItemAttr("shieldBonus")
    speed = container.cycleTime / 1000.0
    fit.extraAttributes.increase("shieldRepair", amount / speed)
