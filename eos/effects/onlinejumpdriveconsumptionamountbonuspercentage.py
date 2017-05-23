# onlineJumpDriveConsumptionAmountBonusPercentage
#
# Used by:
# Modules from group: Jump Drive Economizer (3 of 3)
runTime = "early"
effectType = ("projected", "passive")


def handler(fit, module, context):
    fit.ship.boostItemAttr("jumpDriveConsumptionAmount",
                           module.getModifiedItemAttr("consumptionQuantityBonusPercentage"), stackingPenalties=True)
