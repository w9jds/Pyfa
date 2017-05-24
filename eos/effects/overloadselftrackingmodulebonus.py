# overloadSelfTrackingModuleBonus
#
# Used by:
# Modules named like: Tracking Computer (19 of 19)
# Variations of module: Tracking Disruptor I (6 of 6)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("maxRangeBonus", container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
    container.boostItemAttr("falloffBonus", container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
    container.boostItemAttr("trackingSpeedBonus", container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
