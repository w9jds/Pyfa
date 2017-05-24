# scanResolutionMultiplierOnline
#
# Used by:
# Modules from group: Warp Core Stabilizer (8 of 8)
# Module: Target Spectrum Breaker
effectType = "passive"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("scanResolution", container.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties=True)
