# scriptSensorBoosterScanResolutionBonusBonus
#
# Used by:
# Charges from group: Sensor Booster Script (3 of 3)
# Charges from group: Sensor Dampener Script (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    container.boostItemAttr("scanResolutionBonus", container.getModifiedChargeAttr("scanResolutionBonusBonus"))
