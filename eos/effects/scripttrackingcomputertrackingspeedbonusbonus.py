# scriptTrackingComputerTrackingSpeedBonusBonus
#
# Used by:
# Charges from group: Tracking Disruption Script (2 of 2)
# Charges from group: Tracking Script (2 of 2)
effectType = "passive"


def handler(fit, container, context):
    container.boostItemAttr("trackingSpeedBonus", container.getModifiedChargeAttr("trackingSpeedBonusBonus"))
