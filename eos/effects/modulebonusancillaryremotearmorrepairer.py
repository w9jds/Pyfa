# moduleBonusAncillaryRemoteArmorRepairer
#
# Used by:
# Modules from group: Ancillary Remote Armor Repairer (4 of 4)
runTime = "late"
effectType = "projected", "active"


def handler(fit, container, context, **kwargs):
    if "projected" not in context:
        return

    amount = container.getModifiedItemAttr("armorDamageAmount") * container.fueledMultiplier
    speed = container.cycleTime / 1000.0
    fit.extraAttributes.increase("armorRepair", amount / speed, **kwargs)
