# overloadSelfMissileGuidanceBonus5
#
# Used by:
# Modules from group: Missile Guidance Computer (3 of 3)
effectType = "overheat"


def handler(fit, container, context):
    for tgtAttr in (
            "aoeCloudSizeBonus",
            "explosionDelayBonus",
            "missileVelocityBonus",
            "maxVelocityModifier",
            "aoeVelocityBonus"
    ):
        container.boostItemAttr(tgtAttr, container.getModifiedItemAttr("overloadTrackingModuleStrengthBonus"))
