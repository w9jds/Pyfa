# overloadSelfMissileGuidanceModuleBonus
#
# Used by:
# Variations of module: Guidance Disruptor I (6 of 6)
effectType = "overheat"


def handler(fit, container, context):
    for tgtAttr in (
            "aoeCloudSizeBonus",
            "explosionDelayBonus",
            "missileVelocityBonus",
            "aoeVelocityBonus"
    ):
        container.boostItemAttr(tgtAttr, container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
