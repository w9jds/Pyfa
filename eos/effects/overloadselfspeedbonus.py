# overloadSelfSpeedBonus
#
# Used by:
# Modules from group: Propulsion Module (127 of 127)
effectType = "overheat"


def handler(fit, container, context):
    container.boostItemAttr("speedFactor", container.getModifiedItemAttr("overloadSpeedFactorBonus"),
                            stackingPenalties=True)
