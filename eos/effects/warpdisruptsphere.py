# warpDisruptSphere
#
# Used by:
# Modules from group: Warp Disrupt Field Generator (7 of 7)
effectType = "active"
runTime = "early"


def handler(fit, container, context):
    fit.ship.boostItemAttr("mass", container.getModifiedItemAttr("massBonusPercentage"))
    fit.ship.boostItemAttr("signatureRadius", container.getModifiedItemAttr("signatureRadiusBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "speedBoostFactor", container.getModifiedItemAttr("speedBoostFactorBonus"))
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Propulsion Module",
                                  "speedFactor", container.getModifiedItemAttr("speedFactorBonus"))
    fit.ship.forceItemAttr("disallowAssistance", 1)
