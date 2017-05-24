# scriptMassBonusPercentageBonus
#
# Used by:
# Charges from group: Warp Disruption Script (2 of 2)
effectType = "passive"
runTime = "early"


def handler(fit, container, context):
    container.boostItemAttr("massBonusPercentage", container.getModifiedChargeAttr("massBonusPercentageBonus"))
