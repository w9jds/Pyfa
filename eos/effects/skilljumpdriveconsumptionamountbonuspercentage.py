# skillJumpDriveConsumptionAmountBonusPercentage
#
# Used by:
# Skill: Jump Fuel Conservation
effectType = "passive"


def handler(fit, skill, context):
    fit.ship.boostItemAttr("jumpDriveConsumptionAmount",
                           skill.getModifiedItemAttr("consumptionQuantityBonusPercentage") * skill.level)
