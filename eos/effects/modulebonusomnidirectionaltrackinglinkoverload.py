# moduleBonusOmnidirectionalTrackingLinkOverload
#
# Used by:
# Modules from group: Drone Tracking Modules (10 of 10)
effectType = "overheat"


def handler(fit, container, context):
    overloadBonus = container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus")
    container.boostItemAttr("maxRangeBonus", overloadBonus)
    container.boostItemAttr("falloffBonus", overloadBonus)
    container.boostItemAttr("trackingSpeedBonus", overloadBonus)
    container.boostItemAttr("aoeCloudSizeBonus", overloadBonus)
    container.boostItemAttr("aoeVelocityBonus", overloadBonus)
