# powerBooster
#
# Used by:
# Modules from group: Capacitor Booster (59 of 59)
effectType = "active"


def handler(fit, container, context):
    # Set reload time to 10 seconds
    container.reloadTime = 10000

    if container.charge is None:
        return
    capAmount = container.getModifiedChargeAttr("capacitorBonus") or 0
    container.itemModifiedAttributes["capacitorNeed"] = -capAmount
