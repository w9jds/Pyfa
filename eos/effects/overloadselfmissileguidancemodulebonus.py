# overloadSelfMissileGuidanceModuleBonus
#
# Used by:
# Variations of module: Guidance Disruptor I (6 of 6)
effectType = "overheat"


def handler(fit, module, context):
    for tgtAttr in (
            "aoeCloudSizeBonus",
            "explosionDelayBonus",
            "missileVelocityBonus",
            "aoeVelocityBonus"
    ):
        module.boostItemAttr(tgtAttr, module.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
