# cloakingScanResolutionMultiplier
#
# Used by:
# Modules from group: Cloaking Device (12 of 14)
effectType = "offline"


def handler(fit, container, context):
    fit.ship.multiplyItemAttr("scanResolution",
                              container.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties=True, penaltyGroup="cloakingScanResolutionMultiplier")
