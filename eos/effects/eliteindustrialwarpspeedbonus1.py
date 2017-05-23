# eliteIndustrialWarpSpeedBonus1
#
# Used by:
# Ships from group: Blockade Runner (4 of 4)
effectType = "passive"


def handler(fit, ship, context):
    fit.ship.boostItemAttr("warpSpeedMultiplier", ship.getModifiedItemAttr("eliteBonusIndustrial1"),
                           skill="Transport Ships")
